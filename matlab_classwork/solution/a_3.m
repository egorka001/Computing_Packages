x = linspace(0, 2, 1000);

y = humps(x);

hold on
plot(x ,y);

[ y_m, idx ] = max(y);
x_m = x(idx);

plot(x_m, y_m, '-o', 'MarkerFaceColor', 'r', 'MarkerEdgeColor', 'r');

for i = 1:1000
    if y(i) > 20 & y(i) < 40
        plot(x(i), y(i), '-o', 'MarkerFaceColor', 'g', 'MarkerEdgeColor', 'g');
    end
end

%ylim([20, 40]);