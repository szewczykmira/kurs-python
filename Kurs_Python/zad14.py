def count_for_value(n, mods):
    times = 0
    while n % mods == 0:
        times += 1
        n /= mods
    return times, n

def rozklad(n):
    list_of_parts = []
    parts = 2
    if n <= 1:
        return list_of_primes
    while parts <= n:
        times, n = count_for_value(n, parts)
        if times:
            list_of_parts.append((parts, times))
        parts += 1
    return list_of_parts
