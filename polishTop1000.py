import json
import re

def count_lines(file_path):
    print("Opening...")
    with open(file_path, 'r', encoding='utf-8') as file:
        print("File opened. Counting lines.")
        return sum(1 for _ in file)

def extract_sections(input_file_path, output_json_path):
    total_lines = count_lines(input_file_path)
    print(f"Total number of lines in file: {total_lines}")

    start_phrase = "{{pl-freq 1990"
    end_phrase = "}}"
    title_start = "<title>"
    title_end = "</title>"
    title_pattern = r"title=([^\|}]+)"  # Regex to extract title= value
    sections = []
    current_section = ""
    original_title = ""
    capturing = False

    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if title_start in line:
                # Save current section before starting a new title
                if capturing and current_section:
                    sections.append(current_section)
                    current_section = ""
                    capturing = False
                # Extract the title text
                original_title = line[line.find(title_start) + len(title_start):line.find(title_end)]

            if start_phrase in line:
                capturing = True
                title_in_line = re.search(title_pattern, line)
                if title_in_line:
                    # If there's a custom title, use it for this section
                    current_title = f"<title>{title_in_line.group(1)}</title>\n"
                else:
                    # No custom title found; use the original title
                    current_title = f"<title>{original_title}</title>\n"
                current_section += current_title + line

                if end_phrase in line:
                    # If the end phrase is in the same line, stop capturing
                    sections.append(current_section)
                    current_section = ""
                    capturing = False
            elif capturing:
                # If already capturing, append the line to the current section
                current_section += line
                if end_phrase in line:
                    # If the end phrase is found, stop capturing and save the section
                    sections.append(current_section)
                    current_section = ""
                    capturing = False

    # In case the file ends and there was an ongoing capture
    if capturing and current_section:
        sections.append(current_section)

    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(sections, json_file, ensure_ascii=False, indent=4)
    
    print("Extraction complete. Results saved to:", output_json_path)


# Usage
input_file_path = '/Users/erikbergman/Documents/Programmering/Pythonprojekt/PolishTop1000/enwiktionary-latest-pages-articles.xml'  # Update this path to your file's path
output_json_path = 'extracted_sections.json'
extract_sections(input_file_path, output_json_path)