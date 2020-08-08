def gcd(x,y): 
    if (y==0):
      return x
    else:
      r=x%y
      return gcd(y,r)  
a=int(input("Enter a : "))
b=int(input("Enter b : "))
print(gcd(a,b))