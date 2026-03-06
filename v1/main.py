import os
import time
from collections import deque
from google import genai
from google.genai import types
from dotenv import load_dotenv
from tool_registry import TOOLS
from prompts import SYSTEM_PROMPT


load_dotenv()


client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Conversation memory
MAX_HISTORY = 20
conversation_history = deque(maxlen=MAX_HISTORY)

# Convert tool registry to Gemini tool format
tool_schemas = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name=name,
                description=tool["description"],
                parameters=tool["parameters"],
            )
        ]
    )
    for name, tool in TOOLS.items()
]


def safe_generate(**kwargs):
    retries = 3

    for attempt in range(retries):
        try:
            return client.models.generate_content(**kwargs)
        except Exception as e:
            if "503" in str(e) and attempt < retries - 1:
                print("Gemini overloaded. Retrying...")
                time.sleep(2)
            else:
                raise

def load_agent_memory(data):
    try:
        conversation_history.clear()

        for msg in data[-MAX_HISTORY:]:
            role = "model" if msg["role"] == "assistant" else "user"

            conversation_history.append(
                {
                    "role": role,
                    "parts": [{"text": msg["content"]}],
                }
            )
    except:
        pass


def run_agent(user_input: str, history: list):
    load_agent_memory(history)

    # Ignore meaningless inputs
    if user_input.strip().lower() in ["", ".", "ok", "okay", "sure", "no"]:
        return "Alright."

    # Add user message to history
    conversation_history.append(
        {
            "role": "user",
            "parts": [{"text": user_input}],
        }
    )

    response = safe_generate(
        model="gemini-2.5-flash",
        contents=conversation_history,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=tool_schemas,
        ),
    )

    candidate = response.candidates[0]
    
    conversation_history.append(candidate.content)

    # Check if function was called
    if candidate.content.parts:
        for part in candidate.content.parts:
            if part.function_call:
                
                function_name = part.function_call.name
                arguments = dict(part.function_call.args)

                if function_name not in TOOLS:
                    return f"Error: Unknown tool '{function_name}'"

                print("\n TOOL CALLED:")
                print("Tool Name:", function_name)
                print("Arguments:", arguments)

                # Execute tool
                result = TOOLS[function_name]["function"](**arguments)

                print("Result:", result)
                print("-" * 50)

                # Add tool response to history
                conversation_history.append(
                    {
                        "role": "tool",
                        "parts": [
                            {
                                "function_response": {
                                    "name": function_name,
                                    "response": {"result": result},
                                }
                            }
                        ],
                    }
                )

                # Send tool response back
                followup = safe_generate(
                    model="gemini-2.5-flash",
                    contents=conversation_history,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        tools=tool_schemas,
                    ),
                )

                conversation_history.append(followup.candidates[0].content)

                text_parts = []

                for part in followup.candidates[0].content.parts:
                    if hasattr(part, "text") and part.text:
                        text_parts.append(part.text)

                if text_parts:
                    return "\n".join(text_parts)

                print("Warning: Model returned no text response.")
                return "Task completed successfully." 

    conversation_history.append(response.candidates[0].content)

    return response.text


if __name__ == "__main__":
    print("\nFile Management Agent")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        query = input("User: ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        output = run_agent(user_input=query, history=[])
        print("Agent:", output)
