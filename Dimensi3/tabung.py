def getAttributes():
    return ["jari-jari", "tinggi"]

def getVolume(r, t):
    volume = (22/7) * r ** 2 * t
    return volume

def getLuasPermukaan(r, t):
    luas_permukaan = 2 * (22/7) * r * (r + t)
    return luas_permukaan

def getHasil(r, t):
    hasil = "Volume = " + str(getVolume(r, t)) + "\n" + "Luas Permukaan =" + str(getLuasPermukaan(r, t))
    return hasil

def checkError(nama, value) :
    if nama == "jari-jari"  :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else :
            return True
    elif nama == "tinggi" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else : 
            return True
