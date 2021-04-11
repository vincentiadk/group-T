def getAttributes():
    return ["jari-jari"]

def getVolume(r):
    volume = (22/7) * r ** 3 * 4 / 3
    return volume

def getLuasPermukaan(r):
    luas_permukaan = 4 * (22/7) * r ** 2
    return luas_permukaan

def getHasil(r):
    hasil = "Volume = " + str(getVolume(r)) + "\n" + "Luas Permukaan = " + str(getLuasPermukaan(r))
    return hasil

def checkError(nama, value) :
    if nama == "jari-jari"  :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else :
            return True
