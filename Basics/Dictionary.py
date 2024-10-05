# Dictionary is something that returns block of objects like we did in JSON

carModels = {
    "company": "toyota",
    "model": "crown",
    "year": 2024,
    "release": "01/01/2024",
    "customer": {
        "name": "chafi",
        "country": "Bangladesh"
    }
}
print("Printing the whole Dictionary: \n", carModels)

# if we want to get a specific value
print("Getting the company only: \n", carModels.get("company"))
# getting another data from the nested Dictionary
print("Getting the customer name only: \n", carModels.get("customer", {}).get("name"))
# removing an item from the list
carModels.pop("release")
print("After removing the release attribute: \n", carModels)
# to remove the entire dictionary we can use del keyword, but we can also delete a specific item from the dictionary using del
# del carModel
# print all the key names of the dict
print("Printing all the keys of the dict:")
for item in carModels:
    print(item)
print("Printing all the values of the dict:")
for item in carModels.values():
    print(item)
print("Printing key and value together: ")
for item,value in carModels.items():
    print(item,value)
