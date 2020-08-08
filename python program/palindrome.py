def first(string):
  f=list(string)
  return f[0]
def last(string):
  l=list(string)
  return l[-1]
def middle(string):
  m=list(string)
  return m[1:-1]   
  
print(first('himani'))
print(last('himani'))
print(middle('himani'))
print(middle('hi'))
print(middle('h'))
print(middle(''))

# if we call middle with a string with two letters, one letter and no letters it will print an empty list.
def _palindrome(string):
  if first(string) == last(string) and middle(string) == middle(string)[::-1]:
    return True
  else:
    return False
s= input("Enter a string : ")     
print(_palindrome(s))    