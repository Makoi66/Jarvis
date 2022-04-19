x,y=map(int,input().strip())

if (y>2-x and y<x**2) or (y>x**2 and y<2-x and y<4-x**2 and x<0) or (y>4-x**2 and y>x**2 and x>0) or (y<2-x and y<x**2 and y>0):
    print("+")
else:
    print("-")