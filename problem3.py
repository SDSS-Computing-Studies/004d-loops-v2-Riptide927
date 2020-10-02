#! python3
n =int(input("Gimme a numnber "))
a=0
for x in range (1,n+1):
        a = a + int("1" * x)
print("The sum of the series is " + str(a))