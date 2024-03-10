import math

def circle_calc(radius):
    area = math.pi*(radius**2)
    circum=2*math.pi*radius 
    diameter = 2*radius
    return area,circum,diameter

if __name__ == "__main__":
    radius = int(input("Enter the radius of the circle\n\n").strip())
    round(radius,3)

    #accessing local variables outside their scope
    area,circum,diameter = circle_calc(radius)
    print(f'Diameter: {round(diameter,3)}\nArea: {round(area,3)}\nCircumference: {round(circum,3)}\n')