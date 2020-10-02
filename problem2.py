#! python3

n = int(input("Give me a interger "))
N=str(n)
for x in range(1,n):
    n = n*x
print(N+"!"+" is",n)