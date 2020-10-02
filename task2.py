#! python3
name = input("What is your name ").strip()
coolnames= ("Lebron","Kobe","Michale","Shaq","Dennis")
for x in coolnames:
    if name == x:
        print("That name is on the list")
        break
if name not in coolnames:
    print("That name is not on the list")