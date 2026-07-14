# =====================================
# Python Backend Development Environment
# Ubuntu / Debian
# =====================================

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.12
sudo apt install python3.12 python3.12-venv python3-pip -y

# Verify Python
python3.12 --version

# Create virtual environment
python3.12 -m venv .venv

# Activate environment
source .venv/bin/activate

# (Optional) Upgrade pip
python -m pip install --upgrade pip

# Install uv (optional, recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Git
sudo apt install git -y

# Configure Git
git config --global user.name "Anushervon Saloev"
git config --global user.email "saloev05@gmail.com"

# Generate SSH key
ssh-keygen -t ed25519 -C "text"

# Show public SSH key
cat ~/.ssh/id_ed25519.pub

# Install VS Code (Snap)
sudo snap install code --classic

# Install VS Code extensions
code --install-extension ms-python.python
code --install-extension charliermarsh.ruff
code --install-extension eamodio.gitlens
code --install-extension ms-azuretools.vscode-docker

# Install Docker
curl -fsSL https://get.docker.com | sh

# Allow current user to use Docker
sudo usermod -aG docker $USER
newgrp docker

# Verify Docker
docker run hello-world

# Clone repository
git clone git@github.com:.git
cd <REPO>

# Install FastAPI
pip install fastapi uvicorn

# Run FastAPI
uvicorn main:app --reload