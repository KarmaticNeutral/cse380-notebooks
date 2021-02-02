from math import gcd

def nCk(n, k):
  if k < 0 or k > n:
    return 0
  else:
    result = 1
    d = 1
    g = 1
    m = min(k, n - k)
    while (d <= m):
      g = gcd(result, d)
      result = n * (result // g)
      result = (result // (d // g))
      n -= 1
      d += 1
    return result
