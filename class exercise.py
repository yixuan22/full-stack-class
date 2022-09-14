x=float(input("Please input a number: "))
y=float(input("Please input a number: "))
while y==0:
   print("Please input a nonzero number")
   y=float(input("Please input a number: "))
print(x-y)
print(x+y)
print(x*y)
print(x**y)
print(x/y)

#Ask peer add the third input 
z=float(input("Please input the third number: "))
while z==0:
   print("Please input a nonzero number")
   z=float(input("Please input the third number: "))
print(x-y-z)
print(x+y+z)
print(x*y*z)
print((x**y)**z)
print((x/y)/z)