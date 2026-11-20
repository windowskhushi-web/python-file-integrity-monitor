
from src.baseline_manager import create_baseline

monitored_directory = "monitored_files"
baseline_file = "baseline/baseline.json"

baseline = create_baseline(
    monitored_directory,
    baseline_file
)

print("\nGenerated Baseline:")

for file_path, file_hash in baseline.items():
    print(f"{file_path}: {file_hash}")
