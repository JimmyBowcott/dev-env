# Batch converts all videos in a folder into webm format
import os
import subprocess

# path to ffmpeg
ffmpegPath = "C:/Users/JamesBowcott/Documents/ffmpeg/bin/ffmpeg.exe"

# path to the folder containing the videos you want to convert
inputFolder = r"D:/blender_out/"

# default is 32, raising this value will lower the file size but potentially reduce quality. Can be in the range 1 - 51
crf = "40"

for file in os.listdir(inputFolder):
    if file.endswith(".mp4"):
        print("Processing: ", file)
        filename = os.fsdecode(file)
        input = os.path.join(inputFolder, filename)
        output = os.path.join(inputFolder, filename.split(".")[0] + ".webm")
        process = subprocess.run([ffmpegPath, "-i", input, "-c:v", "libvpx", "-pix_fmt", "yuva420p", "-b:v", "2M", "-auto-alt-ref", "0", output])
        # process = subprocess.run([ffmpegPath, "-i", input, "-c:v", "libvpx-vp9", "-crf", crf, output])
        # if process.returncode == 0 and os.path.exists(output): # i.e. successful
        #     os.remove(output)
