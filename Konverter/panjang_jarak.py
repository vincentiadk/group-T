def getJenisKonverter():
    return "Satuan"

def getAttributes():
    return ["KM", "HM", "DAM", "M", "DM", "CM", "MM"]

def checkError(awal, akhir, n) :
    if awal == akhir :
        return "Satuan tidak boleh sama-sama " + awal
    else :
        return True

def getHasil(awal, akhir, n):
    return ""
 