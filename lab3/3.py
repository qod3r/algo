from tempfile import tempdir
from unordered import UnorderedList, Node


# iterative
def reverse(node):
    temp = []
    while node is not None:
        temp.append(node)
        node = node.getNext()
    
    # for n in temp:
    #     print(n.getData())
    
    temp[0].setNext(None)
    for i in range(len(temp)-1, 0, -1):
        # print(i)
        temp[i].setNext(temp[i - 1])

    return temp[-1]


if __name__ == "__main__":
    lst = UnorderedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    print(lst)

    lst.head = reverse(lst.head)
    print(lst)
    lst.add(123)
    print(lst)