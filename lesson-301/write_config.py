import json
from pathlib import Path


deploy_result = {
    'deploy_id': 'd-20260520-002',
    'env': 'staging',
    'app': 'devops-app',
    'version': '1.3.0',
    'success': True,
    'duration_seconds': 42,
    'errors': [],
    'warnings': ['cert expires in 14 days'],
}


output_path = Path('deploy_result.json')


with output_path.open('w') as f:
    json.dump(deploy_result,f, indent=3, sort_keys=True)
    f.write

print(f"Wrote {output_path.stat().st_size} byte to {output_path}()")
print()
print(output_path.read_text())
