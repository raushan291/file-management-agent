# File Management Agent

A simple **Agentic AI application** that can manage files and directories using natural language.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/raushan291/file-management-agent.git
cd file-management-agent/v1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

---

## Run the Application

Start the Streamlit UI:

```bash
streamlit run app.py
```

## Usage

Open the Streamlit interface and ask things like:

* `List files`
* `Create a folder named test`
* `Delete file sample.txt`
* `Create a Python file hello.py`
* `Write a hello world program in hello.py`
* `Add a function to calculate factorial in math_utils.py`
* `Show the content of hello.py`
* `Read the file config.json`
* `Run hello.py`
* `Execute the script main.py`

By default, the agent works in the **current working directory**.

---
