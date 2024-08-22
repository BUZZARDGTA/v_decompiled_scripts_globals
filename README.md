# extract_all_globals_from_v_decompiled_scripts 

This script automatically extracts global variables from decompiled scripts and saves them to a file.

### Warning

**The script scans exclusively for `Global_x` strings.**<br>
It will not include additional suffixes or formats in the output, such as:
- `Global_x.f_x`
- `Global_x[x /*x*/]`

Only the `Global_x` part will be extracted.

## Usage

Edit the following paths in the source code to match your desired directories:
```py
DECOMPILED_SCRIPTS = Path("D:/Downloads/GTA Stuff/PC/.Other Stuff/03 - Codding/01 - Decompiled Scripts/v-decompiled-scripts-master")
OUTPUT_FILE = Path("extracted_globals.txt")
```

## Screenshot

![WindowsTerminal_2024-08-22_19-01](https://github.com/user-attachments/assets/a0970126-f95a-46f0-8773-5fba40d2dd65)
