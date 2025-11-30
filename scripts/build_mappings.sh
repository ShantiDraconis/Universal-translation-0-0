#!/usr/bin/env bash
set -euo pipefail

echo "▶️ Construindo mapeamento Harappan ↔ 00..."
python -m harappan_00.cli
echo "✅ Concluído."
