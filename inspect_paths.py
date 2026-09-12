from pathlib import Path

here = Path(".")

print("relative: ", here)
print("absolute: ", here.resolve())
print("home dir: ", here.is_dir())


config = Path("deploy.txt")

print("is_file?; ", config.is_file())
print("is_dir?: ", config.is_dir())
print("is_exits?:", config.exists())
print("inspect:", config.stat().st_size)






