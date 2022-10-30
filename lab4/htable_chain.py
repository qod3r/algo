from unordered import UnorderedList
from sympy import nextprime, prevprime


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key, size):
        return key % size
    
    def _next_prime(self):
        prime = self.size
        while prime <= self.size*2:
            prime = nextprime(prime)
        return prime
    
    def _prev_prime(self):
        prime = self.size
        while prime > self.size//2:
            prime = prevprime(prime)
        return prime

    def _change_size(self, newsize):
        temp = {}
        
        for key in self.slots:
            if key is not None:
                for i in range(1, self.data[self.hashfunction(key, self.size)].size(), 2):
                    temp[self.data[self.hashfunction(key, self.size)][i-1]] = self.data[self.hashfunction(key, self.size)][i]
                        
        self.slots = [None] * newsize
        self.data = [None] * newsize
        self.size = newsize

        for tup in temp.items():
            self.put(tup[0], tup[1])
    
    def put(self, key, data):
        if len(self)/self.size > 0.7:
            print(f"λ: {len(self)/self.size:.3f}. Extending...")
            self._change_size(self._next_prime())
            print(f"New size: {self.size}")
            
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = UnorderedList()
            self.data[hashvalue].add(key)
            self.data[hashvalue].append(data)
        else:
            if not self.data[hashvalue].search(key):
                self.data[hashvalue].append(key)
                self.data[hashvalue].append(data)
            else:
                idx = self.data[hashvalue].index(key) + 1
                self.data[hashvalue].remove(self.data[hashvalue][idx])
                self.data[hashvalue].insert(idx, data)
        # print(self.data[hashvalue])

    def get(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))
        data = None
        
        if self.slots[hashvalue] is not None:
            idx = self.data[hashvalue].index(key)
            if idx is not None:
                idx += 1
                data = self.data[hashvalue][idx]
                
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
    
    def __len__(self):
        res = 0
        for e in self.data:
            if e is not None:
                res += e.size() // 2
        return res

    def __contains__(self, item):
        res = False
        for e in self.data:
            if e is not None:
                if e.search(item):
                    res = True
                    break
        return res

    def __delitem__(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] is None:
            pass
        elif self.data[hashvalue].size() == 2:
            self.slots[hashvalue] = None
            self.data[hashvalue] = None
        else:
            idx = self.data[hashvalue].index(key)
            if idx is not None:
                self.data[hashvalue].remove(key)
                self.data[hashvalue].remove(self.data[hashvalue][idx])
    
        if len(self)/self.size < 0.2:
            print(f"λ: {len(self)/self.size:.3f}. Reducing...")
            self._change_size(self._prev_prime())
            print(f"New size: {self.size}")


if __name__ == "__main__":
    H = HashTable()

    H[11] = 'a'
    H[22] = 'b'
    H[33] = 'c'
    H[44] = 'd'
    # H[55] = 'e'
    # H[77] = 'e'
    # H[88] = 'e'
    # print(len(H))
    # H[99] = 'bruh'
    # H[110] = 'bruh2'
    # H[45] = 'tewnty two'
    # print(len(H))
    # H[12] = 'asd'
    # H[13] = 'vv'
    print(H.slots)
    print(*H.data)
    del H[11]
    del H[33]
    
    print(H.slots)
    print(*H.data)
    # print(H[99])
    # print(len(H))
    # print()
    # print('a' in H)
    # print('asdsdsdsd' in H)