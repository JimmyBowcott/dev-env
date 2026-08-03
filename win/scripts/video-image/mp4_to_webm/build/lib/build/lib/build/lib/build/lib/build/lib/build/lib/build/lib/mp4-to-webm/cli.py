# Copyright © 2025 VACAC. All rights reserved.
# Batch converts all videos in a folder into webm format

import os
import subprocess
import argparse
import sys

def convert_folder(input_folder: str, crf: int):
    if not os.path.isdir(input_folder):
        print(f"Error: '{input_folder}' is not a valid directory.")
        sys.exit(1)

    for file in os.listdir(input_folder):
        if file.lower().endswith(".mp4"):
            print("Processing:", file)

            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(
                input_folder,
                os.path.splitext(file)[0] + ".webm"
            )

            cmd = [
                "ffmpeg",
                "-i", input_path,
                "-c:v", "libvpx-vp9",
                "-crf", str(crf),
                "-b:v", "0",
                output_path,
            ]

            result = subprocess.run(cmd)

            if result.returncode != 0:
                print(f"Failed to convert: {file}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert all MP4 files in a folder to WebM using ffmpeg"
    )
    parser.add_argument(
        "folder",
        help="Path to folder containing MP4 files"
    )
    parser.add_argument(
        "--crf",
        type=int,
        default=40,
        help="Quality level (1-51, lower is better quality, default=40)"
    )

    args = parser.parse_args()

    convert_folder(args.folder, args.crf)

if __name__ == "__main__":
    main()
