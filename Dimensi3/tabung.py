def getAttributes():
    return ["jari-jari", "tinggi"]

def getVolume(r, t):
    volume = 3.14 * r ** 2 * t
    return volume

def getLuasPermukaan(r, t):
    luas_permukaan = 2 * 3.14 * r * (r + t)
    return luas_permukaan

def getHasil(r, t):
    hasil = "Volume = " + str(getVolume(r, t)) + "\n" + "Luas Permukaan =" + str(getLuasPermukaan(r, t))
    return hasil
