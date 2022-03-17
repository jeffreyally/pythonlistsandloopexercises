#Import random

#Create the function below:


def matrixBuilder(num):
    matrixlist = []
    for i in range(num):
        matrixlist.append([])
    for i in range(num):
        for j in range(num):
            matrixlist[j].append(1)
    return matrixlist
    

print(matrixBuilder(3))

