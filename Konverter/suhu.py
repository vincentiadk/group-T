def getJenisKonverter():
    return "Termometer"

def getAttributes():
    return ["Celcius", "Fahrenheit", "Kelvin", "Reamur"]

def checkError(awal, akhir, n) :
    if awal == akhir :
        return "Jenis termometer tidak boleh sama-sama " + awal
    else :
        return True

def getHasil(awal, akhir, n):
    hasil = 0.0
    if awal == "Celcius" : 
        if akhir == "Fahrenheit" :
            hasil = n * (9 / 5 ) + 32
        elif akhir == "Kelvin" : 
            hasil = n + 273
        elif akhir == "Reamur" :
            hasil = n * (4 / 5)

    elif awal == "Fahrenheit" :
        if akhir == "Celcius" :
            hasil = (n - 32) * (5 / 9 )
        elif akhir == "Kelvin" : 
            hasil = (n - 32) * (5 / 9 ) + 273
        elif akhir == "Reamur" :
            hasil = (4 / 9) * (n - 32)

    elif awal == "Kelvin" : 
        if akhir == "Fahrenheit" :
            hasil = (n - 273) * (9 / 5 ) + 32
        elif akhir == "Celcius" : 
            hasil = n - 273
        elif akhir == "Reamur" :
            hasil = n - 273 * (4 / 5)

    elif awal == "Reamur" : 
        if akhir == "Fahrenheit" :
            hasil = n * (9 / 4 ) + 32
        elif akhir == "Celcius" : 
            hasil = n * (5 / 4) 
        elif akhir == "Kelvin" :
            hasil = n * (5 / 4) + 273

    return "Hasil konversi suhu " + str(n) + " " + awal +  " = " + str(hasil) + " " + akhir