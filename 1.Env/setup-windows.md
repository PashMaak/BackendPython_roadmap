# =====================================
# Python Backend Development Environment
# Windows (PowerShell)
# =====================================

# Verify winget
winget --version

# Install Python 3.12
winget install Python.Python.3.12

# Verify Python
python --version

# Create virtual environment
python -m venv .venv

# Activate environment
.venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install uv (optional)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install Git
winget install Git.Git

# Configure Git
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Generate SSH key
ssh-keygen -t ed25519 -C "you@example.com"

# Show public SSH key
type $env:USERPROFILE\.ssh\id_ed25519.pub

# Install VS Code
winget install Microsoft.VisualStudioCode

# Install VS Code extensions
code --install-extension ms-python.python
code --install-extension charliermarsh.ruff
code --install-extension eamodio.gitlens
code --install-extension ms-azuretools.vscode-docker

# Install Docker Desktop
winget install Docker.DockerDesktop

# Verify Docker
docker run hello-world

# Clone repository
git clone git@github.com:<ORG>/<REPO>.git
cd <REPO>

# Install FastAPI
pip install fastapi uvicorn

# Run FastAPI
uvicorn main:app --reload