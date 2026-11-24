#!/usr/bin/env python3
"""Write one meme image to /output/entry.png.

The image is bundled in this repo as meme.png (1024x1024, under
1 MiB) and copied deterministically, byte for byte, with no network.
"""

import os
import shutil


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(here, "meme.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
