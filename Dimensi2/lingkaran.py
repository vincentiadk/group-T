def getAttributes():
    return ["jari-jari"]

def getLuas(r):
    luas = 3.14 * r ** 2
    return luas

def getKeliling(r):
    keliling = 2 * 3.14 * r
    return keliling

def getHasil(r):
    hasil = "Luas = " + str(getLuas(r)) + "\n" + "Keliling = " + str(getKeliling(r))
    return hasil

