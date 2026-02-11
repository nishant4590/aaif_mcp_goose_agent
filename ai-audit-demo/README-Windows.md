# 🪿 Goose + MCP + Agents — Windows Setup Guide

This guide explains how to start a Goose session on **Windows** using:
- `agents.md`
- a local **MCP server (Python)**
- a Goose command-line extension

---

## 📁 Project Structure
```
ai-audit-demo\
├── agents.md
├── audit_tool.py
├── .venv\
└── README-Windows.md
```

---

## ✅ Prerequisites
- Windows 10 / 11
- Python 3.11 or 3.12
- Goose CLI ≥ 1.21
- OpenAI API key

---

## 1️⃣ Install Goose
```powershell
scoop install goose
goose --version
```

---

## 2️⃣ Create Python Virtual Environment
```powershell
cd ai-audit-demo
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install mcp
python -c "import mcp; print('mcp ok')"
deactivate
```

---

## 3️⃣ Configure Goose
```powershell
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
C:\path\to\ai-audit-demo\.venv\Scripts\python.exe
```
- Args:
```
C:\path\to\ai-audit-demo\audit_tool.py
```

---

## 4️⃣ Environment Variables
```powershell
setx OPENAI_API_KEY "sk-xxxx"
```

Restart terminal after setting.

---

## 5️⃣ Start Session
```powershell
goose session
```

---

## 6️⃣ agents.md Example
```markdown
# Auditor Agent
Inspect responses and enforce audit policy.
```
