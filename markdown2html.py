#!/usr/bin/python3

import sys
import os

def main():
    """
    Main function to handle the conversion of Markdown to HTML.
    It validates the command line arguments and checks the existence of the input file.
    """
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    # Extract the filenames from arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Check if the Markdown file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    
    # If everything is okay, exit with code 0
    sys.exit(0)

# Ensure this script is not executed when imported
if __name__ == "__main__":
    main()
