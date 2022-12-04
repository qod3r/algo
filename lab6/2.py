from pprint import pprint

# dynamic
def backpack(items, max_w):
    N, W, V = 0, 1, 2
    n = len(items)
    K = [[0 for x in range(max_w + 1)] for x in range(n + 1)]
    curr_combo = []
    
    for row in range(n + 1):
        for col in range(max_w + 1):
            if row == 0 or col == 0:
                K[row][col] = 0
            elif items[row-1][W] <= col:
                K[row][col] = max(items[row-1][V] + K[row-1][col-items[row-1][W]], K[row-1][col])
            else:
                K[row][col] = K[row-1][col]
    
    pprint(K)
    return K[n][max_w]

if __name__ == "__main__":
    items = [
        ('вода', 1, 8),
        ('книга', 1, 8),
        ('еда', 3, 9),
        ('куртка', 2, 5),
        ('камера', 2, 6)
    ]
    w = 6
    print(backpack(items, w))