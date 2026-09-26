import json
from pathlib import Path


config_file = Path("deploy.json")

with config_file.open() as f:
    config = json.load(f)

print(f"App: {config['app_name']}")
print(f"Enviroment-dev-object: {config['environments'].keys()}")
dev = config['environments']['dev']

print(f"Dev-host: {dev['host']}")
print(f"Dev-port: {dev['port']}")
print(f"Dev-debug: {dev['debug']}")
