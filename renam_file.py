from pathlib import Path

old = Path("workspace/rollback.sh")
new = Path("workspace/rollback-1.sh")

if old.exists():
    old.rename(new)
    print("Renamed:", old.name, "->", new.name)

else:
    print("Source not found", old)

print("old exists: ", old.exists())
print("new exists: ", new.exists())

target = Path("workspace/config.json")

if target.exists():
    target.unlink()
    print("Deleted:", target.name)

print("\nworksace/ contents after rename and delete:")
for entry in sorted(Path("workspace").iterdir()):
    print(" ",entry.name)



