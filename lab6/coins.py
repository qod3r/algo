def greedy(n):
    nominals = [100, 50, 10, 4, 3, 1]
    used = {
        100: 0,
        50: 0,
        10: 0,
        4: 0,
        3: 0,
        1: 0
    }

    for nom in nominals:
        while n >= nom:
            # print(n, nom)
            n -= nom
            used[nom] += 1
    
    return used

def dynamic(n):
    ...


if __name__ == "__main__":
    print(greedy(int(input("n: "))))