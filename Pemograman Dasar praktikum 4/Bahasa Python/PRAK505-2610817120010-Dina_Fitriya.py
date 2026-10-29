def Biodata(tahunLahir, Namaku, Asal):
    tahun_sekarang = 2020
    age = tahun_sekarang - tahunLahir

    print("Perkenalkan Nama Saya :", Namaku)
    print("Umur Saya :", age)
    print("Saya Adalah Angkatan :", tahun_sekarang)
    print("Asal Saya dari :", Asal)


tahunLahir = int(input())
Namaku = input()
Asal = input()
Biodata(tahunLahir, Namaku, Asal)