my_dict = {"Иван": 1998, "Анна": 2001}
print(my_dict)
print("Existing value: ", my_dict["Анна"])
print("Not existing value: ", my_dict.get("Алекс"))
my_dict.update({"Николай": 1996,
                "Ирина": 2000})
a = my_dict.pop("Иван")
print("Deleted value: ", a)
print("Modified dictionary: ", my_dict)
print( )
#
my_set = {1, 1.4, "apple", }
print("set: ", my_set)
my_set.add("banana")
my_set.add(2)
my_set.remove(1.4)
print("Modified set: ", my_set)