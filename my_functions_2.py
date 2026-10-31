def add(x,y,z):
    return x + y + z

# result = add(1,2,3)
# print(result)

def addition(*nums):
    # total = sum(nums)
    total = 0
    for num in nums:
        total += num
    return total

def save(**data):
    with open("values.txt", "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

def some_function(name, *scores, **details):
    pass

def cylinder(r,h):
    """
    Calculate the volume and Surface area of a cylinder
    parameters:
    radius and height of th cylinder
    returns: volume and surface area of cylinder
    :param r:
    :param h:
    :return:
    """

    v= 22/7 * r * r * h
    sa= 22/7 * r **2 *2 + 22/7 * r * 2 *h
    return sa, v

surface_area, volume = cylinder(2,5)
print(surface_area,volume)

# lambda functions
divider = lambda x,y: x/y

area_circle = lambda r: 22/7 * r * r

print(divider(25,5))


# some_function("Joan",50,80,30, gender="female", age=37, course="IT")
#
# save(name='Jean',dob='2005-12-30', age=27,gender='male',profession='Teacher')
# # save(age=18, dob='2001-12-31', profession='Engineer')

# print(addition(10,15,2,40))