"""Prime number helpers."""


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def primes_up_to(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]


if __name__ == "__main__":
    print(primes_up_to(int(input("Limit: "))))
