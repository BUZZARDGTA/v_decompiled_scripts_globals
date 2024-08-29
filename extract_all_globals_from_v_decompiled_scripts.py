import re
from pathlib import Path
import time


DECOMPILED_SCRIPTS = Path("D:/Git/v-decompiled-scripts")
OUTPUT_FILE = Path("extracted_globals.txt")

RE_GLOBAL_INT_PATTERN = re.compile(r"\bGlobal_(\d+)\b")
RE_GLOBALS_PATTERN = re.compile(r"\bGlobal_\d+(?:\.f_\d+)*\b")


def get_max_filename_length(directory: Path):
    max_length = 0
    for file_path in directory.rglob('*.c'):
        max_length = max(max_length, len(file_path.name))
    return max_length

def process_files(directory: Path, output_file: Path, max_filename_length: int):
    def extract_globals(file_content: str) -> list[str]:
        matches = RE_GLOBALS_PATTERN.findall(file_content)

        for match in matches:
            if not isinstance(match, str):
                raise TypeError(f"Expected string, got {type(match).__name__}: {match}")

        return matches

    def get_new_globals(globals_in_file: list[str], global_ints: set, global_vars: set):
        new_global_vars = set(globals_in_file) - global_vars
        num_new_global_vars = len(new_global_vars)
        return new_global_vars, num_new_global_vars

    def get_global_int(global_var: str):
        match = RE_GLOBAL_INT_PATTERN.search(global_var)
        if match:
            global_int = int(match.group(1))
            return global_int
        return None

    global_ints = set()
    global_vars = set()

    with output_file.open('w', encoding='utf-8') as out_file:
        for file_path in directory.rglob('*.c'):
            file_name = file_path.name
            print(f'Processing: "{file_name}"', end="")

            content = file_path.read_text(encoding='utf-8')
            globals_in_file = extract_globals(content)

            new_global_vars, num_new_global_vars = get_new_globals(globals_in_file, global_ints, global_vars)

            num_new_global_ints = 0  # Initialize the counter for new global integers
            for global_var in new_global_vars:
                global_vars.add(global_var)
                out_file.write(f"{global_var}\n")
                out_file.flush() # Ensure it is written to disk immediately

                global_int = get_global_int(global_var)
                if global_int not in global_ints:
                    global_ints.add(global_int)
                    num_new_global_ints += 1  # Increment the counter for new global integers

            #print(f"{' ' * (max_filename_length - len(file_name))} .. Found {num_new_global_vars} new Global var(s) and {num_new_global_ints} new Global int(s) from this file.")
            print(f"{' ' * (max_filename_length - len(file_name))} .. {num_new_global_vars} new Global var(s), {num_new_global_ints} new int(s).")

    return global_ints, global_vars

if __name__ == "__main__":
    start_time = time.time()

    max_filename_length = get_max_filename_length(DECOMPILED_SCRIPTS)
    global_ints, global_vars = process_files(DECOMPILED_SCRIPTS, OUTPUT_FILE, max_filename_length)

    if global_ints:
        smallest_global_int = min(global_ints)
        largest_global_int = max(global_ints)
        total_globals_int = len(global_ints)
        total_globals = len(global_vars)
    else:
        smallest_global_int = None
        largest_global_int = None
        total_globals_int = 0
        total_globals = 0

    end_time = time.time()

    total_time = end_time - start_time

    print()
    if global_ints:
        print(f"Smallest Global Int: Global_{smallest_global_int}")
        print(f"Largest  Global Int: Global_{largest_global_int}")
        print(f"Total Number of Globals Int  Found: {total_globals_int}")
        print(f"Total Number of Globals Vars Found: {total_globals}")
    else:
        print("No Global variables were found.")


    print(f"\nTime taken: {total_time:.2f} seconds")
