my_list = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]

def my_function(numbers):
    new_list = []
    for numb in numbers:
        if numb == 0:
            new_list.append('Yahoo')
        else:
            new_list.append(numb)
        
    return new_list
print(my_function(my_list))


