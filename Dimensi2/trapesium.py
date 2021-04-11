def getAttributes():
    return ["alas atas", "alas bawah", "tinggi"]

def getLuas(a, b, t):
    luas = (a + b) * t / 2
    return luas

def getKeliling(a, b, t):
    c = (((a-b) ** 2) + (t ** 2)) ** .5
    keliling = a + b + c + t
    return keliling

def getHasil(a, b, t):
    hasil = "Luas Trapesium = " + str(getLuas(a,b,t)) + "\n" + "Keliling Trapesium = " + str(getKeliling(a,b,t))
    return hasil

def checkError(nama, value) :
    if nama == "alas atas"  :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else :
            return True
    elif nama == "alas bawah" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else : 
            return True
    elif nama == "tinggi" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else : 
            return True