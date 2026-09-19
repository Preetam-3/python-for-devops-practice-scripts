import os
import time
from pathlib import Path

logs_dir = Path('logs')

files = [
    ('app-today.log',     0),
    ('app-yesterday.log', 1),
    ('app-2days.log',     2),
    ('app-8days.log',     8),
    ('app-10days.log',   10),
    ('app-15days.log',   15),
]

now = time.time()

for name, days_old in files:
    path = logs_dir/name
    path.write_text("Log content for {name}. Generated for lesson 204. \n " * 5)
    mtime = now - days_old * 86400
    os.utime(path, (mtime, mtime))
    print(f'Created {path} ({days_old} days_old)')

print(f'\n{len(files)} log files ready in {logs_dir}/')

