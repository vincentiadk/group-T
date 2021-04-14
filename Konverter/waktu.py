def getJenisKonverter():
    return "Satuan Waktu"

def getAttributes():
    return ["Hari", "Jam", "Menit", "Detik", "Mili Detik"]

def checkError(satuan, n) :
    return True

def getHasil(satuan, n) :
    hasil = {}
    if satuan == "Hari" :
        hasil = {
            "hari": n,
            "jam" : n * 24,
            "menit" : n * 60 * 24,
            "detik" : n * 60 * 60 * 24,
            "mili" : n * 60 * 60 * 1000 * 24
        }
    elif satuan == "Jam" :
        hasil = {
            "hari": n / 24,
            "jam" :  n,
            "menit" : n * 60,
            "detik" : n * 60 * 60,
            "mili" : n * 60 * 60 * 1000
        }
    elif satuan == "Menit" :
        hasil = {
            "hari": n / 60 / 24 ,
            "jam" : n / 60, 
            "menit" : n,
            "detik" : n * 60,
            "mili" : n * 60 * 1000
        }
    elif satuan == "Detik" :
        hasil = {
            "hari": n / 60 / 60 / 24 ,
            "jam" : n / 60 / 60,
            "menit" : n / 60,
            "detik" : n,
            "mili" : n * 1000
        }
    elif satuan == "Mili Detik" :
        hasil = {
            "hari": n / 1000 / 60 / 60 / 24 ,
            "jam" : n / 1000 / 60 / 60,
            "menit" : n / 1000 / 60,
            "detik" : n / 1000,
            "mili" : n
        }
    str_hasil = ""
    for key, value in hasil.items() :
        if not (key.upper() == satuan.upper()) :
            str_hasil += str(value) + " " + key + "\n"
    return "Hasil konversi waktu " + str(n) + " " + satuan + " :\n" + str_hasil