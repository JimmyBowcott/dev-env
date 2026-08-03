#########################################################################
#                                                                       #
# Checks that paths listed in a PDF file exist.                         #
# Use via command line (e.g. python script.py example.pdf).             #
# Requires pdfminer package (MIT)                                       #
#                                                                       #
#########################################################################

from pdfminer.high_level import extract_text
import logging
import os
import re
import argparse
import csv

logging.getLogger("pdfminer").setLevel(logging.ERROR) # This mutes the warnings from extract_text

def extract_paths_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    text = text.replace("\n", "")
    paths = re.findall(r'"[A-Z]:[\\/][^"\r\n]*?"', text)
    return list(set(paths))

def check_paths_exist(paths):
    results = {}
    for path in paths:
        path = path[1:-1] # Remove ""
        normalized_path = os.path.normpath(path)
        exists = os.path.exists(normalized_path)
        results[normalized_path] = exists
    return results

def write_results_to_csv(results, output_file, missing_only=False):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Path', 'Exists'])
        for path, exists in results.items():
            if missing_only and exists:
                continue
            writer.writerow([path, 'Yes' if exists else 'No'])

def main():
    parser = argparse.ArgumentParser(description="Check if paths in a PDF exist on the system.")
    parser.add_argument("pdf_file", help="Path to the PDF file.")
    parser.add_argument("--output", help="Output CSV file (optional).")
    parser.add_argument("--missing-only", action="store_true", help="Only show missing paths.")
    args = parser.parse_args()

    if not os.path.exists(args.pdf_file):
        print(f"Error: File '{args.pdf_file}' not found.")
        return

    print(f"Reading: {args.pdf_file}")
    paths = extract_paths_from_pdf(args.pdf_file)
    print(f"Found {len(paths)} paths.")
    results = check_paths_exist(paths)

    if args.output:
        write_results_to_csv(results, args.output, args.missing_only)
        print(f"Results written to: {args.output}")
    else:
        for path, exists in results.items():
            if args.missing_only and exists:
                continue
            if not exists:
                print(f"{path} not found.")

if __name__ == "__main__":
    main()
