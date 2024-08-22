import re
from pathlib import Path
import time

DECOMPILED_SCRIPTS = Path("D:/Downloads/GTA Stuff/PC/.Other Stuff/03 - Codding/01 - Decompiled Scripts/v-decompiled-scripts-master")
OUTPUT_FILE = Path("extracted_globals.txt")

def extract_globals(file_content: str):
    pattern = re.compile(r'\bGlobal_(\d+)\b')
    return [int(match) for match in pattern.findall(file_content)]

def get_max_filename_length(directory: Path):
    max_length = 0
    for file_path in directory.rglob('*.c'):
        max_length = max(max_length, len(file_path.name))
    return max_length

def process_files(directory: Path, output_file: Path, max_filename_length: int):
    global_vars = set()

    with output_file.open('w', encoding='utf-8') as out_file:
        for file_path in directory.rglob('*.c'):
            file_name = file_path.name
            print(f'Processing: "{file_name}"', end="")

            content = file_path.read_text(encoding='utf-8')
            globals_in_file = extract_globals(content)

            new_globals = set(globals_in_file) - global_vars
            num_new_globals = len(new_globals)

            for var in new_globals:
                global_vars.add(var)
                out_file.write(f"Global_{var}\n")
                out_file.flush() # Ensure it is written to disk immediately

            print(f"{' ' * (max_filename_length - len(file_name))} .. Found {num_new_globals} new globals from this file.")

    return global_vars

if __name__ == "__main__":
    start_time = time.time()

    max_filename_length = get_max_filename_length(DECOMPILED_SCRIPTS)
    global_vars = process_files(DECOMPILED_SCRIPTS, OUTPUT_FILE, max_filename_length)

    if global_vars:
        smallest_global = min(global_vars)
        largest_global = max(global_vars)
        total_globals = len(global_vars)
    else:
        smallest_global = None
        largest_global = None
        total_globals = 0

    end_time = time.time()

    total_time = end_time - start_time

    print()
    if global_vars:
        print(f"Smallest Global Number: Global_{smallest_global}")
        print(f"Largest Global Number: Global_{largest_global}")
        print(f"Total Number of Globals Found: {total_globals}")
    else:
        print("No global variables were found.")


    print(f"\nTime taken: {total_time:.2f} seconds")
