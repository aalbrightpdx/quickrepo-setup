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
python3 setup_repo.py
```

The script will guide you step-by-step!

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

## License

MIT License
