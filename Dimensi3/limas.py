import math

def getAttributes():
    return ['jumlah sisi', 'panjang sisi', 'panjang selimut']

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
    elif nama == "panjang selimut" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0."
        else : 
            return True
    # elif nama == "panjang selimut" :
    #     if value < inputUsers[-1] :
    #         return nama + " tidak boleh kurang dari panjang sisi."
    #     else : 
    #         return True

def getHasil(n, sisi, panjang_selimut):
    try:
        l_permukaan = luas_permukaan(n, sisi, panjang_selimut)
        vol = volume(n, sisi, panjang_selimut)
    except:
        return 'Error!! Panjang selimut lebih pendek daripada panjang sisi.'
    else:   
        n = int(n)
        out = "\nLuas permukaan prisma segi-{0} beraturan = {1:.2f} cm\u00b2\nVolume prisma segi-{0} beraturan = {2:.2f} cm\u00b3"
        
        return out.format(n, l_permukaan, vol)