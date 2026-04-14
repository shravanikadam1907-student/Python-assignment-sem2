# create and access elements
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
brand = my_dict["brand"]
print(brand) 

#update dictionary
my_dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict2={"brand": "thar", "model": "RWD", "year": 20}
new_dict=my_dict1.update(my_dict2)
print(new_dict)





#remove elements
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del my_dict["model"]



#merging dictionariesmy_dict1= {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict2={"brand": "ford", "model": "escape", "year": 2026}

merged_dict=my_dict|my_dict2
print(merged_dict)