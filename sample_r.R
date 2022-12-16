# This is a sample file.

setwd('/Users/WilliamWang/Library/Mobile Documents/com~apple~CloudDocs/Documents/py/rundir')

set.seed(0)
x <- rnorm(100, mean = 100, sd = 15)
y <- rnorm(100, mean = 100, sd = 15)

png(filename = 'sample_r_graph.png')
plot(x, y)
dev.off()
