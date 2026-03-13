# File Management Agent

A simple **Agentic AI application** that can manage files and directories using **natural language**.

The agent can understand user instructions and perform file operations such as creating files, reading content, executing scripts, and managing directories.

This repository demonstrates the **evolution of the same application across multiple agent architectures**.

---

## Project Versions

This repository contains **different implementations** of the same application.

| Version | Architecture | Description |
|--------|-------------|-------------|
| **v1** | Basic LLM + Python tools | Direct tool calling without MCP |
| **v2** | MCP-based architecture | Tools exposed via Model Context Protocol server |
| **v3** | Google ADK + MCP | Agent built using Google Agent Development Kit |

---

## Repository Structure

```
file-management-agent/
│
├── v1/        # Basic agent implementation
├── v2/        # MCP-based tool integration
├── v3/        # ADK-based agent
└── README.md
```

Each version contains its own **setup instructions and usage details**.

---

## Quick Start

If you want to try the **latest implementation**, use **v3**.

For setup instructions and usage details, see the **v3 README**:  
[View v3 README](./v3/readme.md)

---
