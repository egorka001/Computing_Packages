x = linspace(0, 2, 1000);

y = humps(x);

hold on
title("humps");
xlabel('x');
ylabel('y');
plot(x ,y);

[ y_m, idx ] = max(y);
x_m = x(idx);

plot(x_m, y_m, '-o', 'MarkerFaceColor', 'r', 'MarkerEdgeColor', 'r');

[ y_r, y_r_idx ] = find(y > 20 & y < 40);

plot(x(y_r_idx), y(y_r_idx), 'o');

