def getAttributes():
    return ["jari-jari"]

def getLuas(r):
    luas = (22/7) * r ** 2
    return luas

def getKeliling(r):
    keliling = 2 * (22/7) * r
    return keliling

def getHasil(r):
    hasil = "Luas = " + str(getLuas(r)) + "\n" + "Keliling = " + str(getKeliling(r))
    return hasil

