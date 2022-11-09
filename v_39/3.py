def main(m, n, z, b, x):
    res = 0
    res2 = 0

    for k in range(1, n + 1):
        for i in range(1, m + 1):
            res += 44 * k ** 2 - 64 * (76 * i ** 2 + z / 51) ** 4

    for j in range(1, n + 1):
        for i in range(1, b + 1):
            res += (i ** 2 / 37 - x) ** 7 - (j - j ** 3 - 0.11)

    return '%.2e' % (res - res2)


print(main(7, 4, 0.42, 3, 0.54))
print(main(2, 7, 0.65, 8, 0.32))
print(main(2, 3, 0.12, 2, -0.87))
print(main(4, 5, 0.51, 8, 0.64))
print(main(2, 5, -0.86, 8, -0.12))
