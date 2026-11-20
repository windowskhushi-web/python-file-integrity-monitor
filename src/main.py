
import argparse
from pathlib import Path

from src.baseline_manager import create_baseline
from src.integrity_checker import check_integrity


MONITORED_DIRECTORY = "monitored_files"
BASELINE_FILE = "baseline/baseline.json"


def display_report(results):
    print("\n========== FILE INTEGRITY REPORT ==========")

    categories = {
        "unchanged": "UNCHANGED",
        "modified": "MODIFIED",
        "new": "NEW FILES",
        "deleted": "DELETED",
        "unreadable": "UNREADABLE"
    }

    for key, title in categories.items():
        files = results[key]

        print(f"\n{title}: {len(files)}")

        if files:
            for file_path in files:
                print(f"  - {file_path}")
        else:
            print("  None")

    print("\n===========================================")


def main():
    parser = argparse.ArgumentParser(
        description="Python File Integrity Monitoring Tool"
    )

    parser.add_argument(
        "command",
        choices=["baseline", "check"],
        help="Create a baseline or check file integrity"
    )

    args = parser.parse_args()

    try:
        monitored_path = Path(MONITORED_DIRECTORY)
        baseline_path = Path(BASELINE_FILE)

        if not monitored_path.exists():
            raise FileNotFoundError(
                f"Monitored directory not found: {monitored_path}"
            )

        if not monitored_path.is_dir():
            raise NotADirectoryError(
                f"Not a directory: {monitored_path}"
            )

        if args.command == "baseline":
            create_baseline(
                MONITORED_DIRECTORY,
                BASELINE_FILE
            )

        elif args.command == "check":
            if not baseline_path.exists():
                raise FileNotFoundError(
                    f"Baseline not found: {baseline_path}. "
                    "Create one using the baseline command."
                )

            results = check_integrity(
                MONITORED_DIRECTORY,
                BASELINE_FILE
            )

            display_report(results)

    except (OSError, ValueError) as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
