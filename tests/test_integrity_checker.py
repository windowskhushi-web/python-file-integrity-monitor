
from src.integrity_checker import check_integrity

results = check_integrity(
    "monitored_files",
    "baseline/baseline.json"
)

print("\nINTEGRITY CHECK RESULTS")

for category, files in results.items():
    print(f"\n{category.upper()}:")

    if files:
        for file_path in files:
            print(f"  - {file_path}")
    else:
        print("  None")
