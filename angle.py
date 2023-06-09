from math import atan, pi
def solve(ab, bc):
   def deg(rad):
      return 180/pi * rad

   ans = deg(atan(ab/bc))
   return ans

ab = 6
bc = 4
print(solve(ab, bc))
