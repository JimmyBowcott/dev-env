import os
import subprocess

input_folder = r""

for root, _, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(".png"):
            input_path = os.path.join(root, file)
            output_path = os.path.splitext(input_path)[0] + ".webp"
            cmd = [
                "ffmpeg",
                "-i", input_path,
                "-c:v", "libwebp",
                "-q:v", "100",
                output_path
            ]
            process = subprocess.run(cmd, shell=True)
            os.remove(input_path)
