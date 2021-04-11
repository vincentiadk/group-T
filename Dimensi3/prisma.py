import math
from geom_exception import NilaiNolError, SegiError, SisiError

def getAttributes():
    return ['jumlah sisi', 'panjang sisi', 'tinggi']

def luas_alas(n, sisi):
    alpha = math.pi/n
    return 0.25 * n * sisi**2 * (1 / math.tan(alpha))

def luas_permukaan(n, sisi, tinggi):
    l_alas = luas_alas(n, sisi)
    l_selimut = n * sisi * tinggi
    return 2*l_alas + l_selimut

def volume(n, sisi, tinggi):
    l_alas = luas_alas(n, sisi)
    return l_alas*tinggi

def getHasil(n, sisi, tinggi):
    while True:
        try:
            if n < 3:
                raise SegiError
            if sisi <= 0:
                raise NilaiNolError
            if tinggi <= 0:
                raise NilaiNolError
        except SegiError:
            print("Untuk membentuk bangun ruang, dibutuhkan minimal tiga sisi.")
        except NilaiNolError:
            print("Nilai tidak boleh negatif atau nol.")
        except ValueError:
            print("Input harus berupa angka.")
    # Belum tau request input baru dimasukin di mana

    
    l_permukaan = luas_permukaan(n, sisi, tinggi)
    vol = volume(n, sisi, tinggi)

    out = "\nLuas permukaan prisma segi-{0} beraturan = {1:.2f} cm\u00b2\nVolume prisma segi-{0} beraturan = {2:.2f} cm\u00b3"
    
    return out.format(n, l_permukaan, vol)