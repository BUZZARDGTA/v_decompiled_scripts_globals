# V Decompiled Scripts Globals

This script automatically extracts global variables from decompiled scripts and saves them to a file.

### Warning

**The script scans exclusively for `Global_x` and `Global_x.f_x` vars.**<br>
The output does not include Global arrays or additional suffixes.<br>
For example, it will not capture formats like `Global_x[x]` or `Global_x[x /*x*/]`.<br>
Only the base `Global_x` part will be extracted from these.

## Usage

Edit the following paths in the source code to match your desired directories:
```py
DECOMPILED_SCRIPTS = Path("D:/Downloads/GTA Stuff/PC/.Other Stuff/03 - Codding/01 - Decompiled Scripts/v-decompiled-scripts-master")
OUTPUT_FILE = Path("extracted_globals.txt")
```

## Screenshots

### <div align="center">Script's Output:</div>
![WindowsTerminal_2024-08-23_22-00](https://github.com/user-attachments/assets/091bc98e-1319-484d-bb6f-5c744f1322e8)

### <div align="center">Extracted Globals File:</div>
![Notepad_2024-08-23_22-18](https://github.com/user-attachments/assets/37d13a13-6556-4d8c-9f1a-f301899a3a12)
