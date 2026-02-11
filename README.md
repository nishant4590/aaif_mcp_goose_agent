# aaif_mcp_goose_agent
🤖 Agentic Audit Demo: AAIF Coordination Flow This repository is a reference implementation of the Agentic AI Foundation (AAIF) "Triple Threat" stack. It demonstrates a secure, local-first coordination flow between Goose (The Worker), MCP (The Bridge), and AGENTS.md (The Policy).

🚀 Getting Started
1. Prerequisites

Goose CLI installed (brew install block-goose-cli)

Python 3.10+

An active LLM provider (GitHub Copilot, Anthropic, or OpenAI)

2. Installation

Bash
git clone https://github.com/your-username/ai-audit-demo.git
cd ai-audit-demo
pip install mcp
3. Register the MCP Extension

Add the custom auditor tool to your Goose configuration:

Bash
goose configure add extension --name auditor --cmd python --args \[$(pwd)/audit_tool.py\]
