format shortG;

n = 10;

m = ones(1, n);

A = - 2 * diag(m);

m = ones(1, n - 1);
B = diag(m, 1);
C = diag(m, -1);

D = A + B + C;

D(1, n) = 1;
D(n, 1) = 1;



