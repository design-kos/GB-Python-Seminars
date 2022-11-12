# Дана функция f(x) = 18x^3+5x^2 + 10x - 30
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

import sympy

x = sympy.Symbol('x')
f = 5*x**2 + 10*x - 30
roots = sympy.solve(f, x)
print(f"Корни уравнения: {roots}")

print(f"Функция возрастает: {sympy.solve(f > 0, x)}")
print(f"Функция убывает: {sympy.solve(f < 0, x)}")

sympy.plotting.plot(f)

diff = sympy.diff(f, x)
print(f"Вершина функции: {sympy.solve(diff, x)}")

print(f"Y > 0 на промежутках: {sympy.solve(diff > 0, x)}")
print(f"Y < 0 на промежутках: {sympy.solve(diff < 0, x)}")
