from geom_exception import NilaiNolError, SegiError, SisiError

def getAttributes():
    return ['sisi']

def keliling(sisi):
    return 4*sisi

def luas(sisi):
    return sisi**2

def getHasil(sisi):
    while True:
        try:
            if sisi <= 0:
                raise NilaiNolError
            break
        except NilaiNolError:
            print("Sisi tidak boleh bernilai nol atau negatif.")
        except ValueError:
            print("Input harus berupa angka.")
        # Belum tau request input baru dimasukin di mana
    kel = keliling(sisi)
    l = luas(sisi)

    return "Luas = {:.2f} cm\u00b2\nKeliling = {:.2f} cm".format(l, kel)