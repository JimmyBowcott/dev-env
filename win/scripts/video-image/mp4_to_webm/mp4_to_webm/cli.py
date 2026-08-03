# Batch converts all videos in a folder into webm format

import os
import subprocess
import argparse
import sys

QUALITY_PRESETS = {
    "low": 45,
    "medium": 35,
    "high": 28,
    "veryhigh": 22,
    "lossless": 15,
}

def quality_to_crf(q):
    if isinstance(q, str) and q.lower() in QUALITY_PRESETS:
        return QUALITY_PRESETS[q.lower()]

    try:
        q = int(q)
        q = max(0, min(100, q))
        return int(45 - (q / 100) * 30)
    except:
        return 35

def convert_folder(input_folder: str, quality, vp8: bool, crf_override: int | None):
    if not os.path.isdir(input_folder):
        print(f"Error: '{input_folder}' is not a valid directory.")
        sys.exit(1)

    crf = crf_override if crf_override is not None else quality_to_crf(quality)

    for file in os.listdir(input_folder):
        if not file.lower().endswith(".mp4"):
            continue

        print("Processing:", file)

        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(
            input_folder,
            os.path.splitext(file)[0] + ".webm"
        )

        if vp8:
            cmd = [
                "ffmpeg",
                "-i", input_path,
                "-c:v", "libvpx",
                "-pix_fmt", "yuva420p",
                "-b:v", "2M",
                "-auto-alt-ref", "0",
                "-f", "webm",
                output_path
            ]
        else:
            cmd = [
                "ffmpeg",
                "-i", input_path,
                "-c:v", "libvpx-vp9",
                "-crf", str(crf),
                "-b:v", "0",
                output_path
            ]

        result = subprocess.run(cmd)

        if result.returncode != 0:
            print(f"Failed to convert: {file}")
        else:
            print(f"Converted: {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert MP4 videos to WebM (with presets + Unity compatibility)"
    )

    parser.add_argument("folder", help="Input folder")

    parser.add_argument(
        "--quality",
        default="medium",
        help="Quality: low, medium, high, veryhigh OR 0–100 (default: medium)"
    )

    parser.add_argument(
        "--crf",
        type=int,
        help="Override CRF directly (1–51)"
    )

    parser.add_argument(
        "--vp8",
        action="store_true",
        help="Use VP8 encoding (e.g. for Unity)"
    )

    args = parser.parse_args()

    convert_folder(
        args.folder,
        args.quality,
        args.vp8,
        args.crf
    )

if __name__ == "__main__":
    main()
