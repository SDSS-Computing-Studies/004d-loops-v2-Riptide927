#! python3

h = int(input("Height "))
w = int(input("Width "))

for y in range(h):
    for x in range(w):
        print("*",end="")
    print("")