
import json
from pathlib import Path

from src.file_scanner import scan_directory
from src.hash_generator import calculate_sha256


def check_integrity(monitored_directory, baseline_file):
    """Compare current file hashes against the stored baseline."""

    baseline_path = Path(baseline_file)

    with open(baseline_path, "r", encoding="utf-8") as file:
        baseline = json.load(file)

    if not isinstance(baseline, dict):
        raise ValueError("Invalid baseline format: expected a JSON object.")

    current_files = scan_directory(monitored_directory)

    current_hashes = {}
    unreadable = []

    for file_path in current_files:
        try:
            file_hash = calculate_sha256(file_path)

            relative_path = Path(file_path).relative_to(
                Path(monitored_directory)
            )

            current_hashes[str(relative_path)] = file_hash

        except OSError as error:
            unreadable.append(str(file_path))
            print(f"Could not read {file_path}: {error}")

    results = {
        "unchanged": [],
        "modified": [],
        "new": [],
        "deleted": [],
        "unreadable": unreadable
    }

    for file_path, current_hash in current_hashes.items():
        if file_path not in baseline:
            results["new"].append(file_path)

        elif baseline[file_path] == current_hash:
            results["unchanged"].append(file_path)

        else:
            results["modified"].append(file_path)

    unreadable_paths = {
        str(Path(path).relative_to(Path(monitored_directory)))
        for path in unreadable
    }

    for file_path in baseline:
        if (
            file_path not in current_hashes
            and file_path not in unreadable_paths
        ):
            results["deleted"].append(file_path)

    return results
