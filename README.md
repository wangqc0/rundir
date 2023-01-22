# Run Directory Automatically for a Research Project

By: Qichao Wang

Last update on: 22 January 2023 (Version 2)

I was illuminated by [Gentzkow and Shapiro](https://web.stanford.edu/~gentzkow/research/CodeAndData.pdf) to adopt the complete automatic process for a research project as an additional step from a manual pipeline from data processing and plotting using Stata, R or Matlab to typesetting the research paper using LaTex. The Python programme is based on [Hofman](https://github.com/hofmanpaul/rundirectory.py)’s work with modifications.

With this small tool, you can run a research project from raw data to the final report for submission within one line of command as follows after directing the terminal to the folder of the project:

```
python3 rundirectory.py
```

I have tested for the most used statistical software and publishing tools in social science research on Mac, including Stata, R (RStudio), Matlab, Python and LaTex (with BibTex incorporated). Any suggestions for adding new useful software are warmly welcomed.

To use the tool on a new project, please copy and paste the two files, `rundirectory.py` and `rundirectory_function.py`, to the folder of your project. Then:

1. Modify the code in the `# Run` block of `rundirectory.py` by replacing the names of the sample code with the names of the scripts in the project. 
2. Modify the code in the `# Software locations` block of `rundirectory_function.py` by replacing the locations of the software on your computer. I have added comments as follows to instruct how to find the locations:
	* Stata (`loc_stata_win` or `loc_stata_mac`):
		* Mac: Open "Finder", go to "Applications", click the folder of the installed Stata, show the package contents of the file with the Stata icon, go to the folder "Contents/MacOS". The file to use is the one with lowercase letters and a hyphen.
		* Windows: Go to the folder of the installed Stata, then find the ".exe" file. This is the file to use.
	* R (`loc_r`): Open RStudio, type `R.home('bin')`. Use the returned folder as the location.
	* Matlab (`loc_matlab`):
		* Mac: Open "Finder", go to "Applications", show the package contents of the installed Matlab, click the folder "bin", then find the "matlab" file.
		* Windows: Go to the folder of the installed Matlab, then find the ".exe" file.
	* Python (`loc_python`):
		* Mac: Usually, just entering `python3` works. Otherwise, try `which python3` in the terminal to find the location, and use the returned folder as the location.
		* Windows: Go to the folder where your Python is installed. Use the folder as the location.
	* LaTeX (`loc_pdflatex` and 	`loc_bibtex`):
		* Mac: For pdflatex, try `which pdflatex` in the terminal to find the location, and use the returned file as the location. For bibtex (used for bibliography), try `which biber` in the terminal to find the location, and use the returned file as the location.
		* Windows: Go to the folder of the installed Tex distribution, then find the corresponding files for "pdflatex" and "biber".
3. Run the command above and wait for the job to be done.

I have also pushed the self-contained [handbook](sample_latex.pdf) to the repository. It shows the generated plots from the scripts of the statistical software in the report.
