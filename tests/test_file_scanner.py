from src.file_scanner import scan_directory

directory = "monitored_files"

files = scan_directory(directory)

print("Files discovered:")

for file in files:
    print(file)

print(f"\nTotal files found: {len(files)}")