# By Qichao Wang
# From source: "https://github.com/hofmanpaul/rundirectory.py"
# with modifications

# Software locations

loc_stata_win = "C:/Program Files (x86)/Stata18/StataMP-64.exe"
loc_stata_mac = "/Applications/Stata/StataMP.app/Contents/MacOS/stata-mp"
loc_r = "/Library/Frameworks/R.framework/Resources/bin/Rscript"
loc_matlab = "/Applications/MATLAB_R2024a.app/bin/matlab"
loc_python = "python3"
loc_pdflatex = "/Library/TeX/texbin/pdflatex"
loc_bibtex = "/Library/TeX/texbin/biber"

# Functions

def parse_location(fileloc):
	filepath = fileloc.split("/")
	script = filepath[-1]
	dir_script = "/".join(filepath[0:-1])
	return script, dir_script

def run_stata(fileloc):
	"""Run Stata do-file in batch mode, delete the log file, then go back to the original directory"""
	fileloc = "/".join([dir_origin, fileloc])
	script, dir_script = parse_location(fileloc)
	os.chdir(dir_script)

	if sys.platform == "win32":
		subprocess.call([loc_stata_win, "-e", "do", script])
	else:
		subprocess.call([loc_stata_mac, "-b", "do", script])
	
	err = re.compile("^r\([0-9]+\);$")
	with open("{}.log".format(re.sub("(.*)\\.(.*)$", "\\1", script)), 'r') as logfile:
		for line in logfile:
			if err.match(line):
				print(line)
				sys.exit("Stata Error code {line} in {fileloc}".format(line = line[0:-2], fileloc = fileloc))
				lastline = line
				print(lastline)

	os.remove("{}.log".format(re.sub("(.*)\\.(.*)$", "\\1", script)))
	os.chdir(dir_origin)

def run_r(fileloc):
	"""Run R script, then go back to the original directory"""
	fileloc = "/".join([dir_origin, fileloc])
	script, dir_script = parse_location(fileloc)
	os.chdir(dir_script)
	subprocess.call([loc_r, "--vanilla", script])
	os.chdir(dir_origin)

def run_matlab(fileloc):
	"""Run Matlab script, then go back to the original directory"""
	fileloc = "/".join([dir_origin, fileloc])
	script, dir_script = parse_location(fileloc)
	os.chdir(dir_script)
	subprocess.call([loc_matlab, "-nodisplay", "-batch", script.split(".")[0]])
	os.chdir(dir_origin)

def run_python(fileloc):
	"""Run Python script, then go back to the original directory"""
	fileloc = "/".join([dir_origin, fileloc])
	script, dir_script = parse_location(fileloc)
	os.chdir(dir_script)
	subprocess.call([loc_python, script])  
	os.chdir(dir_origin)

def run_cpp(fileloc):
	"""Run C++ script, then go back to the original directory"""
	fileloc = "/".join([dir_origin, fileloc])
	script, dir_script = parse_location(fileloc)
	os.chdir(dir_script)
	os.system("g++ " + script + " -o " + re.sub("(.*)\\.(.*)$", "\\1", script))
	os.system("./" + re.sub("(.*)\\.(.*)$", "\\1", script))
	os.chdir(dir_origin)

def run_latex(fileloc, distribution = "pdflatex", num_typeset = 2, shell_escape = False):
	"""Run Tex script, then go back to the original directory"""
	# shell_escape: Enable when external tools are needed for compiling.
	if distribution == "pdflatex":
		loc_latex = loc_pdflatex
	else:
		loc_latex = "/Library/TeX/texbin/" + distribution
	fileloc = "/".join([dir_origin, fileloc])
	script, dir_script = parse_location(fileloc)
	os.chdir(dir_script)
	if shell_escape:
		subprocess_call_tex = [loc_latex, "-shell-escape", script]
	else:
		subprocess_call_tex = [loc_latex, script]
	subprocess.call(subprocess_call_tex)
	subprocess.call([loc_bibtex, re.sub("(.*)\\.(.*)$", "\\1", script)])
	for i_num_typeset in range(num_typeset):
		subprocess.call(subprocess_call_tex)
	os.chdir(dir_origin)
