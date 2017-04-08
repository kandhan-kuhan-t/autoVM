import subprocess

out = subprocess.run(["ls"],stdout=subprocess.PIPE)

print(out.stdout.decode('utf-8'))