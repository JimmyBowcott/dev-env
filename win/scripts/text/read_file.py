import chardet
import re
input_file = ""
output_file = ""
encoding = "utf-8"

with open(input_file, 'rb') as f:
    raw_data = f.read()
    res = chardet.detect(raw_data)
    encoding = res['encoding']
    print(f"Detected {encoding} encoding")


with open(input_file, "r", encoding=encoding) as f:
    print("Reading lines from", input_file)
    lines = f.readlines()

counter = 0

pattern = r'"[a-z]+":\s*"(\d+)"'
dimensions = [0,0,0]
output = [""] * len(lines)
to_replace = {}
for i, line in enumerate(lines):

    if '"length"' in line:
        match = re.search(pattern, line)
        if match:
            number = match.group(1)
            dimensions[0] = int(number)

    elif '"width"' in line:
        match = re.search(pattern, line)
        if match:
            number = match.group(1)
            dimensions[1] = int(number)

    elif '"depth"' in line:
        match = re.search(pattern, line)
        if match:
            number = match.group(1)
            dimensions[2] = int(number)
        dimensions.sort()
        to_replace[i-2] = f'        "length": "{dimensions[2]}",\n'
        to_replace[i-1] = f'        "width": "{dimensions[1]}",\n'
        to_replace[i] = f'        "depth": "{dimensions[0]}",\n'

for i, line in enumerate(lines):
    if i in to_replace:
        output[i] = to_replace[i]
    else:
        output[i] = line


with open(output_file, 'w', encoding=encoding) as f:
    f.writelines(output)
    print(f"Wrote {len(output)} lines to {output_file}")



