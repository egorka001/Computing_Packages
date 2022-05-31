x = linspace(-5, 5, 10000);
y_1 = sin(x);
y_2 = sin(2 * x);
y_3 = sin(3 * x);
y_4 = sin(4 * x);

subplot(2, 3, 1);
plot(x, y_1, 'r');
title('y = sin(x)');
xlabel('x');
ylabel('y');
grid on;

subplot(2, 3, 2);
plot(x, y_2, 'g');
title('y = sin(2x)');
xlabel('x');
ylabel('y');
grid on;

subplot(2, 3, 3);
plot(x, y_3, 'b');
title('y = sin(3x)');
xlabel('x');
ylabel('y');
grid on;

subplot(2, 3, 4);
plot(x, y_4, 'y');
title('y = sin(4x)');
xlabel('x');
ylabel('y');
grid on;

subplot(2, 3, [5 6]);
hold on;
plot(x, y_1, 'r');
plot(x, y_2, 'g');
plot(x, y_3, 'b');
plot(x, y_4, 'y');
title('friends!');
xlabel('time');
ylabel('fun');
grid on;