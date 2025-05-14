print("*****AREA CLACULATOR*****")
print("""press 1 to get the area of square.  
press 2 to get the area of the rectangle
press 3 to get the area of the circle
press 4 to get the area of the triangle""")

choise = int(input("enter the number between 1-4: "))

if choise == 1:
    side = float(input("enter the length of the side: "))
    area = side**2
    print("the area of the square",area)
elif choise == 2:
    length = float(input("enter the length of the side of the rectangle: "))
    breadth = float(input("enter the breadth of the rectangle: "))
    area = length * breadth
    print("the area of the rectangle is: ",area)
elif choise == 3:
    radius = float(input("enter the radius of the circle: "))
    area = (22/7)*radius**2
    print("the area of the circle is: ",area)
elif choise == 4:
    base = float(input("enter the base of the triangle: "))
    height = float(input("enter the height of the triangle: "))
    area = (1/2)*base*height
    print("the area of the triangle is: ",area)
else:
    print("invalid input")
