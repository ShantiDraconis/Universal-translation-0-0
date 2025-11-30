#!/usr/bin/env bash
set -euo pipefail

echo "▶️ Building Harappan ↔ 00 mapping..."
python -m harappan_00.cli
echo "✅ Done."
