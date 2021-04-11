import math
from geom_exception import NilaiNolError, SegiError, SisiError

def getAttributes():
    return ['jumlah sisi', ' panjang sisi', 'panjang_selimut']

def luas_alas(n, sisi):
    return 0.25 * n * sisi**2 * (1 / math.tan(math.pi/n))

def luas_permukaan(n, sisi, panjang_selimut):
    l_alas = luas_alas(n, sisi)
    # Luas segitiga dengan menggunakan rumus Heron
    semiperimeter = 0.5 * (sisi + panjang_selimut*2)
    l_segitiga = (semiperimeter * (semiperimeter - sisi)*(semiperimeter - panjang_selimut)**2) ** 0.5
    l_selimut = n * l_segitiga
    return l_alas + l_selimut

def volume(n, sisi, panjang_selimut):
    l_alas = luas_alas(n, sisi)
    r = math.sqrt((sisi**2) / (2 * (1 - math.cos(math.radians(360/n)))))
    tinggi = panjang_selimut * math.sin(math.acos(r/panjang_selimut))
    return (1/3) * l_alas * tinggi

def getHasil(n, sisi, panjang_selimut):
    while True:
        try:
            if n < 3:
                raise SegiError
            if sisi <= 0:
                raise NilaiNolError
            if panjang_selimut <= 0:
                raise NilaiNolError
            if panjang_selimut < sisi:
                raise SisiError
        except SegiError:
            print("Untuk membentuk bangun ruang, dibutuhkan minimal tiga sisi.")
        except NilaiNolError:
            print("Nilai tidak boleh negatif atau nol.")
        except SisiError:
            print("Panjang selimut tidak boleh lebih kecil daripada panjang sisi.")
        except ValueError:
            print("Input harus berupa angka.")
    # Belum tau request input baru dimasukin di mana
    l_permukaan = luas_permukaan(n, sisi, panjang_selimut)
    vol = volume(n, sisi, panjang_selimut)

    out = "\nLuas permukaan prisma segi-{0} beraturan = {1:.2f} cm\u00b2\nVolume prisma segi-{0} beraturan = {2:.2f} cm\u00b3"
    
    return out.format(n, l_permukaan, vol)