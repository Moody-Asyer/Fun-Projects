def hourglassSum(arr):
    angka_gede = -63
    for x in range(4):
        for y in range(4):
            jumlah = arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
            if jumlah > angka_gede:
                angka_gede = jumlah
            else:
                angka_gede = angka_gede

    return angka_gede

arr = []
for _ in range(6):
        arr.append(list(map(int, input("masukkan angka =").rstrip().split())))

hasil = hourglassSum(arr)
print(hasil)