# access element from nested dictionary


product={
  "mystock1" : {"price":10,
    "name":"pancil",
    "quantity": 5},



   "mystock2" :  {"price":510,
    "name":"bag",
    "quantity": 3},



     "mystock3" : {"price":10,
    "name":"pen",
    "quantity": 15},

}

print(product["mystock1"]["name"])
print(product["mystock2"]["name"])
print(product["mystock3"]["name"])