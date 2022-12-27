from merge import merge_sort
from merge_iter import merge_sort as merge_sort_iter
from timeit import Timer
import random
import matplotlib.pyplot as plt


def almost(r):
    a = list(range(r))
    x, y = r//2, r//4
    a[x], a[x + y] = a[x + y], a[x]
    return a

def almost_reverse(r):
    a = list(range(r))
    a.reverse()
    x, y = r//2, r//4
    a[x], a[x + y] = a[x + y], a[x]
    return a

def list_95(r):
    a = list(range(r))
    idx = int(r * 0.95)
    a[idx:] = [random.random() for _ in range(r - idx)]
    return a

def var10(r):
    a = list(range(r))
    chunks = [10 * x for x in range(r//10)]
    for chunk in chunks:
        aa = a[chunk:chunk+10]
        random.shuffle(aa)
        a[chunk:chunk+10] = aa
    return a


if __name__ == "__main__":
    # a = [7, 3, 9, 4, 2, 5, 6, 1, 8]
    # a = [3, 5, 2, 9, 8, 1, 6, 4, 7]
    # a = [1, 2, 3, 4, 5, 6, 7, 8]
    # a = [8, 7, 6, 5, 4, 3, 2, 1]
    # print(f"a: {a}\n")
    # a = merge_sort_iter(a)
    # print(f"\nsorted: {a}")
    
    methods = {
        "random": lambda r: [random.random() for _ in range(r)],
        "almost": almost,
        "almost_reverse": almost_reverse,
        "01": lambda r: [random.choice([0, 1]) for _ in range(r)],
        "95": list_95,
        "var10": var10
    }
    ranges = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
    for method in methods.keys():
        plt_x, plt_t = [], []
        timer = Timer(f"merge_sort(a)", globals=globals())
        print(f"{method}:")
        
        for r in ranges:
            print(r)
            a = methods[method](r)
            plt_x.append(r)
            plt_t.append(timer.timeit(number=100))
        
        plt.plot(plt_x, plt_t, marker='.', label=method)
        plt.xlabel("elements")
        plt.ylabel("time")
        plt.legend()
    
    plt.savefig(f"times.png", dpi=240)
