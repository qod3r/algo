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


fig = plt.figure()
ax_random = fig.add_subplot()

step = 500
t_sel = Timer("selection(arr1)", globals=globals())
t_quick = Timer("quicksort(arr2, 0, len(arr2) - 1)", globals=globals())

plt_x, plt_s, plt_q = [], [], []

for i in range(step, step * 10 + 1, step):
    print(i)
    
    arr1 = randint(-step, step, [i])
    arr2 = randint(-step, step, [i])

    plt_x.append(i)
    plt_s.append(t_sel.timeit(number=1))
    plt_q.append(t_quick.timeit(number=1))

print(*plt_s, *plt_q, sep="\n")

ax_random.set_title("random order")
ax_random.set_xlabel("elements")
ax_random.set_ylabel("time")
ax_random.plot(plt_x, plt_s, label='selection')
ax_random.plot(plt_x, plt_q, label='quick')
ax_random.legend()


sys.setrecursionlimit(1500)
step = 100
ax_sorted = fig.add_subplot()
plt_x, plt_s, plt_q = [], [], []
for i in range(step, step * 10 + 1, step):
    print(i)
    
    arr1 = list(range(i))
    arr2 = list(range(i))

    plt_x.append(i)
    plt_s.append(t_sel.timeit(number=1))
    plt_q.append(t_quick.timeit(number=1))

print(*plt_s, *plt_q, sep="\n")

ax_random.set_title("ordered")
ax_sorted.set_xlabel("elements")
ax_sorted.set_ylabel("time")
ax_sorted.plot(plt_x, plt_s, label='selection')
ax_sorted.plot(plt_x, plt_q, label='quick')
ax_sorted.legend()


plt.savefig("sorts.png")

