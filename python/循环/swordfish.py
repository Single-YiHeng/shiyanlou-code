while True:
    print("who are you!")
    name = input()
    if name != 'Joe':
        continue
        print("hello,Joe. what is the password? (it is a fish)")
    password = input()
    if password == 'swordfish':
        break
print("access granted.")
