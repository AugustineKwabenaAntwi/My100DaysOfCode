import functions as f

print("1.Triangle 2.Rectangle 3.Circle 4.Square")

choice = int(input("Enter your choice: "))

if choice == 1:
  base  = int(input("Enter base: "))
  height = int(input("Enter height: "))
  area = f.cal_triangle_area
  print("The area of the triangle is: ",area(base,height))

elif choice == 2:
  width = int(input("Enter the width:   "))
  length = int(input("Enter the length:   "))
  area = f.cal_rectangle_area
  print("The area of the rectangle is: ",area(width,length))
elif choice == 3:
  radius = int(input("Enter the radius:   "))
  area = f.cal_circle_area
  print("The area of the circle is: ",area(radius))

elif choice == 4:
  side = int(input("Enter the side:   "))
  area = f.cal_square_area
  print("The area of the square is: ",area(side))

else: print("Input is invalid")