from math import sqrt
from cmath import sqrt as c_sqrt

def get_sqrt(n: float) -> float | complex:
  return sqrt(n) if n >= 0 else c_sqrt(n)
