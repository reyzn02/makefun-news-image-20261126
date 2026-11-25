"""Entry program for make.fun bounty news-image-20261126.

Copies the pre-built editorial image (entry.png) to the grader's
output directory as entry.png, then verifies the copy: it must be a
whole PNG (correct magic bytes) and byte-identical to the source, so
a corrupt or truncated asset fails loudly instead of being judged.
Standard library only, no network.

The image itself is drawn by draw.py in this repository (Pillow,
run at build time): a newspaper front page summing up Thursday
26 November 2026 — six verified stories plus a footer strip.
"""

import hashlib
import os
import shutil
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _head(path: Path, size: int = 8) -> bytes:
    with open(path, "rb") as fh:
        return fh.read(size)


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"missing image asset: {source}")
    if _head(source) != PNG_MAGIC:
        raise ValueError("entry.png is not a valid PNG file")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)

    # Verify the copy before exiting: same bytes, whole PNG.
    if _head(target) != PNG_MAGIC:
        raise ValueError("copied entry.png is not a valid PNG file")
    if _sha256(target) != _sha256(source):
        raise ValueError("copied entry.png differs from the source image")


if __name__ == "__main__":
    main()
