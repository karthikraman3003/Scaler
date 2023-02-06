def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    t = 1
    for i in range(t):
        a = 9
        b = 6
        c = (a * b) // gcd(a, b)
        print(c)


if __name__ == '__main__':
    main()