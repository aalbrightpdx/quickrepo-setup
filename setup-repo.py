#!/usr/bin/env python3

import os
import subprocess
import sys

def run_cmd(cmd, capture_output=False, check_success=False):
    """Run a system command."""
    result = subprocess.run(cmd, shell=True, text=True,
                             capture_output=capture_output)
    if check_success:
        return result.returncode == 0
    if capture_output:
        return result.stdout.strip()
    return None

def check_git_global_user():
    """Check if Git global username and email are set."""
    username = run_cmd("git config --global user.name", capture_output=True)
    email = run_cmd("git config --global user.email", capture_output=True)
    return username, email

def set_git_global_user():
    """Prompt to set Git global username and email."""
    print("➤ No Git username/email found. Let's set them up!")
    username = input("Enter your Git username: ").strip()
    email = input("Enter your Git email address: ").strip()
    run_cmd(f'git config --global user.name "{username}"')
    run_cmd(f'git config --global user.email "{email}"')
    print(f"✅ Git global username and email set: {username} / {email}\n")

def check_ssh_key():
    """Check if an SSH key exists."""
    ssh_dir = os.path.expanduser("~/.ssh")
    if not os.path.isdir(ssh_dir):
        return False
    keys = [f for f in os.listdir(ssh_dir) if f.endswith(".pub")]
    return bool(keys)

def create_ssh_key():
    """Prompt to create a new SSH key."""
    print("➤ No SSH key found.")
    choice = input("Would you like to create one now? [y/n]: ").lower()
    if choice == 'y':
        email = run_cmd("git config --global user.email", capture_output=True) or input("Enter email for SSH key: ")
        run_cmd(f'ssh-keygen -t ed25519 -C "{email}"')
        print("✅ SSH key generated. Don't forget to add it to GitHub!")
    else:
        print("⚠️ Skipping SSH key creation. You will need one to push via SSH.")

def fix_remote_url(remote_input):
    """Auto-correct remote URL input."""
    if remote_input.startswith("git@github.com:"):
        return remote_input
    elif "/" in remote_input and not remote_input.startswith("http"):
        return f"git@github.com:{remote_input}"
    else:
        print("⚠️ Invalid remote format. Please enter 'username/repo.git' or full SSH URL like 'git@github.com:username/repo.git'.")
        sys.exit(1)

def main():
    # Step 1: Check Git global username/email
    username, email = check_git_global_user()
    if not username or not email:
        set_git_global_user()
    else:
        print(f"➤ Git user already set: {username} / {email}\n")

    # Step 2: Check SSH key
    if check_ssh_key():
        print("➤ SSH key found.\n")
    else:
        create_ssh_key()

    # Step 3: Check if already a Git repo
    if not os.path.isdir(".git"):
        init = input("➤ No Git repo found. Initialize new Git repo here? [y/n]: ").lower()
        if init == 'y':
            run_cmd("git init")
            print("✅ Initialized new Git repository.\n")
        else:
            print("❌ Exiting. No Git repo initialized.")
            sys.exit(0)
    else:
        print("➤ Git repo already initialized.\n")

    # Step 4: Add remote origin or fix if needed
    remotes = run_cmd("git remote -v", capture_output=True)
    if not remotes:
        remote_input = input("➤ Enter SSH path (e.g., username/repo.git or full SSH URL): ").strip()
        ssh_url = fix_remote_url(remote_input)
        run_cmd(f"git remote add origin {ssh_url}")
        print(f"✅ Remote origin set: {ssh_url}\n")
    else:
        print("➤ Remote already exists:\n" + remotes + "\n")
        change_remote = input("➤ Remote already exists. Do you want to change it? [y/n]: ").lower()
        if change_remote == 'y':
            remote_input = input("➤ Enter new SSH path (e.g., username/repo.git or full SSH URL): ").strip()
            ssh_url = fix_remote_url(remote_input)
            run_cmd(f"git remote set-url origin {ssh_url}")
            print(f"✅ Remote URL updated to SSH: {ssh_url}\n")

    # Step 5: Stage files
    run_cmd("git add .")
    print("✅ Staged all files.\n")

    # Step 6: Commit
    commit_message = input("➤ Enter a commit message: ").strip()
    if not commit_message:
        commit_message = "Initial commit"
    run_cmd(f'git commit -m "{commit_message}"')
    print(f"✅ Commit made: {commit_message}\n")

    # Step 7: Set branch to main
    run_cmd("git branch -M main")

    # Step 8: Push
    push_now = input("➤ Push to GitHub now? [y/n]: ").lower()
    if push_now == 'y':
        success = run_cmd("git push -u origin main", check_success=True)
        if success:
            print("✅ Pushed to GitHub!\n")
        else:
            print("❌ Push failed.\n")
            print("💡 Tip: You may need to run one of the following manually:")
            print("    git pull --rebase origin main")
            print("")
    else:
        print("⚠️ Push skipped. You can push later manually.\n")

    print("🎉 All done! Your forge glows brightly! 🔥")

if __name__ == "__main__":
    main()

