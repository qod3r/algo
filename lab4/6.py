import os
import hashlib


dir = input("Enter dir: ")

hashes = {}
for file in os.listdir(os.path.dirname(__file__) + "/" + dir):
    hasher = hashlib.md5()
    with open(f"{dir}/{file}", 'rb') as f:
        chunk = 0
        while chunk != b'':
            chunk = f.read(1024)
            hasher.update(chunk)
        hashes[file] = hasher.hexdigest() 

hashes_reverse = {}
for k, v in hashes.items():
   if v not in hashes_reverse:
      hashes_reverse[v] = [k]
   else:
      hashes_reverse[v].append(k)

for k, v in hashes_reverse.items():
    if len(v) > 1:
        print(v)