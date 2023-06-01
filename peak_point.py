import numpy as np

def peakpoint(array):


  f=0
  l=len(array)-1

  while f<=l:
    mid=(f+l)//2

    if array[mid]>array[mid+1]:
      l=mid
    else:
      f=mid

  return -1

array=np.array([15,35,85,96,5,6,8,12])
index=peakpoint(array)

print("the peak point is found at:",index)
