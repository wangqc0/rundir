% This is a sample file.

rng(0, 'twister')
x = randn(100, 2);

plot(x(:, 1), x(:, 2), '.')
saveas(gcf, 'sample_matlab_graph.png');
close;