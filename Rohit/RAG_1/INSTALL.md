"""
RAG_1 Installation Guide

Quick Setup Instructions to Run Tests
"""

# ============================================================================
# STEP 1: OPEN POWERSHELL AND NAVIGATE TO RAG_1
# ============================================================================

```powershell
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_1
```


# ============================================================================
# STEP 2: CREATE VIRTUAL ENVIRONMENT (if not already created)
# ============================================================================

```powershell
python -m venv venv
```


# ============================================================================
# STEP 3: ACTIVATE VIRTUAL ENVIRONMENT
# ============================================================================

```powershell
venv\Scripts\Activate.ps1
```

# You should see (venv) at the start of the command prompt


# ============================================================================
# STEP 4: UPGRADE PIP
# ============================================================================

```powershell
python -m pip install --upgrade pip
```


# ============================================================================
# STEP 5: INSTALL ALL DEPENDENCIES
# ============================================================================

```powershell
pip install -r requirements.txt
```

# This will install all required packages. Be patient, it may take a few minutes.


# ============================================================================
# STEP 6: VERIFY INSTALLATION
# ============================================================================

```powershell
# Check installed packages
python check_dependencies.py

# You should see all packages marked as ✓
```


# ============================================================================
# STEP 7: RUN TESTS
# ============================================================================

```powershell
# Run all tests
pytest tests/ -v

# Run only unit tests (fastest)
pytest tests/unit/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/unit/test_loader.py -v
```


# ============================================================================
# TROUBLESHOOTING
# ============================================================================

## Issue: Still getting "ModuleNotFoundError"

Solution 1: Make sure virtual environment is activated
```powershell
# Check for (venv) at start of prompt
# If missing, run:
venv\Scripts\Activate.ps1
```

Solution 2: Reinstall dependencies
```powershell
pip install --upgrade -r requirements.txt
```

Solution 3: Clear pip cache and reinstall
```powershell
pip cache purge
pip install -r requirements.txt
```


## Issue: "Command not found: pytest"

Solution: Make sure venv is activated
```powershell
venv\Scripts\Activate.ps1
pytest --version
```


## Issue: "No module named 'app'"

Solution: Make sure you're in the RAG_1 directory
```powershell
pwd  # Should show: C:\...\RAG_1
```


## Issue: Python version too old

Solution: Check Python version
```powershell
python --version
# Need Python 3.8 or higher
```


# ============================================================================
# QUICK START COMMANDS
# ============================================================================

Full setup in one go:
```powershell
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_1
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest tests/unit/ -v
```


# ============================================================================
# WHAT EACH TOOL DOES
# ============================================================================

| Command | Purpose |
|---------|---------|
| `venv\Scripts\Activate.ps1` | Activate Python virtual environment |
| `pip install -r requirements.txt` | Install all dependencies |
| `python check_dependencies.py` | Verify all packages installed |
| `pytest tests/ -v` | Run all tests with verbose output |
| `pytest tests/unit/ -v` | Run unit tests only |
| `pytest tests/ --cov=app` | Run tests with coverage report |


# ============================================================================
# DEACTIVATE VIRTUAL ENVIRONMENT (when done)
# ============================================================================

```powershell
deactivate
```

This will return to your system Python environment.

