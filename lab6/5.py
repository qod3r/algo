from pprint import pprint


def longest_subseq(a, b):
    m = len(a)
    n = len(b)

    L = [[None]*(n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    # pprint(L)
    return L[m][n]


if __name__ == "__main__":
    a = input("word: ")
    b = input("similar: ").split()
    
    max_len = 0
    idx = 0
    for i in range(len(b)):
        c = longest_subseq(a, b[i])
        if c > max_len:
            max_len = c
            idx = i
    
    print(f"most similar: {b[idx]}, len: {max_len}")