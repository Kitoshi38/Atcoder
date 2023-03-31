n = int(input())

def fib(n):
    fib_arr = [0] * (n+1)
    def _fib(n):
        if n == 0 or n == 1:
            return 1
        elif fib_arr[n]:
            return fib_arr[n]
        else:
            fib_arr[n] = _fib(n-1) + _fib(n-2)
            return fib_arr[n]
    return _fib(n)

print(fib(n))