def getAttributes():
    return ["alas atas", "alas bawah", "tinggi"]

def getLuas(a, b, t):
    luas = (a + b) * t / 2
    return luas

def getKeliling(a, b, t):
    c = (((a-b) ** 2) + (t ** 2)) ** 1/2
    keliling = a + b + c + t
    return keliling

def getHasil(a, b, t):
    hasil = "Luas = " + str(getLuas(a,b,t)) + "\n" + "Keliling = " + str(getKeliling(a,b,t))
    return hasil