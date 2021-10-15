n = int(input("Ввведите максимальное число"))
if n<0:
    print("Неверно")
    exit()
sieve = set(range(2, n+1))
while sieve:
    prime = min(sieve)
    print(prime)
    sieve -= set(range(prime, n+1, prime))
