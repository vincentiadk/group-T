def getAttributes():
    return ["panjang sisi"]

def getVolume(sisi):
    volume =  sisi ** 3
    return volume

def getLuasPermukaan(sisi):
    luasPermukaan = 6 * (sisi * sisi)
    return luasPermukaan

def getHasil(sisi):
    hasil = "Volume = " + str(getVolume(sisi)) + "\n" + "Luas Permukaan = " + str(getLuasPermukaan(sisi))
    return hasil