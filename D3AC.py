import math
def cluster(data,w):
  radii=[]
  for p in data:
    print(p)
    densities=[]
    for k in range(1,(max2D(data)-min2D(data))+1):
      r=k*w
      r1=(k-1)*w
      densities.append(torusDensity(p,r1,r,data))
      print(densities)
      try:
        good_delta_density=(list(reversed(densities))[0]-list(reversed(densities))[1])<0
        if (k <= 2): good_delta_density = True
      except IndexError as e:
        print(e.__repr__())
        good_delta_density=True
      if not good_delta_density:
        break
    radii.append(r1)
  print("[RADII] {} [RADII]".format(str(radii)))
  clusters=[]
  for p1 in data:
    clusters.append([])
    for p2 in data:
      d_l2=l2dist(p1,p2)
      rt=radii[data.index(p1)]
      if d_l2 <= rt:
        clusters[data.index(p1)].append(p2)
    print("FOR POINT {}, NEIGHBOURS ARE AS FOLLOWS: ".format(str(p1)))
    print(clusters[data.index(p1)])
    clusters[data.index(p1)].append(p1)
  for i in range(len(clusters)):
    clusters[i]=sorted(clusters[i])[:]
  print(clusters)
  clusters_dict={ sum(min(i)) : i for i in clusters }
  clusters_good=list(clusters_dict.values())
  return withoutDuplicatesOrEmpty(clusters_good)
def max2D(data):
  c_max=float("-inf")
  for i in data:
    if max(i) > c_max:
      c_max = max(i)
  return c_max
def min2D(data):
  c_min=float("inf")
  for i in data:
    if min(i) < c_min:
      c_min = min(i)
  return c_min
def l2dist(a,b):
  sigma = 0
  for i in range(len(a)):
    sigma += (a[i]-b[i])**2
  return sigma**(1/2)
def withoutDuplicatesOrEmpty(o):
  no_duplicates=[i for n, i in enumerate(o) if i not in o[:n]] 
  final=[]
  for i in no_duplicates:
    if not (i==[]):
      final.append(i)
  return final
def torusDensity(p,low,high,all):
  cnt = 0
  for i in all:
    if (l2dist(p,i) >= low) and (l2dist(p,i) <= high):
      cnt += 1
  a = (math.pi*(high**2))-(math.pi*(low**2))
  return cnt/a