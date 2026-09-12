from pathlib import Path


log_directory = Path("logs/ran")
log_directory.mkdir(exist_ok=True,parents=True)

print("Created directory:" ,log_directory)
print("Is directory:" ,log_directory.is_dir)

log_directory.mkdir(exist_ok=True,parents=True)

for entry in sorted(Path("logs").iterdir()):
    print(" ", entry)

