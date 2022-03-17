myNumbers = [23,234,345,4356234,243,43,56,2]


def increment_by_one(num):
    return num * 3



new_list = list(map(increment_by_one,myNumbers))

print(new_list)