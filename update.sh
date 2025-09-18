#!/bin/bash

# Wrapper script to update the glossary and push changes to GitHub,
# immediately executable after cloning the repository. This could
# also be run within a CI/CD pipeline to automate updates.

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 scraper.py
git add slang.json
git commit -m "Update glossary on $(date +'%Y-%m-%d') at $(date +'%H:%M:%S')"
git push
