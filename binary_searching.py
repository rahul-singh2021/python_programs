import numpy as np
 
def binarysearch(array,x):

  f=0
  l=len(array)
  while f<=l:
    mid=(f+l)//2

    if x < array[mid]:
      l=mid-1
    elif x >array[mid]:
      f=mid+1
    else:
      return mid    
  return -1

array=np.array([6,3,1,7,2,10,5,37,8])
array=sorted(array)      

x=8

index=binarysearch(array,x)

print("the given number is located at :",index)
