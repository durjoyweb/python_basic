# How to delete an element in a dictionary with a specific key



product={
    "price":10,
    "name":"pancil",
    "quantity": 5
}

print(product)


del product["quantity"]

print("updated dictionary is : \n", product)