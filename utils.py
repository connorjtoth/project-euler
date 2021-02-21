def get_smallest_prime_factor(n, primes):
    smallest_prime_factor = next((p for p in primes if n % p == 0), None)

    if smallest_prime_factor is None:
        i = primes[-1] + 2
        while i <= n:
            if all(i % p != 0 for p in primes):
                primes.append(i)
                if n % i == 0:
                    return i
            i += 2

    return smallest_prime_factor


def get_divisors(n, memo={1: {1}}, primes=[2, 3], proper=False):
    if n == 0:
        raise ValueError
    if n not in memo:
        divisors = {1, n}
        prime_factor = get_smallest_prime_factor(n, primes)

        if prime_factor != n:
            other_factor = n // prime_factor
            other_divisors = get_divisors(other_factor, memo, primes)
            divisors.update(prime_factor * x for x in other_divisors)
            divisors.update(other_divisors)
        memo[n] = divisors

    result = set(memo[n])
    if proper:
        result.discard(n)
    return result


def next_permutation(permutation):
    k = max(k for k in range(len(permutation) - 1)
            if permutation[k] < permutation[k + 1])
    j = max(j for j in range(k + 1, len(permutation))
            if permutation[k] < permutation[j])
    permutation[k], permutation[j] = permutation[j], permutation[k]
    permutation = permutation[:k + 1] + list(reversed(permutation[k + 1:]))
    return permutation