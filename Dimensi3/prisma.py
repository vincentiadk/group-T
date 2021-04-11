import math

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

def checkError(nama, value) :
    if nama == "jumlah sisi"  :
        if value < 3 :
            return nama + " tidak boleh kurang dari tiga."
        else :
            return True
    elif nama == "panjang sisi" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0."
        else : 
            return True
    elif nama == "tinggi" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0."
        else : 
            return True

def getHasil(n, sisi, tinggi):
    l_permukaan = luas_permukaan(n, sisi, tinggi)
    vol = volume(n, sisi, tinggi)
    n = int(n)
    out = "\nLuas permukaan prisma segi-{0} beraturan = {1:.2f} cm\u00b2\nVolume prisma segi-{0} beraturan = {2:.2f} cm\u00b3"
    
    return out.format(n, l_permukaan, vol)