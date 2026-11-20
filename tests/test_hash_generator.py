from src.hash_generator import calculate_sha256

file_path = "monitored_files/configs/sample.txt"

result = calculate_sha256(file_path)

print("SHA-256 Hash:")
print(result)