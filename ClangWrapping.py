import subprocess
import sys

command = "clang "
n = len(sys.argv)
for i in range(1, n):
	command = command + sys.argv[i] + " "
subprocess.run(command, shell = True)
