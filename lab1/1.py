from timeit import Timer
import matplotlib.pyplot as plt

# All prime numbers before n (inclusive)
# O(nlogn)
def foo(n): # n - число
    res = []
    
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1
            j += 1
        if divisors == 0:
            res.append(i)
            
    return res

t = 1000

plt_x = []
plt_t = []
m = Timer("foo(i)", globals=globals())
for i in range(t, t*10+1, t):
    print(i)
    plt_x.append(i)
    plt_t.append(m.timeit(number=100))
    
print(*plt_t, sep='\n')

plt.plot(plt_x, plt_t, marker='.')
plt.xlabel("number")
plt.ylabel("time")
plt.savefig("primes.png")