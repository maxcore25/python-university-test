def main(n):
    if n == 0:
        return 0.77
    if n == 1:
        return 0.27
    if n >= 2:
        return 1-main(n-1)**9/38-(main(n-1)**3/51-main(n-2)/82)
