def urut_nama(nama):
    nama.sort()
    return nama

def jawaban(pertanyaan):
    kemungkinan_jawaban = ["Y", "y", "t", "T"]
    if pertanyaan not in kemungkinan_jawaban:
        print("coba lagi")
    else:
        if pertanyaan == "Y" or pertanyaan == "y":
            return True
        else:
            return False

def urut_angka(nama):
    count = 0
    for x in range(len(nama)):
        nama[x] = (count + 1,nama[x])
        count = count + 1
    return nama

def main():
    nama =["Anatasia",
    "Jody",
    "Jose",
    "Michael",
    "Moody",
    "Arnold",
    "Christiawan",
    "Badia",
    "Bastian",
    "Charis",
    "Rivaldo",
    "Yehezkiel",
    "Yosia",
    "Mega",
    "Edgar",
    "Elson",
    "Fernando",
    "Tiffany",
    "Christopher",
    "Christyane",
    "Darren",
    "Giovanni",
    "Jason"]

    kelas = urut_nama(nama)

    tanya = str(input("apakah anda ingin memberi nomor absen?[Y/T]"))
    jawab = jawaban(tanya)
    if jawab == True:
        absen = urut_angka(kelas)
        return (absen)
    else:
        return kelas

print(main())



