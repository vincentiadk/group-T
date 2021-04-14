def getJenisKonverter():
    return "Termometer"


def getAttributes():
    return ["Celcius", "Fahrenheit", "Kelvin", "Reamur"]


def checkError(satuan, n):
    return True


def getHasil(satuan, n):
    hasil = {}
    if satuan == "Celcius":
        hasil = {
            "Fahrenheit": n * (9 / 5) + 32,
            "Kelvin": n + 273,
            "Reamur": n * (4 / 5)
        }

    elif satuan == "Fahrenheit":
        hasil = {
            "Celcius": (n - 32) * (5 / 9),
            "Kelvin": (n - 32) * (5 / 9) + 273,
            "Reamur": (4 / 9) * (n - 32)
        }

    elif satuan == "Kelvin":
        hasil = {
            "Fahrenheit": (n - 273) * (9 / 5) + 32,
            "Celcius": n - 273,
            "Reamur": n - 273 * (4 / 5)
        }

    elif satuan == "Reamur":
        hasil = {
            "Fahrenheit":  n * (9 / 4) + 32,
            "Celcius": n * (5 / 4),
            "Kelvin": n * (5 / 4) + 273
        }
    str_hasil = ""
    for key, value in hasil.items() :
        str_hasil += str(value) + " " + key + "\n"
    return "Hasil konversi suhu " + str(n) + " " + satuan + " :\n" + str_hasil