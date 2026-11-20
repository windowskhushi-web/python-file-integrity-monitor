
import json
from pathlib import Path

from src.file_scanner import scan_directory
from src.hash_generator import calculate_sha256


def create_baseline(monitored_directory, baseline_file):
    """
    Generate and save SHA-256 hashes for monitored files.

    Args:
        monitored_directory: Directory containing files to monitor.
        baseline_file: Destination JSON file for the baseline.

    Returns:
        Dictionary containing file paths and their SHA-256 hashes.
    """

    files = scan_directory(monitored_directory)
    baseline = {}

    for file_path in files:
        try:
            file_hash = calculate_sha256(file_path)

            relative_path = Path(file_path).relative_to(
                Path(monitored_directory)
            )

            baseline[str(relative_path)] = file_hash

        except OSError as error:
            print(f"Could not read {file_path}: {error}")

    baseline_path = Path(baseline_file)
    baseline_path.parent.mkdir(parents=True, exist_ok=True)

    with open(baseline_path, "w", encoding="utf-8") as file:
        json.dump(baseline, file, indent=4)

    print(f"Baseline created successfully: {baseline_path}")
    print(f"Total files recorded: {len(baseline)}")

    return baseline
