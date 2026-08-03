import base64
import argparse

parser = argparse.ArgumentParser(
                    prog='png2b64',
                    description='Reads PNG to base64')

parser.add_argument('filename')

args = parser.parse_args()

if not args.filename:
    print("Error: Filname not provided!")
elif not args.filename.endswith(".png"):
    print("Error: Incorrect file type. This only takes .png.")
else:
    with open(args.filename, "rb") as img:
        print(base64.b64encode(img.read()))
