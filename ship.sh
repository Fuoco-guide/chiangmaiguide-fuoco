#!/bin/bash
# Usage: ./ship.sh "commit message"
# Stages all changes (excluding .DS_Store, memory.md, CLAUDE.md) and pushes.
MSG="${1:-update}"
git add index.html
git add listing-*.webp 2>/dev/null
git commit -m "$MSG

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push origin main
