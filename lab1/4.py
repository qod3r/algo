from timeit import Timer
import matplotlib.pyplot as plt


def gen_dict(n):
    k = [f"{i}" for i in range(n)]
    v = [i for i in range(n)]
    
    # print(dict(zip(k, v)))
    
    return dict(zip(k, v))


del_list = Timer("del xlist[i//2]", globals=globals())
del_dict = Timer("del xdict[f'{i//2}']", globals=globals())

plt_x = []
plt_dict = []
plt_list = []

for i in range(1_000_000, 10_000_001, 1_000_000):
    xlist = list(range(i))
    xdict = gen_dict(i)   
    print(i)
    
    plt_x.append(i)
    plt_list.append(del_list.timeit(number=1))
    plt_dict.append(del_dict.timeit(number=1))
    
print("List\t\tDict")
for i in range(len(plt_x)):
    print(f"{plt_list[i]:.6f}\t{plt_dict[i]:.6f}")
    
plt.plot(plt_x, plt_list, plt_x, plt_dict)
plt.xlabel("elements")
plt.ylabel("time")
plt.savefig("list+dict.png")