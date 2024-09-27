import sys

from z3city import solver

hourly_prices = [1.0] * 24

result = solver.solve(hourly_prices, 8, 3)
print(result)
