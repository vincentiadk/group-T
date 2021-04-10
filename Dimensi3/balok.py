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
    hasil = "Volume = " + str(getVolume(p, l, t)) + "\n" + "Luas Permukaan = " + str(getLuasPermukaan(p, l, t))
    return hasil