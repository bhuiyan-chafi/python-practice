fruitList=["apple","grapes","banana","mango","cherry"]
juiceList=["apple juice","grape juice","mango shake","cherry blossom"]

# we will add a new fruit to the fruitList
fruitList.append("orange")
print(fruitList)
# the difference between append() and insert() is that insert will push the object in the exact index that you mentioned.
fruitList.insert(5,"jackfruit")
print(fruitList)

# if we need to remove an item from the list
fruitList.remove("orange")
print("After remove(orange): ",fruitList)
# if we don't mention any index in the pop() function it will simply pop the last value
fruitList.pop(2)
print("After pop(2): ",fruitList)
del fruitList[3]
print("After del fruitList[3]: ",fruitList)


# joining two lists together
mixJuice=fruitList+juiceList
print("The mix juice: ",mixJuice)
# other ways to append the lists
fruitList.extend(juiceList)
print("After extending the fruitList: \n",fruitList)