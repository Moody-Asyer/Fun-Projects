def main():
    def rotLeft(a, d):
        b = a[:]
        for x in range(0, n):
            baru = (x + d) % len(a)
            b[x] = a[baru]

        return b

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result_kiri = rotLeft(a, d)
    result = result_kiri
    print(result)

main()