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
