def greet():
    print("hello, welcome to python")


def greeting(user):
    print(f"Hello, {user} welcome to python")
# greet()
# greet()
# greet()
# greeting("Jean")
# greeting("Mark")

def area_circle(radius, precision: int=2):
    a = 22/7 * radius * radius
    result = round(a, precision)
    print(result)

# area_circle(10, 2)
# area_circle(5)

def volume_cylinder(r, h):
    volume = 22/7 * r * r * h
    return volume
print(volume_cylinder(2,5))

volume_cylinder(2,5)