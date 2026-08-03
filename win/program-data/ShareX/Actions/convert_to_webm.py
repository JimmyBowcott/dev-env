# Copyright © 2025 VACAC. All rights reserved.

import os
import subprocess

inputFolder = r"D:/Jimmy_Bowcott/Screen_Capture/"

for file in os.listdir(inputFolder):
    filename = os.fsdecode(file)
    input = os.path.join(inputFolder, filename)
    output = os.path.join(inputFolder, filename.split(".")[0] + ".webm")
    if file.endswith(".mp4") and not os.path.exists(output):
        process = subprocess.run(
            [
                "ffmpeg",
                "-i",
                input,
                "-vf",
                "scale=1920:-2",
                "-c:v",
                "libvpx",
                "-b:v",
                "2.2M",
                "-maxrate",
                "2.6M",
                "-bufsize",
                "5.2M",
                "-deadline",
                "realtime",
                "-cpu-used",
                "6",
                "-threads",
                "0",
                "-auto-alt-ref",
                "0",
                "-lag-in-frames",
                "0",
                "-c:a",
                "libopus",
                "-b:a",
                "96k",
                "-compression_level",
                "0",
                output,
            ]
        )
