#!/usr/bin/env python3
"""Crop a folder of screenshots using the requested fixed rectangle."""

from pathlib import Path
from PIL import Image


INPUT_DIR = Path("/home/amadeus/Projects/amdocs/native-multimodal-grafana-images")
OUTPUT_DIR = INPUT_DIR / "cropped"
X, Y, WIDTH, HEIGHT = 291, 0, 1211, 335


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    images = sorted(INPUT_DIR.glob("*.png"))
    if not images:
        raise SystemExit(f"No PNG files found in {INPUT_DIR}")

    for source in images:
        with Image.open(source) as image:
            right, bottom = X + WIDTH, Y + HEIGHT
            if right > image.width or bottom > image.height:
                raise ValueError(
                    f"{source.name} is {image.width}x{image.height}; "
                    f"crop requires at least {right}x{bottom}"
                )
            image.crop((X, Y, right, bottom)).save(OUTPUT_DIR / source.name)

    print(f"Cropped {len(images)} images into {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
