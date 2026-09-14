import os 

try:
    val = os.environ['HOME']
    print(val)
except KeyError as e:
    print("KeyError: ", e)


app_env = os.environ.get('ASP_VERSION', '0.0.0.0')
print(app_env)


""" os.environ['KEY'] raises KeyError if the variable is absent — appropriate when the variable is mandatory and a missing value is a bug. os.environ.get('KEY', default) and os.getenv('KEY', default) are identical; both return the default (or None if no default is given) when the variable is missing.

In DevOps scripts, prefer os.getenv('KEY', 'fallback') for optional config and os.environ['KEY'] inside a try/except (or with an explicit if 'KEY' not in os.environ: sys.exit(1) guard) for required variables.

The second run prefixes the variable assignments on the same shell line — a POSIX pattern for temporarily overriding env vars without exporting them."""

