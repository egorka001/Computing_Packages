fun = @(x) x .* sin(x) - cos(x);

x = linspace(0, 20, 1000);
y = x .* sin(x) - cos(x);

hold on
grid on
title("x * sin(x) - cos(x)");
xlabel('x');
ylabel('y');
plot(x, zeros(1000), '--', 'linewidth', 2);
plot(x, y);

z = ginput(2);
[zr, zf] = fzero(fun, [z(1,1), z(2,1)]);
plot(zr, zf, 'r*', z(1,1), fun(z(1,1)), 'g*', z(2,1), fun(z(2,1)), 'g*');


