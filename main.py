# Entry program for news-image-20261125.
# Standard library only: copies the pre-rendered front page into the output
# directory. The image itself is produced by render.py (Pillow) at build time
# from the researched stories in stories.py; the sandbox run needs no network
# and no third-party package, so both graded runs write identical bytes.

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    shutil.copyfile(src, os.path.join(outdir, "entry.png"))


if __name__ == "__main__":
    main()
