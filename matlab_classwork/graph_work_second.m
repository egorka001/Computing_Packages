subplot(2, 1, 1);
hold on;
x = linspace(0, 2*pi, 1000);
y = sin(x)./x;
x_1 = y .* cos(x);
y_1 = y .* sin(x);
plot(x_1, y_1);
plot(0, 0, '-o', 'MarkerSize', 10, 'MarkerFaceColor', 'r', 'MarkerEdgeColor', 'r');
plot(1, 0, '-o', 'MarkerSize', 10, 'MarkerFaceColor', 'r', 'MarkerEdgeColor', 'r');
title('y = sin(x) / x');
xlabel('x');
ylabel('y');
grid on;

subplot(2, 1, 2);
%hold on;
p = 0:0.01:2*pi;
r = sin(p)./ p;
c = polar(p,r);
c.Color = 'r';
c.LineWidth = 2;
%t = polar(0, 0);
%t.Color = 'b';
%t.LineWidth = 4;
title('r = sin(p) / p');
grid on;








