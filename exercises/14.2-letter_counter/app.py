par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
for letter in par:
    if letter == ' ':
        continue
    if letter not in counts:
        counts[letter.lower()] = 1
    else:
        counts[letter.lower()] += 1

print(counts)

