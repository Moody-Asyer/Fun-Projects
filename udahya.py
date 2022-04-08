def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def binom(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

def geo(n,p):
    return (1-p)**(n-1) * p #ATAU
    #return (1-p)**(n-x) * p
#n=berapa kali
#p=persentase berhasil(desimal)
#q=1-p(gagal)
#x=n ke berapa



