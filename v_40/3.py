def main(n, a, b):
    res = 0

    for k in range(1, b + 1):
        for c in range(1, a + 1):
            for i in range(1, n + 1):
                res += 55 * (20 * k - i ** 3 - 56 * c ** 2) ** 2 + 1

    return '%.2e' % res


print(main(6, 2, 3))
print(main(5, 2, 3))
print(main(2, 8, 8))
print(main(6, 3, 3))
print(main(5, 3, 6))
