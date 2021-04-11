def getAttributes():
    return ["jari-jari"]

def getVolume(r):
    volume = (4/3) * 3.14 * r ** 3
    return volume

def getLuasPermukaan(r):
    luas_permukaan = 4 * 3.14 * r ** 2
    return luas_permukaan

def getHasil(r):
    hasil = "Volume = " + str(getVolume(r)) + "\n" + "Luas Permukaan = " + str(getLuasPermukaan(r))
    return hasil
