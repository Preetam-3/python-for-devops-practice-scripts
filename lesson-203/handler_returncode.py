import subprocess
import sys

def run_command(cmd: list[str]) -> str:
    result = subprocess.run(cmd, capture_output=True,text=True)
    if result.returncode != 0:
        print(f"Error: command failed with the exit code {result.returncode}", file=sys.stderr)
        print(f" command: {' '.join(cmd)}", file=sys.stderr)
        if result.stderr:
            print(f"   stderr: ,{result.stderr.strip()}", file=sys.stderr)
        sys.exit(result.returncode)
    
    return result.stdout.strip()

os_name = run_command(['uname', '-s'])
print("Os name:", os_name)

host = run_command(['hostname'])
print("Hostname:", host)


non_existence = '/this/path/doesnt/exits/xyz'
print(f"\n Attemting: ls {non_existence}")
bad_result = subprocess.run(['ls', non_existence], capture_output=True,text=True)
if bad_result.returncode != 0:
    print(f"  returncode: {bad_result.returncode}")
    print(f"  stderr:     {bad_result.stderr}")
    print(f"  (handled gracefully - no sys.exit here)")

run_command(['ls','-l', '/this/path/not/exits'])

