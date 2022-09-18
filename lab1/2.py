from timeit import Timer
from random import choice
from string import ascii_lowercase
import matplotlib.pyplot as plt


def gen_string(n):
    s = ""
    for _ in range(int(n / 2)):
        s += choice(ascii_lowercase)
    s += s[::-1]
    return s

def palindrome_naive(s):
    s1 = s
    s2 = s[::-1]
    
    for i in range(len(s)):
        if s1[i] != s2[i]:
            return False
    return True
    
def palindrome_good(s):
    return s == s[::-1]


step = 1_000_000
t_naive = Timer("palindrome_naive(s)", globals=globals())
t_good = Timer("palindrome_good(s)", globals=globals())
plt_x, plt_n, plt_g = [], [], []

for i in range(step, step*10+1, step):
    print(i)
    s = gen_string(i)
    plt_x.append(i)
    plt_n.append(t_naive.timeit(number=100))
    plt_g.append(t_good.timeit(number=100))
    
print(*plt_n, *plt_g, sep="\n")

plt.plot(plt_x, plt_n, plt_x, plt_g, marker='.')
plt.xlabel("number")
plt.ylabel("time")
plt.savefig("palindromes.png")

# print(palindrome_good(gen_string(10)))