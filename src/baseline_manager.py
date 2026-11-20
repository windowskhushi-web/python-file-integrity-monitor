
import json
from pathlib import Path

from src.file_scanner import scan_directory
from src.hash_generator import calculate_sha256


def create_baseline(monitored_directory, baseline_file):
    """Generate and save SHA-256 hashes for monitored files."""

    files = scan_directory(monitored_directory)
    baseline = {}
    errors = []

    for file_path in files:
        try:
            file_hash = calculate_sha256(file_path)

            relative_path = Path(file_path).relative_to(
                Path(monitored_directory)
            )

            baseline[str(relative_path)] = file_hash

        except OSError as error:
            errors.append(str(file_path))
            print(f"Could not read {file_path}: {error}")

    if errors:
        raise OSError(
            f"Baseline creation incomplete. "
            f"{len(errors)} file(s) could not be read. "
            "Existing baseline was not overwritten."
        )

    baseline_path = Path(baseline_file)
    baseline_path.parent.mkdir(parents=True, exist_ok=True)

    with open(baseline_path, "w", encoding="utf-8") as file:
        json.dump(baseline, file, indent=4)

    print(f"Baseline created successfully: {baseline_path}")
    print(f"Total files recorded: {len(baseline)}")

    return baseline
