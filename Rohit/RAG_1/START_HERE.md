# 🚀 START HERE - RAG_1 Project Setup

**⏱️ Total Time: 15 minutes (mostly automatic)**

---

## What You'll Do

1. ✅ Create Python environment (1 min)
2. ✅ Install packages (3-5 min, automatic)
3. ✅ Verify installation (1 min)
4. ✅ Run tests (1 min)
5. ✅ Add API key (2 min)
6. ✅ Run everything (1 min)

---

## 🎯 Copy & Paste These Commands

**Open PowerShell and run these commands one at a time:**

### Command 1: Navigate to Project
```powershell
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_1
```

### Command 2: Create Virtual Environment
```powershell
python -m venv venv
```
⏱️ Wait for it to complete (~30 seconds)

### Command 3: Activate Environment
```powershell
venv\Scripts\Activate.ps1
```
✓ You should see `(venv)` at the start of your prompt

### Command 4: Upgrade pip
```powershell
python -m pip install --upgrade pip
```

### Command 5: Install All Dependencies
```powershell
pip install -r requirements.txt
```
⏱️ **WAIT - This will take 3-5 minutes** (automatic, be patient)

### Command 6: Verify Installation
```powershell
python check_dependencies.py
```
✓ You should see: `✓ package-name` for all packages

### Command 7: Run Unit Tests (Quick Check)
```powershell
pytest tests/unit/ -v
```
✓ You should see tests passing or skipping correctly

---

## 🔑 Add Your API Key (IMPORTANT!)

### Step 1: Get your OpenAI API key
- Go to: https://platform.openai.com/account/api-keys
- Click "Create new secret key"
- Copy the key (you can only see it once!)

### Step 2: Add it to `.env` file
```powershell
code .env
```

This opens the `.env` file in VS Code. Find this line:
```
OPENAI_API_KEY=your-key-here
```

Replace `your-key-here` with your actual key. Should look like:
```
OPENAI_API_KEY=sk-proj-abc123xyz...
```

**Then save the file (Ctrl+S)**

---

## ✅ Verify Everything Works

### Run All Tests
```powershell
pytest tests/ -v
```

### Try the Example
```powershell
python main.py
```

---

## 📖 Next Steps

After everything works:

1. **Quick Reference**: Read [QUICKREF.md](QUICKREF.md) for commands
2. **Full Guide**: Read [README.md](README.md) for details
3. **Tweaks**: Edit `app/config/settings.py` if needed
4. **Your Code**: Import and use RAGPipeline in your code

---

## 🆘 If Something Goes Wrong

### Issue: "ModuleNotFoundError" or "No module named"
→ Make sure Command 5 completed successfully
→ Run: `python check_dependencies.py`

### Issue: "Command not found: pytest"
→ Make sure `(venv)` is shown in your prompt
→ Run Command 3 again: `venv\Scripts\Activate.ps1`

### Issue: "Permission denied"
→ Run PowerShell as Administrator

### More Issues?
→ Read [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 📍 You Are Here

```
Setup (YOU ARE HERE) → Install → Verify → Test → Use
```

---

## 🎉 Quick Command Reference

| What | Command |
|-----|---------|
| Activate environment | `venv\Scripts\Activate.ps1` |
| Run unit tests | `pytest tests/unit/ -v` |
| Run all tests | `pytest tests/ -v` |
| Run with coverage | `pytest --cov=app tests/` |
| Try example | `python main.py` |
| Check dependencies | `python check_dependencies.py` |
| View logs | `Get-Content logs/rag_pipeline.log -Tail 50` |
| Done/Quit | `deactivate` |

---

## ✨ That's It!

You're done with setup. Your RAG system is ready to use!

**Next time you start (every session):**
```powershell
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_1
venv\Scripts\Activate.ps1
```

Then run:
- `pytest tests/ -v` to test
- `python main.py` to use
- Or import in your code: `from app.rag import RAGPipeline`

---

**Questions?** → Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
**Commands?** → Check [QUICKREF.md](QUICKREF.md) or [COMMANDS.md](COMMANDS.md)
**Details?** → Check [README.md](README.md) or [INSTALL.md](INSTALL.md)

---

**Ready? Copy Command 1 and paste it into PowerShell! 🚀**
