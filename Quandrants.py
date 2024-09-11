x = float(input("Please enter an X value: "))
y = float(input("Please enter an Y value: "))
if x > 0 and y > 0
    print("This cordinate is in Quadrant 1.")
elif x < 0 and y > 0:
    print("This cordinate is in Quadrant 2.")
elif x < 0 and y < 0:
    print("This cordinate is in Quadrant 3.")
elif x > 0 and y < 0:
    print("This cordinate is in Quadrant 4.")
else:
    print("This cordinate is in multiple quadrants.")
