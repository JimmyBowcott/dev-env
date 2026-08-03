import chardet
input_file = ""
encoding = "utf-8"

with open(input_file, 'rb') as f:
    raw_data = f.read()
    res = chardet.detect(raw_data)
    encoding = res['encoding']
    print(f"Detected {encoding} encoding")


def clean_file(input_file, output_file):
    with open(input_file, 'r', encoding=encoding) as f:
        lines = f.readlines()
    cleaned_lines = []
    previous_blank = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("//"):
            continue
        if stripped == "":
            if not previous_blank:
                cleaned_lines.append("\n")
                previous_blank = True
        else:
            cleaned_lines.append(line)
            previous_blank = False
    with open(output_file, 'w') as f:
        f.writelines(cleaned_lines)

clean_file(input_file, input_file)
