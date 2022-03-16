import subprocess

if (subprocess.run("test -d llvm-project", shell = True).returncode == 1):
	download = subprocess.Popen("git clone --depth=1 https://github.com/llvm/llvm-project.git", shell = True)
	download.wait()

if (subprocess.run("test -d build", shell = True, cwd = 'llvm-project/').returncode == 1):
	subprocess.run(['mkdir', 'build'], cwd = 'llvm-project/')
	cmakeBuild = subprocess.Popen("cmake -DLLVM_ENABLE_PROJECTS=clang -G \"Unix Makefiles\" ../llvm", shell = True, cwd = 'llvm-project/build/')
	cmakeBuild.wait()

subprocess.run(['make', 'clang'], cwd = 'llvm-project/build/')
