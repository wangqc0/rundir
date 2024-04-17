# By Qichao Wang
# From source: "https://github.com/hofmanpaul/rundirectory.py"
# with modifications

# Setup

import os
import subprocess
import sys
import re
dir_origin = os.getcwd()

exec(open("rundirectory_function.py").read())

print("""
	Wait for the message 'DONE' to show up.
	The files are running in the background.
	""")

# Run

run_stata("sample_stata.do")
run_r("sample_r.r")
run_matlab("sample_matlab.m")
run_python("sample_python.py")
run_cpp("sample_cpp.cpp")
run_latex("sample_latex.tex", num_typeset = 1)

print("DONE")
