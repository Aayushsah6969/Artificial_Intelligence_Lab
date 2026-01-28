# Function to calculate area of different shapes
def area_calculator(shape, a, b=0):
    
    if shape == "triangle":
        area = 0.5 * a * b
        return area
    
    elif shape == "square":
        area = a * a
        return area
    
    elif shape == "rectangle":
        area = a * b
        return area
    
    elif shape == "circle":
        area = 3.14 * a * a
        return area


# Examples
print(area_calculator("triangle", 5, 4))     # base=5, height=4
print(area_calculator("square", 4))          # side=4
print(area_calculator("rectangle", 6, 3))    # length=6, width=3
print(area_calculator("circle", 7))          # radius=7
