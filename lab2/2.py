def tribonacci(n):
    if (n == 0 or n == 1):
        return 0
    elif (n == 2):
        return 1
    else:
        return (tribonacci(n - 1) +
                tribonacci(n - 2) +
                tribonacci(n - 3))

n = int(input("n: "))
print(f"trib(n): {tribonacci(n)}")