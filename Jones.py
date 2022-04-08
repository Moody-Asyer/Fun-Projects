def true_or_false(jawaban):
    kemungkinan_jawaban = ["Y","y","t","T"]
    if jawaban not in kemungkinan_jawaban:
        print("situ labil")
    else:
        if jawaban == "Y" or jawaban == "y":
            return True
        elif jawaban == "T" or jawaban == "t":
            print("anda tidak asik")

def kaya_baik_ganteng(duit,sikap,muka):
    kemungkinan_jawaban = ["Y", "y", "t", "T"]
    if duit not in kemungkinan_jawaban or sikap not in kemungkinan_jawaban or muka not in kemungkinan_jawaban:
        print("jawab ketiganya!!!")
    else:
        if (duit == "y" and sikap == "y" and muka == "y") or (duit == "Y" and sikap == "Y" and muka == "Y"):
            return True
        else:
            return False
def main():
    cowo = str(input("apakah anda lagi deketin cewe?[Y/T]"))
    jawab = true_or_false(cowo)

    if jawab == True:
        x = str(input("apakah anda baik?[Y/T]"))
        y = str(input("apakah anda ganteng?[Y/T]"))
        z = str(input("apakah anda kaya?[Y/T]"))
        hasil = kaya_baik_ganteng(x,y,z)

        if hasil == True:
            cewe = "naksir sama lu"
            print("cewe : gua",cewe)
        else:
            tai = "maaf kita temenan aja"
            for x in range (0,100):
                print(tai)

main()