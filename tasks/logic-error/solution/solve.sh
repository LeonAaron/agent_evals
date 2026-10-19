#!/bin/bash
set -euo pipefail

cat > /app/logic.py <<'PY'
from typing import List

def snap(input: List[int]):
    size = len(input) // 2
    result = sorted(input)
    result = result[:size]
    return result
PY
