"""Execute every generated API "Complete example" and report failures.

Backward-compatible wrapper for ``python docs/generate_api.py --verify``.
Run from the repository root:

    python docs/_tools/verify_api_examples.py [--pkg <subpackage>]
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from generate_api import main  # noqa: E402

if __name__ == "__main__":
    sys.argv = [sys.argv[0], "--verify", *sys.argv[1:]]
    sys.exit(main())
