def getAttributes():
    return ['panjang', 'lebar']

def keliling(sisi_panjang, sisi_pendek):
    return 2*sisi_panjang + 2*sisi_pendek

def luas(sisi_panjang, sisi_pendek):
    return sisi_panjang*sisi_pendek

def checkError(inputUsers, nama, value) :
    if nama == "panjang"  :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else :
            return True
    # elif nama == "lebar" :
    #     if value <= 0 :
    #         return nama + " tidak boleh kurang dari atau sama dengan 0"
    #     else : 
    #         return True
    elif nama == "lebar" :
        if value >= inputUsers[0] :
            return nama + " tidak boleh lebih besar atau sama dengan panjang."
        else : 
            return True

def getHasil(sisi_panjang, sisi_pendek):
    kel = keliling(sisi_panjang, sisi_pendek)
    l = luas(sisi_panjang, sisi_pendek)

    return "Luas = {:.2f} cm\u00b2\nKeliling = {:.2f} cm".format(l, kel)
