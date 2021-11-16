#  Program: 17_dictionary.py
#  Author: Michael Souther
#  Date: 09/21/2020
#  Create a dictionary
product1 = {"product_id":1000,"name":"Product1","cost":3.95}
product2 = dict(product_id=1001,name="Product2",cost=2.95)
print("Print dictionaries");
print(product1)
print(product2)

print("Print value using key from dictionary");
print(product1['name'])
# print(product1['price'])
print("Print values using get method and key from dictionary");
print(product1.get('price'))
print(product1.get('product_id'))
print("Loop Product 1 Dictionary")
for key in product1.keys():
    # access value given key
    value=product1[key]
    print(key,"=",value)    
print("Loop Product 2 Dictionary")
for key, value in product2.items():
    print(key,"=",value)
print("product_id" in product1)
print("Add a key and value to a dictionary");
product1["color"] = "red"
print(product1['color'])
print("Pop a key/value pair from a dicationary")
print(product1)
product1.pop("cost")
print(product1)
