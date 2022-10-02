from random import randint
from timeit import Timer
import matplotlib.pyplot as plt
from numpy.random import randint
import sys


def selection(arr):
    size = len(arr)
    for i in range(size):
        min_index = i
 
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])

def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
      
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quicksort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quicksort(array, low, pi - 1)
    quicksort(array, pi + 1, high)


fig, axes = plt.subplots(3, 1)
plt.tight_layout(pad=2.5)

t_sel = Timer("selection(arr1)", globals=globals())
t_quick = Timer("quicksort(arr2, 0, len(arr2) - 1)", globals=globals())


# random list
step = 200
plt_x, plt_s, plt_q = [], [], []
for i in range(step, step * 10 + 1, step):
    print(i)
    
    arr1 = randint(-step, step, [i])
    arr2 = randint(-step, step, [i])

    plt_x.append(i)
    plt_s.append(t_sel.timeit(number=1))
    plt_q.append(t_quick.timeit(number=1))
print(*plt_s, *plt_q, sep="\n")

axes[0].set_title("random order")
axes[0].set_xlabel("elements")
axes[0].set_ylabel("time")
axes[0].plot(plt_x, plt_s, label='selection')
axes[0].plot(plt_x, plt_q, label='quick')
axes[0].legend()


# ordered list
sys.setrecursionlimit(2500)
step = 200
plt_x, plt_s, plt_q = [], [], []
for i in range(step, step * 10 + 1, step):
    print(i)
    
    arr1 = list(range(i))
    arr2 = list(range(i))

    plt_x.append(i)
    plt_s.append(t_sel.timeit(number=1))
    plt_q.append(t_quick.timeit(number=1))
print(*plt_s, *plt_q, sep="\n")

axes[1].set_title("ordered")
axes[1].set_xlabel("elements")
axes[1].set_ylabel("time")
axes[1].plot(plt_x, plt_s, label='selection')
axes[1].plot(plt_x, plt_q, label='quick')
axes[1].legend()


# reverse ordered list
step = 200
plt_x, plt_s, plt_q = [], [], []
for i in range(step, step * 10 + 1, step):
    print(i)
    
    arr1 = list(range(i, 0, -1))
    arr2 = list(range(i, 0, -1))

    plt_x.append(i)
    plt_s.append(t_sel.timeit(number=1))
    plt_q.append(t_quick.timeit(number=1))
print(*plt_s, *plt_q, sep="\n")

axes[2].set_title("reverse ordered")
axes[2].set_xlabel("elements")
axes[2].set_ylabel("time")
axes[2].plot(plt_x, plt_s, label='selection')
axes[2].plot(plt_x, plt_q, label='quick')
axes[2].legend()


plt.savefig("sorts.png", dpi=250)
