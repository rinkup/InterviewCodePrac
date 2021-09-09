import math
def t_cap(totalC, loc, cap) :
  out = {}
  ret = []
  for ind, val in enumerate(loc):
      x = val[0] #1
      y = val[1] #-1 
      diff = math.sqrt(x*x+y*y) # 1.4
      out[ind] = diff
    #   out.sort() # { 0:2.236, 2:1.4, 1:5}

  for i in range(0, cap):
      ret.append(loc[out.index(i)])
    
  return ret


totalCrates = 3
allLocations = [[1, 2], [3, 4], [1, -1]]
truckCapacity = 2
print(t_cap(totalCrates, allLocations, truckCapacity))