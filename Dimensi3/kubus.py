def getAttributes():
    return ["panjang sisi"]

def getVolume(sisi):
    volume =  sisi ** 3
    return volume

def getLuasPermukaan(sisi):
    luasPermukaan = 6 * (sisi * sisi)
    return luasPermukaan

def getHasil(sisi):
    hasil = "Volume Kubus = " + str(getVolume(sisi)) + "\n" + "Luas Permukaan Kubus = " + str(getLuasPermukaan(sisi))
    return hasil

def checkError(nama, value) :
    if nama == "panjang sisi"  :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else :
            return True
    else :
        return True