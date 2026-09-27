a =10 

print(a*a)


a =20 

print(a*a)


a =30 

print(a*a)


def Square(a):
    return a*a


print(Square(10))
print(Square(20))
print(Square(30))


def Rectangle(l, b):
      return l*b

print(Rectangle(10,20))

print(Rectangle(100,20))
print(Rectangle(0,20))


def Area(n):
    if n%2==0 :
        return "even"
    else:
        return "odd"

print(Area(7))
print(Area(70))
print(Area(0))
print(Area(12))