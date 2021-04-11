def getAttributes():
    return ['sisi panjang', 'sisi pendek']

def keliling(sisi_panjang, sisi_pendek):
    return 2*sisi_panjang + 2*sisi_pendek

def luas(sisi_panjang, sisi_pendek):
    return sisi_panjang*sisi_pendek

def checkError(nama, value) :
    if nama == "sisi panjang"  :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else :
            return True
    elif nama == "sisi pendek" :
        if value <= 0 :
            return nama + " tidak boleh kurang dari atau sama dengan 0"
        else : 
            return True
    # elif nama == "sisi pendek" :
    #     if value <= inputUsers[-1] :
    #         return nama + " tidak boleh lebih besar atau sama dengan sisi panjang."
    #     else : 
    #         return True

def getHasil(sisi_panjang, sisi_pendek):
    kel = keliling(sisi_panjang, sisi_pendek)
    l = luas(sisi_panjang, sisi_pendek)

    return "Luas = {:.2f} cm\u00b2\nKeliling = {:.2f} cm".format(l, kel)
