from unordered import UnorderedList


def move_to_front(lst):
    line = input()
    if lst.index(line) is not None:
        lst.remove(line)
    lst.add(line)


if __name__ == "__main__":
    lst = UnorderedList()
    
    try:
        while True:
            move_to_front(lst)
            print(lst)
    except KeyboardInterrupt:
        print("")
        exit(0)