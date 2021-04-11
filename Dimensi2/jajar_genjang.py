def getAttributes():
    return ["sisi alas", "sisi miring", "tinggi"]

def getLuas(a, t):
    luas = a * t
    return luas

def getKeliling(a, b):
    keliling = 2 * (a + b)
    return keliling

def getHasil(a, b, t):
    hasil = "Luas = " + str(getLuas(a, t)) + "\n" + "Keliling = " + str(getKeliling(a, b))
    return hasil

def checkError(nama, value) :
    if nama == "sisi alas"  :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else :
            return True
    elif nama == "sisi miring" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else : 
            return True
    elif nama == "tinggi" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else : 
            return True
