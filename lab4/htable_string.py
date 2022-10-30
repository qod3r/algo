from sympy import nextprime, prevprime


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def hashfunction(self, key, size):
        key = str(key)
        sum = 0
        for pos in range(len(key)):
            sum += ord(key[pos])

        return sum % size
    
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
        tempslots = self.slots.copy()
        tempdata = self.data.copy()
        temp = list(zip(tempslots, tempdata))
        
        self.slots = [None] * newsize
        self.data = [None] * newsize
        
        for tup in temp:
            if tup[0] is not None:
                self.put(tup[0], tup[1])
        self.size = newsize
        
    def put(self, key, data):
        if len(self)/self.size > 0.7:
            print(f"λ: {len(self)/self.size:.3f}. Extending...")
            self._change_size(self._next_prime())
            print(f"New size: {self.size}")
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                step = 1
                nextslot = self.rehash(hashvalue, len(self.slots), step)
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    step += 1
                    nextslot = self.rehash(nextslot, len(self.slots), step)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    # linear
    # def rehash(self, oldhash, size):
    #     return (oldhash + 1) % size
    
    # square    
    def rehash(self, oldhash, size, step):
        return (oldhash + step ** 2) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        step = 1
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots), step)
                if position == startslot:
                    stop = True
                step += 1
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
    
    def __len__(self):
        return sum(x is not None for x in self.data)
    
    def __contains__(self, x):
        return x in self.data
    
    def __delitem__(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        step = 1
        while self.data[startslot] is None:
            startslot = self.rehash(startslot, len(self), step)
            step += 1
        
        stop = False
        found = False
        position = startslot
        step = 1
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                self.data[position] = None
                self.slots[position] = None
            else:
                position = self.rehash(position, len(self.slots), step)
                step += 1
                if position == startslot:
                    stop = True
                
        if len(self)/self.size < 0.2:
            print(f"λ: {len(self)/self.size:.3f}. Reducing...")
            self._change_size(self._prev_prime())
            print(f"New size: {self.size}")


if __name__ == "__main__":
    H = HashTable()
    H['asd'] = 'a'
    H['asd'] = 'bruh'
    H[22] = 'b'
    H[33] = 'c'
    H[44] = 'd'
    H[55] = 'd'
    H[66] = 'd'
    H[77] = 'd'
    H[123] = 'sdsd'
    H[124] = 'sdsd'
    # H[88] = 'd'
    print(H.slots)
    print(H.data)