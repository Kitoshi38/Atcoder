n = int(input())

def is_prime(m):
    if m == 1:
        return False
    flag = True
    for i in range(2, int(m**0.5)+1):
        if m % i == 0:
            flag = False
            break
    return flag

print(f'{n}: ', end="")
prime_arr = []
for i in range(2, int(n**0.5)+1):
    if is_prime(i):
        prime_arr.append(i)

for i in range(len(prime_arr)):
    if n == 1:
        break
    else:
        while(1):
            if n % prime_arr[i] == 0:
                n = n // prime_arr[i]
                if n != 1:
                    print(prime_arr[i], end=" ")
                else:
                    print(prime_arr[i])
            else:
                break

if n != 1:
    print(n)
