class Robot:
    default_name = "Unnamed"


r1 = Robot()
r2 = Robot()
r3 = Robot()

print("Before changing anything:")
print(r1.default_name)
print(r2.default_name)
print(r3.default_name)

r2.default_name = "Wall-E"

print("\nAfter overriding r2:")
print(r1.default_name)
print(r2.default_name)
print(r3.default_name)

Robot.default_name = "Android"

print("\nAfter changing the class attribute:")
print(r1.default_name)
print(r2.default_name)
print(r3.default_name)