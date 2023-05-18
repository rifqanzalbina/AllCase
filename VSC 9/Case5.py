myList = ['banana', 'cherry' , 'apple']
print(myList)

for i in myList:
    print(i)


if 'melon' in myList:
    print("Yes that's fruit in Here")
else:
    print("No that's fruit In Here")

myList.append('lemon')
item = myList.pop()
print(item)
print(myList)