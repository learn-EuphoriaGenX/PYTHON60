# list, tuple, set, dict

myList = ['apple', 'banana', 'banana', True, False, 13, 23.4]
#ordered, mutable, allow duplicates, 

myList[0] = "mango"
# myList[1] = banana
# myList[2] = true
# ...
for i in range(0, len(myList)):
    print(f'myList[{i}] = {myList[i]}')

print(myList.count('banana'))
myList.reverse()
print(myList)
print(myList.index('mango'))



# 