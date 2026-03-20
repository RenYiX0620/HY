#!/bin/bash
# Scrapling Fetcher Shell Wrapper
# 用法：./fetch.sh <url> [--selector <css_selector>] [--stealth]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$SCRIPT_DIR/fetch.py" "$@"
