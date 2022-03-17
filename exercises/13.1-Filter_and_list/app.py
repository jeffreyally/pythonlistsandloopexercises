
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

def startsWithR(items):
    return items.startswith('R') == True

resulting_names = list(filter(startsWithR,all_names))

print(resulting_names)




