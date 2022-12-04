from htable_string import HashTable


text = input().split()
h = HashTable()

for word in text:
    if word not in h.slots:
        h[word] = 1
    else:
        h[word] = h[word] + 1
    print(h[word], end=" ")
print()