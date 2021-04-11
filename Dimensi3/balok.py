def getAttributes():
    return ["panjang", "lebar", "tinggi"]

def getVolume(p, l, t):
    volume =  p * l * t
    return volume

def getLuasPermukaan(p, l, t):
    Lp1 = 2 * p * l
    Lp2 = 2 * l * t
    Lp3 = 2 * t * p
    luasPermukaan = Lp1 + Lp2 + Lp3
    return luasPermukaan

def getHasil(p, l, t):
    hasil = "Volume Balok = " + str(getVolume(p, l, t)) + "\n" + "Luas Permukaan Balok = " + str(getLuasPermukaan(p, l, t))
    return hasil

def checkError(nama, value) :
    if nama == "panjang"  :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else :
            return True
    elif nama == "lebar" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else : 
            return True

    elif nama == "tinggi" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else : 
            return True