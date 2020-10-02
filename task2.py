#! python3
name = input("What is your name ").strip()
coolnames= ("Joe","Jeff","Jim","Jake")
for x in coolnames:
    if name == x:
        print("you have a cool name")
        break
if name not in coolnames:
    print("your name is lame")