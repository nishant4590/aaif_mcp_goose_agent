# 🪿 Goose + MCP + Agents — macOS Setup Guide

This guide explains how to start a Goose session on **macOS** using:
- `agents.md`
- a local **MCP server (Python)**
- a Goose command-line extension

---

## 📁 Project Structure
```
ai-audit-demo/
├── agents.md
├── audit_tool.py
├── .venv/
└── README-macOS.md
```

---

## ✅ Prerequisites
- macOS 13+
- Python 3.11 or 3.12
- Goose CLI ≥ 1.21
- OpenAI API key

---

## 1️⃣ Install Goose
```bash
brew install block-goose
goose --version
```

---

## 2️⃣ Create Python Virtual Environment
```bash
cd ai-audit-demo
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install mcp
python -c "import mcp; print('mcp ok')"
deactivate
```

---

## 3️⃣ Configure Goose
```bash
goose configure
```

### Provider
- OpenAI
- Streaming: Yes
- Base path: v1/chat/completions
- Model: gpt-4o-mini

### Command-line Extension
- Name: auditor
- Command:
```
/absolute/path/to/ai-audit-demo/.venv/bin/python
```
- Args:
```
/absolute/path/to/ai-audit-demo/audit_tool.py
```

---

## 4️⃣ Environment Variables
```bash
export OPENAI_API_KEY="sk-xxxx"
```

---

## 5️⃣ Start Session
```bash
goose session
```

---

## 6️⃣ agents.md Example
```markdown
# Auditor Agent
Inspect responses and enforce audit policy.
```
