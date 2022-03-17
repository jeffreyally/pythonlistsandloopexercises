my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


new_list = []

for i in my_list:
    print(type(i))
    if type(i) is list or type(i) is dict:
        
        new_list.append(i)
    


print(new_list)

#be careful with is as it is very specific.
# isinstance tends to be more straight forward

