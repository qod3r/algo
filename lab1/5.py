from timeit import Timer
from random import randint
import matplotlib.pyplot as plt


in_list = Timer("target in xlist", globals=globals())
in_set = Timer("target in xset", globals=globals())

plt_x = []
plt_list = []
plt_set = []

for i in range(1_000_000, 10_000_001, 1_000_000):
    xlist = list(range(i))
    xset = set(range(i))

    # target = randint(0, i)
    target = 'asd'
    print(f"i: {i}, target: {target}")
    
    plt_x.append(i)
    plt_list.append(in_list.timeit(number=100))
    plt_set.append(in_set.timeit(number=100))
    
print("List\t\tSet")
for i in range(len(plt_x)):
    print(f"{plt_list[i]:.6f}\t{plt_set[i]:.6f}")

plt.plot(plt_x, plt_list, plt_x, plt_set)
plt.xlabel("elements")
plt.ylabel("time")
plt.savefig("list+set.png")