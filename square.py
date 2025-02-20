from math import sqrt
from cmath import csqrt

def get_sqrt(n: float) -> float | complex:
  return sqrt(n) if n >= 0 else csqrt(n)
