import json
from pathlib import Path

config_path = Path("deploy.json")

with config_path.open() as f:
    config = json.load(f)

print("Before changes")

print(f'Enviroment: {config["environments"]["prod"]["replicas"]}')

config['version'] = '1.5.0'
config['environment']['prod']['replicas'] = 8


with config_path.open('w') as f:
    json.dump(config,f, indent=3, sort_keys=True)
    f.write('\n')

with config_path.open() as f:
    updated = json.load(f)



print("After changes")


print(f' Envriroment: {config["environments"]["prod"]["replicas"]}')

