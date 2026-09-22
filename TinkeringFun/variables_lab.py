force = float(input("Enter a force in newtons: "))
distance = float(input("Enter a distance in meters: "))

work = force * distance
print("work:", work)
print(type(work))

time = 6
power = work / time
print("power:", power)
print(type(power))

# Mandatory change to test 