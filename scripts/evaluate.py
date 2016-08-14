from whitespace_cleaner import *
import sys, os, filecmp, subprocess

if len(sys.argv) < 3:
	print("Invalid usage!")
	print("python", sys.argv[0], "problem_name team_num")
	print("Example:")
	print("python", sys.argv[0], "sum 1")
	sys.exit(0)

fnamestem = sys.argv[1] + "_" + sys.argv[2]
sourcestem = "../sources/" + fnamestem
binary = "../binary/" + fnamestem
outexp = "../problems/" + sys.argv[1] + "_sn.txt"
problem = "../problems/" + sys.argv[1] + "_qn.txt"
sourcefile = ""
ext = ""
exts = {".cpp", ".py", ".java"}
output = ""
ansf = open(outexp, "rb")
ans = ansf.read()
prob = open(problem, "rb")
probstr = prob.read()

for i in exts:
	if os.path.isfile(sourcestem + i):
		sourcefile = sourcestem + i
		ext = i
if sourcefile == "":
	print("Only .py, .cpp and .java are supported.")
	sys.exit(0)

if ext == ".cpp":
	subprocess.run(["g++",sourcefile,"-o",binary])
	if os.path.isfile(binary):
		print("Compilation Success.")
		p = subprocess.Popen([binary], stdout=subprocess.PIPE, stdin=subprocess.PIPE,stderr=subprocess.PIPE)
		output = p.communicate(input=probstr)[0]
	else:
		print("Compilation Fail.")
elif ext == ".py":
	output = subprocess.check_output(["python",sourcefile,"<", problem])

elif ext == ".java":
	subprocess.run(["javac",sourcefile,"-d", "../binary"]);
	binary += ".class"
	if os.path.isfile(binary):
		print("Compilation Success.")
		p = subprocess.Popen(["java",binary], stdout=subprocess.PIPE, stdin=subprocess.PIPE,stderr=subprocess.PIPE)
		output = p.communicate(input=probstr)[0]


	else:
		print("Compilation Fail.")

output = clean(output)

if ans == output:
	print("Solution Accepted.")
else:
	print("Solution Incorrect.")
	print("expected")
	print(ans)
	print("got")
	print(output)
