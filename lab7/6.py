from binheap import BinHeap

class PQItem:
    def __init__(self, data, priority):
        self.priority = priority
        self.data = data
    
    def __repr__(self):
        return str(self.data)
    
    def __lt__(self, other):
        return True if self.priority < other.priority else False
    
    def __gt__(self, other):
        return True if self.priority > other.priority else False

class PriorityQueue:
    def __init__(self):
        self.heap = BinHeap()
    
    def enqueue(self, item, priority):
        self.heap.insert(PQItem(item, priority))
    
    def dequeue(self):
        return self.heap.delMin().data


pq = PriorityQueue()
#             vv  приоритет элемента
pq.enqueue(1, 10)
pq.enqueue("should do it", 2)
pq.enqueue("not important", 4)
pq.enqueue("priority one", 1)
pq.enqueue("maybe later", 3)

print(pq.heap.heapList)
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())

