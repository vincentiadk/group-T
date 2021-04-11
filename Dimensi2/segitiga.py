def getAttributes():
    return ["alas", "tinggi"]

def getLuas(alas, tinggi):
    luas = alas * tinggi / 2
    return luas

def getKeliling(alas, tinggi):
    sisi = ((alas ** 2) + (tinggi ** 2)) ** .5 
    sisiSama = (((alas/2) ** 2) + (tinggi ** 2)) ** .5   
    keliling1 = sisi + alas + tinggi
    keliling2 = (sisiSama * 2) + alas
    return [keliling1, keliling2]

def getHasil(alas, tinggi):
    keliling = getKeliling(alas,tinggi)
    hasil = "Luas Segitiga = " + str(getLuas(alas,tinggi)) + "\n" + "Keliling Segitiga Siku-siku = " + str(keliling[0]) +"\n" + "Keliling Segitiga Sama Sisi = " + str(keliling[1]) 
    return hasil