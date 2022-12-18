# By Qichao Wang
# From source: "https://github.com/hofmanpaul/rundirectory.py"
# with modifications

# Software locations

loc_stata_win = "C:/Program Files (x86)/Stata15/StataSE-64.exe"
loc_stata_mac = "/Applications/Stata/StataSE.app/Contents/MacOS/stata-se"
loc_r = "/Library/Frameworks/R.framework/Resources/bin/Rscript"
loc_matlab = "/Applications/MATLAB_R2021b.app/bin/matlab"
loc_python = "python"
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
	with open("{}.log".format(script[0:-3]), 'r') as logfile:
		for line in logfile:
			if err.match(line):
				print(line)
				sys.exit("Stata Error code {line} in {fileloc}".format(line=line[0:-2], fileloc=fileloc))
				lastline = line
				print(lastline)

	os.remove("{}.log".format(script[0:-3]))
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
	subprocess.call([loc_matlab, "-nodisplay", "-batch", script.split('.')[0]])
	os.chdir(dir_origin)

def run_python(fileloc):
	"""Run Python script, then go back to the original directory"""
	fileloc = "/".join([dir_origin, fileloc])
	script, dir_script = parse_location(fileloc)
	os.chdir(dir_script)
	subprocess.call([loc_python, script])  
	os.chdir(dir_origin)

def run_latex(fileloc, num_typeset = 2):
	"""Run Tex script, then go back to the original directory"""
	fileloc = "/".join([dir_origin, fileloc])
	script, dir_script = parse_location(fileloc)
	os.chdir(dir_script)
	subprocess.call([loc_pdflatex, script])
	subprocess.call([loc_bibtex, script[0:-4]])
	for i_num_typeset in range(num_typeset):
		subprocess.call([loc_pdflatex, script])
	os.chdir(dir_origin)
