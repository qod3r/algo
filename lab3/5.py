class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext
        
    def setPrev(self, newprev):
        self.prev = newprev
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
            

class DoubleList():
    def __init__(self):
        self.head = None
    
    def __str__(self):
        res = ""
        current = self.head
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        while current != None:
            bolden = current is self.head
            res += f"{'[' + BOLD if bolden else ''}{current.getData()}{ENDC if bolden else ''}{']' if current.getNext() == None else ', '}"
            current = current.getNext()
        
        return res
    
    def __len__(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count
        
    def isEmpty(self):
        return self.head is None
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    # front
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        
        if self.head is not None:
            self.head.prev = temp
        
        self.head = temp
            
    def append(self, item):
        temp = Node(item)
        current = self.head
        
        if self.head is None:
            temp.setPrev(None)
            self.head = temp
            return
        
        while current.getNext() is not None:
            current = current.getNext()
        
        current.setNext(temp)
        temp.setPrev(current)
    
    def removeFront(self):
        data = self.head.getData()
        self.head.getNext().setPrev(None)
        self.head = self.head.getNext()
        return data
    
    def removeRear(self):
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        
        data = current.getData()
        current.getPrev().setNext(None)
        return data
        
    def insertBefore(self, pos, item):
        if pos >= len(self):
            print('tried to insert out of bounds')
            return
        
        current = self.head
        prev = None
        for _ in range(pos):
            prev = current
            current = current.getNext()
        
        temp = Node(item)
        prev.setNext(temp)
        temp.setPrev(prev)
        temp.setNext(current)
        current.setPrev(temp)        
    
    def insertAfter(self, pos, item):
        if pos == len(self) - 1:
            self.append(item)
            return
        if pos < 0 or pos > len(self) - 1:
            print('tried to insert out of bounds')
            return
        
        current = self.head
        for _ in range(pos):
            current = current.getNext()
        
        temp = Node(item)
        temp.setNext(current.getNext())
        current.setNext(temp)
        temp.setPrev(current)
        
        if temp.getNext() is not None:
            temp.getNext().setPrev(temp)
            
    def remove(self, pos):
        if pos < 0 or pos >= len(self):
            print('tried to delete out of bounds')
            return
        
        data = None
        if pos == 0:
            data = self.removeFront()
            return data
        if pos == len(self) - 1:
            data = self.removeRear()
            return data
        
        current = self.head
        for _ in range(pos):
            current = current.getNext()
        
        current.getPrev().setNext(current.getNext())
        current.getNext().setPrev(current.getPrev())
        data = current.getData()
        return data
        


if __name__ == "__main__":
    l = DoubleList()

    l.add('a')
    l.append('b')
    l.append('c')
    l.append('d')
    l.insertBefore(3, 'asd')
    print(l)
    l.insertAfter(3, 'zxc')
    print(l)
    print(l.removeFront())
    print(l)
    print(l.removeRear())
    print(l)
    print(l.search('asd'))
    print(l.remove(1))
    print(l)
    print(l.remove(2))
    print(l)
    
    