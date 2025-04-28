# Git Repo Quick Setup Script 🛠️

A simple Python script to quickly initialize a new Git repository with smart checks and friendly prompts.

This script helps you:
- Ensure your Git global username and email are set
- Ensure you have an SSH key (and create one if missing)
- Initialize a Git repository if needed
- Add a remote origin (SSH preferred)
- Stage and commit all files
- Push your initial commit to GitHub

---

## How to Use

Navigate into your project directory and run:

```bash
python3 repo-setup.py
```

The script will guide you step-by-step!

## How to Install

### 1. Clone the repo into ~/.bin/quickrepo-setup

```bash
git clone git@github.com:aalbrightpdx/quickrepo-setup.git ~/.bin/quickrepo-setup
```

### 2. (Optional) Make a Shortcut Script

If you want to run it easily like:

```bash
repo-setup
```
from anywhere,
you can make a tiny wrapper script inside ~/.bin/.

Create a new file:

```bash
nano ~/.bin/repo-setup
```

Paste this inside:

```bash
#!/bin/bash
python3 ~/.bin/quickrepo-setup/repo-setup.py
```

Save and exit (CTRL+O, Enter, CTRL+X).

Make it executable:

```bash
chmod +x ~/.bin/repo-setup
```

✅ Now repo-setup becomes a command!

### 3. Add ~/.bin to your PATH (if it's not already)

First, check if ~/.bin is in your path:

```bash
echo $PATH
```

If you don't see it, add it to your shell config.

If you use bash:

```bash
echo 'export PATH="$HOME/.bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

✅ Now your terminal knows to look inside ~/.bin/ for commands!

## 📜 Quick Recap: Full Commands

```bash
# Clone the repo into ~/.bin
git clone git@github.com:aalbrightpdx/quickrepo-setup.git ~/.bin/quickrepo-setup

# Create shortcut launcher
echo -e '#!/bin/bash\npython3 ~/.bin/quickrepo-setup/repo-setup.py' > ~/.bin/repo-setup
chmod +x ~/.bin/repo-setup

# Add ~/.bin to PATH if needed
echo 'export PATH="$HOME/.bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 4. Test it

Now anywhere you are, you can type:

```bash
repo-setup
```

and it will run your fancy repo setup wizard! ✨🔥

## Features

🛠️ Check and set Git global username/email

🔑 Check for existing SSH key or create a new one

📂 Initialize Git repository if missing

🌍 Add remote SSH URL

📜 Stage and commit your project

🚀 Push to GitHub automatically

💬 Prompt for custom commit messages

---

## Requirements

Python 3.x installed

Git installed and configured

OpenSSH installed (for SSH key generation)

## Notes

SSH connection is recommended for pushing to GitHub.

If you don't yet have an SSH key, the script will help you create one.

Make sure you manually upload your public SSH key to GitHub under Settings > SSH and GPG keys.

## ✨ Recommended Next Step: Use GitHelper

After you configure a repository with repo-setup,
you can use githelper for regular day-to-day commits and pushes.

GitHelper is a simple CLI tool that:

    Shows which repo you are about to update

    Lets you review git status

    Guides you through adding, committing, and pushing safely

    Helps prevent mistakes like committing to the wrong repo

Install GitHelper just like QuickRepo-Setup for best results!

## License

MIT License
