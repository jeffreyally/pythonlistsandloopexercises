theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

def wikiwoko(num):
    str = 'woko' if num == 0 else "wiki" if num == 1 else None
    return str

print(list(map(wikiwoko,theBools)))

#sample
#a = "neg" if b<0 else "pos" if b>0 else "zero"