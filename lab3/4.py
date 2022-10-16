from unordered import UnorderedList
from timeit import Timer
import matplotlib.pyplot as plt


class Stack:
    def __init__(self):
        self.lst = UnorderedList()
    
    def push(self, item):
        self.lst.add(item)
    
    def pop(self):
        return self.lst.pop(0)

    def peek(self):
        return self.lst.head.getData()
    
    def isEmpty(self):
        return self.lst.size() == 0
    
    def __len__(self):
        return self.lst.size()

class Queue:
    def __init__(self):
        self.lst = UnorderedList()
    
    def enqueue(self, item):
        self.lst.append(item)

    def dequeue(self):
        return self.lst.pop(0)

    def isEmpty(self):
        return self.lst.size() == 0
    
    def __len__(self):
        return self.lst.size()

class Deque:
    def __init__(self):
        self.lst = UnorderedList()
    
    def addFront(self, item):
        self.lst.add(item)
    
    def addRear(self, item):
        self.lst.append(item)
    
    def removeFront(self):
        return self.lst.pop(0)
    
    def removeRear(self):
        return self.lst.pop()
    
    def isEmpty(self):
        return self.lst.size() == 0
    
    def __len__(self):
        return self.lst.size()


if __name__ == "__main__":
    s, q, d = Stack(), Queue(), Deque()
    
    t_s = Timer("s.push(e)", globals=globals())
    t_q = Timer("q.enqueue(e)", globals=globals())
    t_df = Timer("d.addFront(e)", globals=globals())
    t_dr = Timer("d.addRear(e)", globals=globals())
    
    plt_x, plt_s, plt_q, plt_df, plt_dr = [], [], [], [], []
    
    step = 10_000
    for i in range(step, step*10 + 1, step):
        print(i)
        e = list(range(1000))
        
        plt_x.append(i)
        plt_s.append(t_s.timeit(number=100))
        plt_q.append(t_q.timeit(number=100))
        plt_df.append(t_df.timeit(number=100))
        plt_dr.append(t_dr.timeit(number=100))

    plt.plot(plt_x, plt_s, label='stack')
    plt.plot(plt_x, plt_q, label='queue')
    plt.plot(plt_x, plt_df, label='deque front')
    plt.plot(plt_x, plt_dr, label='deque rear')
    plt.xlabel('elements')
    plt.ylabel('time')
    plt.legend()
    plt.title('element addition')
    plt.savefig('structures_addition.png')
        