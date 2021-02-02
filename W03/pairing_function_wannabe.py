tri = lambda x: x * (x + 1) // 2
c2 = lambda x,y: tri(x) + (0 if y < x else tri(y+2) - tri(x+1))
c2alt = lambda x,y: sum(range(1,x+1)) + sum(range(x+2,y+2+1))

def build_table(use_alt, show_all):
  pfw = c2alt if use_alt else c2
  pairings = []
  for x in range(1,10):
    paired = []
    for y in range(1,10):
      if show_all or y >= x:
        paired.append(pfw(x, y))
      else:
        paired.append('-')
    pairings.append(paired)
  return pairings

return build_table(True, False)
