#angka di list dijumlah(index yang sama gak perlu),yang bisa dibagi k diitung masuk
def divisibleSumPairs(n, k, ar):
    count=0
    for x in range(0,n-1):
        for y in (ar[x+1:]):
            a=ar[x]+y
            if a % k == 0:
                    count += 1
            else:
                count = count
    return count

jumlah=int(input("ada berapa angka?"))
pembagi=int(input("pembagi="))
daftar_angka=list(map(int, input("masukkin angka sebanyak n=").rstrip().split()))
print(divisibleSumPairs(jumlah,pembagi,daftar_angka))

#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem