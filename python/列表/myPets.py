#判断是否在列表内，in，not in
mypets = ['zophie','pooka','fat-tail']
print('enter a pet name:')
name = input()
if name not in mypets:
     print("i do not have a pet named" + name)
else:
    print(name + "is my pet.")
