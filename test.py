import subprocess

p1 = subprocess.run('dir', capture_output=True, shell=True, text=True)
print(p1.stdout)
