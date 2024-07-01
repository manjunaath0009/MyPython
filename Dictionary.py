thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset1 = list(thisset)
thisset1[0] = 'Apple';
print(thisset1)
thisset = set(thisset1)
print(thisset)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
x=thisdict.keys()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020
print(car.values())
print(car.keys())
print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "models" not in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("Hello World")