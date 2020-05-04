import D3AC as D3AC, functools as ft
def cluster(data, n):
  currw = 0
  while currw < (D3AC.max2D(data) - D3AC.min2D(data)):
    currw += min([ min(map(abs, i)) for i in data])
    res = D3AC.cluster(data, currw)
    if len(res) == n:
      break
  return res