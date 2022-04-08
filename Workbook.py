def workbook(n,k,arr):
    page=1
    special=0
    for x in range(0,n):
        b = []
        while arr[x] > 0:
            b.append(arr[x])
            arr[x] = arr[x] - 1
        b.sort()
        a = []
        for y in b:
            a.append(y)
            if y == page:
                special += 1
            if len(a) == k:
                if y == max(b):
                    page = page
                elif y != max(b):
                    page += 1
                a.clear()
        page += 1
    return special

def main():
    n = int(input("masukkan jumlah bab = "))
    k = int(input("masukkan total nomor per halaman ="))
    arr = list(map(int, input("jumlah nomor tiap bab =").rstrip().split()))
    result = workbook(n, k, arr)
    print(result)

main()

#https://www.hackerrank.com/challenges/lisa-workbook/problem
#versi panjang


