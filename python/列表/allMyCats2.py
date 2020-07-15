#使用列表进行改进！

catNames = []
while True:
    print("enter the name of cat " +str(len(catNames) + 1) + "(or enter nothing to stop)")
    name = input()
    if  name == '':
       break
    catNames = catNames + [name]
print("the cat names are:")
for name in catNames:
    print(' ' + name)
