def getJenisKonverter():
    return "Satuan"

def getAttributes():
    return ["KM", "HM", "DAM", "M", "DM", "CM", "MM"]

def checkError(satuan, n) :
    return True

def getHasil(satuan, n):
    satuanInt = 0

    if satuan == "KM" : 
        satuanInt = 0
    elif satuan == "HM" : 
        satuanInt = 1
    elif satuan == "DAM" : 
        satuanInt = 2
    elif satuan == "M" : 
        satuanInt = 3
    elif satuan == "DM" : 
        satuanInt = 4
    elif satuan == "CM" : 
        satuanInt = 5
    elif satuan == "MM" : 
        satuanInt = 6

    str_hasil = ""
    for i in range(7):
        if satuanInt < i :
            hasil = n * (10 ** (i - satuanInt))
            str_hasil += str(hasil) + " " + getAttributes()[i] + "\n"
        elif satuanInt > i:
            hasil = n / (10 ** (satuanInt - i))
            str_hasil += str(hasil) + " " + getAttributes()[i] + "\n"
        else :
            pass

    return "Hasil konversi jarak " + str(n) + " " + satuan +  " :\n" + str_hasil