def tangga():

    def tangga_naik_kanan(n):
        for x in range(1,n+1):
            print(("#"*x).rjust(n))

    def tangga_naik_kiri(n):
        for x in range(1,n+1):
            print(("#"*x).ljust(n))

    def tangga_turun_kiri(n):
        for x in range(n,0,-1):
            print(("#"*x).ljust(n))

    def tangga_turun_kanan(n):
        for x in range(n,0,-1):
            print(("#"*x).rjust(n))

    tangga_naik_kanan(n)
    tangga_naik_kiri(n)
    tangga_turun_kiri(n)
    tangga_turun_kanan(n)

n = int(input("masukkan angka="))
tangga()
