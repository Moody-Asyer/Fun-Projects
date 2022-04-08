#Ngitung burung migrasi(jumlah paling banyak tapi nomor paling kecil)
def migratoryBirds(arr):
    tipe = 0
    banyak = 0
    c = set(arr)
    for x in c:
        a = arr.count(x)
        if a > banyak:
            banyak = a
            tipe = x
        else:
            banyak = banyak
            tipe = tipe
    return tipe


arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

print(result)

