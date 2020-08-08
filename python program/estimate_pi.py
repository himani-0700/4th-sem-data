import math
def estimate_pi():
  sum=1
  tsum=0
  k=0
  while sum > 1e-15:
   sum = (math.factorial(4*k) * (1103+26390*k)) / ((math.factorial(k)**4) * 396**(4*k))
   tsum=tsum+sum
   k=k+1
  return (1/((2*2**(1/2)/9801)*tsum))
  
  
print(estimate_pi())  
print(math.pi)
if math.pi==estimate_pi():
  print("True")
else:
  print("False")  

