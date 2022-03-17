arr = [45, 67, 87, 23, 5,  32, 60]

#make a new list new_list = []?
#create for in range loop with reversed range
# append each number to newlist
#print new_list

new_list = []

for i in reversed(range(len(arr))):
    new_list.append(arr[i])

print(new_list)