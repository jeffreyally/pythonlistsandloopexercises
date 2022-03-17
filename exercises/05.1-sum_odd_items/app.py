arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

auxiliar = 0
for numbers in arr:
    
    if numbers % 2 == 1:
        print(numbers)
        auxiliar = auxiliar + numbers



print(auxiliar)