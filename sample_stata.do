* This is a sample file.

cd "/Users/WilliamWang/Library/Mobile Documents/com~apple~CloudDocs/Documents/py/rundir"

use "co3.dta", clear

twoway dot y s
graph export "sample_stata_graph.eps", replace
