x = linspace(0, 20, 1000);
y = x .* sin(x) - cos(x);

hold on
title("x * sin(x) - cos(x)");
xlabel('x');
ylabel('y');
plot(x, y);


