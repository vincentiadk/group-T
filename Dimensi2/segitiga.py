def getAttributes():
    return ["alas", "tinggi"]

def getLuas(alas, tinggi):
    luas = alas * tinggi / 2
    return luas

def getKeliling(alas, tinggi):
    sisi = ((alas ** 2) + (tinggi ** 2)) ** .5    
    keliling = sisi + alas + tinggi
    return keliling

def getHasil(alas, tinggi):
    hasil = "Luas = " + str(getLuas(alas,tinggi)) + "\n" + "Keliling = " + str(getKeliling(alas,tinggi))
    return hasil