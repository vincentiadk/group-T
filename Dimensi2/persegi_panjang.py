from geom_exception import SisiError, NilaiNolError

def getAttributes():
    return ['sisi panjang', 'sisi pendek']

def keliling(sisi_panjang, sisi_pendek):
    return 2*sisi_panjang + 2*sisi_pendek

def luas(sisi_panjang, sisi_pendek):
    return sisi_panjang*sisi_pendek

def getHasil(sisi_panjang, sisi_pendek):
    while True:
        try:
            if sisi_panjang <= 0:
                raise NilaiNolError
            if sisi_pendek <= 0:
                raise NilaiNolError
            if sisi_pendek > sisi_panjang:
                raise SisiError
            break
        except NilaiNolError:
            print("Nilai tidak boleh bernilai nol atau negatif.")
        except SisiError:
            print('Sisi pendek lebih besar daripada sisi panjang.'
        except ValueError:
            print("Input harus berupa angka.")
    # Belum tau request input baru dimasukin di mana

    kel = keliling(sisi_panjang, sisi_pendek)
    l = luas(sisi_panjang, sisi_pendek)

    return "Luas = {:.2f} cm\u00b2\nKeliling = {:.2f} cm".format(l, kel)
