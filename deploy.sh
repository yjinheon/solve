#!/bin/bash

echo -e "\033[0;32mDeploying solved code to Github\033[0m" # e means interpret backslash escapes

# Add changes to git.
git add .

# Commit changes.
msg="working in progres.. $(date)"
if [ $# -eq 1 ]; then
  msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin main
