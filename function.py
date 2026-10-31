import random

# a = append w= write
with open("data.txt","a") as file:
    # file.write("99\n")
    # file.write("67\n")
    for temp in range(100):
        x= random.randint(-10,100)
        file.write(str(x)+"\n")
with open("data.txt","r") as file:
    content = file.read() # 0 params 0 args
    print(content)


