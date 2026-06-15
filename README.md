# Fast_Api_Tutorial

## FastAPI Setup

Use a virtual environment so project dependencies stay separate from your system Python.

### Linux / macOS

```bash
# Check Python version
python3 --version

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install FastAPI and related modules
pip install fastapi uvicorn[standard] pydantic python-multipart sqlalchemy

# Optional: save installed packages
pip freeze > requirements.txt
```

### Windows

```powershell
# Check Python version
python --version

# Create virtual environment
python -m venv venv

# Activate virtual environment in PowerShell
.\venv\Scripts\Activate.ps1

# If PowerShell blocks activation, run this once:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Upgrade pip
python -m pip install --upgrade pip

# Install FastAPI and related modules
pip install fastapi uvicorn[standard] pydantic python-multipart sqlalchemy

# Optional: save installed packages
pip freeze > requirements.txt
```

For Command Prompt on Windows, activate the virtual environment with:

```cmd
venv\Scripts\activate.bat
```

## Install From Requirements

If `requirements.txt` already exists, install dependencies with:

```bash
pip install -r requirements.txt
```

## Run FastAPI App

If your main file is `main.py` and your FastAPI object is named `app`, run:

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative API documentation:

```text
http://127.0.0.1:8000/redoc
```

## Deactivate Virtual Environment

```bash
deactivate
```
