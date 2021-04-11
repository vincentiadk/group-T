def getAttributes():
    return ['panjang sisi']

def keliling(sisi):
    return 4*sisi

def luas(sisi):
    return sisi**2

def checkError(inputUsers, nama, value) :
    if nama == "panjang sisi"  :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else :
            return True
    
def getHasil(sisi):
    kel = keliling(sisi)
    l = luas(sisi)

    return "Luas = {:.2f} cm\u00b2\nKeliling = {:.2f} cm".format(l, kel)