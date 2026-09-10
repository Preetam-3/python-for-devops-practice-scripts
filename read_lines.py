from pathlib import Path

inventory = Path("servers.txt")
inventory.write_text("web-01\nweb-02\ndb-01\ndb-02\ncache-01\n")

server = []
with inventory.open() as f:
    for line in f:
        name = line.strip()
        if name:
            server.append(name)

print("Server found",len(server))

for s in server:
    print(" -",s)


with inventory.open("a") as f:
    f.write("cache-02\n")

print("\nAfter append:")
print(inventory.read_text())

 
