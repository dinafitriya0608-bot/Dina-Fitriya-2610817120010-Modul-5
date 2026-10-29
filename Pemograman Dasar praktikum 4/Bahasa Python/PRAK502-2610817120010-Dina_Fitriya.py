def hitung(nilai1, nilai2):
    difference = nilai1 - nilai2
    if difference < 0:
        difference = -difference
    return difference


def mutlak(angka):
    if angka < 0:
        return -angka
    return angka


a, c, b, d = map(int, input().split())
Hasil = hitung(a, b) + hitung(c, d)
print(mutlak(Hasil))