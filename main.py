# import library 2 dimensi
import Dimensi2.segitiga as segitiga
import Dimensi2.persegi as persegi
import Dimensi2.persegi_panjang as persegi_panjang
import Dimensi2.lingkaran as lingkaran
import Dimensi2.trapesium as trapesium
import Dimensi2.jajar_genjang as jajar_genjang
# import library 3 dimensi
import Dimensi3.kubus as kubus
import Dimensi3.limas as limas
import Dimensi3.prisma as prisma
import Dimensi3.bola as bola
import Dimensi3.tabung as tabung
import Dimensi3.balok as balok

# import library untuk konverter
import Konverter.suhu as suhu
import Konverter.waktu as waktu
import Konverter.panjang_jarak as panjang_jarak

import init_db
import time
import sqlite3

masterBangunRuang = []
masterBangunRuang.append([
    segitiga,
    persegi,
    persegi_panjang,
    lingkaran,
    trapesium,
    jajar_genjang
])
masterBangunRuang.append([
    kubus,
    limas,
    prisma,
    bola,
    tabung,
    balok
])
masterKonverter = [
    panjang_jarak,
    suhu,
    waktu
]


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def inputFloatAtribut(atribut):
    print("Masukkan " + atribut + " : ", end="")
    value = 0
    try:
        value = float(input())
    except ValueError:
        print("Input yang Anda masukkan salah, hanya menerima angka.")
        value = inputFloatAtribut(atribut)
    return value


def inputHistory(jenis1, jenis2):
    conn = get_db_connection()
    conn.execute('INSERT INTO histories (jenis_1, jenis_2) VALUES (?, ?)',
                 (jenis1, jenis2))
    conn.commit()
    conn.close()


def getHistory():
    conn = get_db_connection()
    histories = conn.execute(
        'SELECT * FROM histories ORDER BY created desc Limit 0, 10').fetchall()
    conn.close()
    return histories


def showHistori():
    exit = False
    while (exit != True):
        histories = getHistory()
        print()
        print("Berikut ini 10 histori terkini penggunaan kalkulator Anda :")
        if len(histories) < 1:
            print('Belum ada histori penggunaan kalkulator')
        else:
            for his in histories:
                jenis_2 = his['jenis_2']
                if his['jenis_1'] == '2D':
                    if his['jenis_2'] == '1':
                        jenis_2 = 'Segitiga'
                    elif his['jenis_2'] == '2':
                        jenis_2 = 'Persegi'
                    elif his['jenis_2'] == '3':
                        jenis_2 = 'Persegi Panjang'
                    elif his['jenis_2'] == '4':
                        jenis_2 = 'Lingkaran'
                    elif his['jenis_2'] == '5':
                        jenis_2 = 'Trapesium'
                    else:
                        jenis_2 = 'Jajar Genjang'
                elif his['jenis_1'] == '3D':
                    if his['jenis_2'] == '1':
                        jenis_2 = 'Kubus'
                    elif his['jenis_2'] == '2':
                        jenis_2 = 'Limas Segi-n'
                    elif his['jenis_2'] == '3':
                        jenis_2 = 'Prisma Segi-n'
                    elif his['jenis_2'] == '4':
                        jenis_2 = 'Bola'
                    elif his['jenis_2'] == '5':
                        jenis_2 = 'Tabung'
                    else:
                        jenis_2 = 'Balok'
                print(str(his['id']) + '.', his['jenis_1'],
                      jenis_2, his['created'], sep=" ")
        exit = True


def delHistori():
    init_db.create_db()
    print('Data histori kalkulator sudah di reset')


def isSQLite3(filename):
    from os.path import isfile, getsize

    if not isfile(filename):
        return False
    if getsize(filename) < 100:  # SQLite database file header is 100 bytes
        return False

    with open(filename, 'rb') as fd:
        header = fd.read(100)
    # return header[:16] == 'SQLite format 3\x00'
    return True


def initDb():
    if isSQLite3('database.db') == False:
        init_db.create_db()
        print("Inisialisasi database ... ")
        time.sleep(1)
        print("Database telah siap ")
        time.sleep(1)


def showBangun():
    exit = False
    while (exit != True):
        # Memilih jenis dimensi
        print()
        print("Pilih jenis dimensi(2D/3D):", end='')
        jenisDimensi = input().upper()
        if(jenisDimensi == "2D"):
            print("\nBangunan 2D \n 1. Segitiga\n 2. Persegi\n 3. Persegi Panjang\n 4. Lingkaran\n 5. Trapesium\n 6. Jajar Genjang\nPilih nomor bangun ruang:", end=" ")
            bangunRuang = masterBangunRuang[0]
        elif(jenisDimensi == "3D"):
            print("\nBangunan 3D \n 1. Kubus\n 2. Limas Segi-n\n 3. Prisma Segi-n\n 4. Bola\n 5. Tabung\n 6. Balok \nPilih nomor bangun ruang:", end=" ")
            bangunRuang = masterBangunRuang[1]
        else:
            bangunRuang = []
            print("Perintah yang Anda masukan salah, silakan coba kembali")
            continue

        # Memilih Jenis bangun ruang
        isJenisRuang = False
        while(isJenisRuang != True):
            try:
                jenisBangunRuang = int(input())
                if(jenisBangunRuang >= 0 and jenisBangunRuang <= 6):
                    inputHistory(jenisDimensi, jenisBangunRuang)
                    isJenisRuang = True
                    bangunanTerpilih = bangunRuang[jenisBangunRuang-1]
                    atributeBangunan = bangunanTerpilih.getAttributes()
                    jumlahAtribut = len(atributeBangunan)
                    inputUsers = []
                    for atribut in atributeBangunan:
                        value = inputFloatAtribut(atribut)
                        input_ = bangunanTerpilih.checkError(
                            inputUsers, atribut, value)

                        while (input_ != True):
                            print(input_)
                            value = inputFloatAtribut(atribut)
                            input_ = bangunanTerpilih.checkError(
                                inputUsers, atribut, value)
                        inputUsers.append(value)

                    if(jumlahAtribut == 1):
                        print(bangunanTerpilih.getHasil(inputUsers[0]))
                    elif(jumlahAtribut == 2):
                        print(bangunanTerpilih.getHasil(
                            inputUsers[0], inputUsers[1]))
                    elif(jumlahAtribut == 3):
                        print(bangunanTerpilih.getHasil(
                            inputUsers[0], inputUsers[1], inputUsers[2]))
                    elif(jumlahAtribut == 4):
                        print(bangunanTerpilih.getHasil(
                            inputUsers[0], inputUsers[1], inputUsers[2], inputUsers[3]))

                    time.sleep(1)
                    print(
                        "Apakah Anda sudah selesai menggunakan kalkulator?(Y/N)", end=" ")
                    isSelesai = input().upper()
                    if(isSelesai == "Y"):
                        exit = True
                else:
                    print("Angka yang diijinkan hanya antara 1 - 6")
                    time.sleep(1)
                    print("Pilih nomor bangun ruang:")
            except ValueError:
                print('Anda hanya diijinkan untuk melakukan input angka(integer)')
                time.sleep(1)
                print('Pilih nomor bangun ruang:')


def showKonverter(nama):
    if nama == "panjang dan jarak jarak":
        konverterTerpilih = masterKonverter[0]
    elif nama == "suhu":
        konverterTerpilih = masterKonverter[1]
    else:
        konverterTerpilih = masterKonverter[2]

    jenis_konverter = konverterTerpilih.getJenisKonverter()
    satuan_konverter = konverterTerpilih.getAttributes()

    exitKonverter = False
    while (exitKonverter != True):
        exitSatuan = False
        satuan = ""
        n = 0
        while (exitSatuan != True):
            # Memilih tipe konverter awal
            print()
            print("Pilih satuan " + jenis_konverter + " awal : ")
            jmlSatuan = len(satuan_konverter)
            for i in range(len(satuan_konverter)):
                print("{}. {}".format(i + 1, satuan_konverter[i]))
            print("Masukan " + jenis_konverter +
                  " awal pilihan Anda : ", end='')
            try:
                satuanInt = int(input())
                if(satuanInt > 0) and (satuanInt <= jmlSatuan):
                    satuan = satuan_konverter[satuanInt - 1]
                    error = konverterTerpilih.checkError(satuan, n)
                    if error != True:
                        print(error)
                    else:
                        exitSatuan = True
                else:
                    print(
                        "Perintah yang Anda masukan salah, hanya masukan angka 1 sampai " + str(jmlSatuan), end="")

            except ValueError:
                print(
                    "Perintah yang Anda masukan salah, hanya masukan angka 1 sampai " + str(jmlSatuan), end="")

        # simpan histori konverter terpilih
        inputHistory(nama, satuan)
        exitNilai = False
        while (exitNilai != True) :
            try:
                print("Masukan nilai yang akan dikonversi : ", end='')
                n = float(input())
                error = konverterTerpilih.checkError(satuan, n)
                if error != True:
                    print(error)
                else:
                    exitNilai = True
            except ValueError:
                print("Hanya masukkan angka desimal atau integer.")


        print(konverterTerpilih.getHasil(satuan, n))

        print("Apakah Anda masih ingin menggunakan kalkulator " +
              nama + "? (Y/N)", end='')
        isSelesai = input().upper()
        if isSelesai == "N":
            exitKonverter = True


def showMenu():
    print()
    print("=================================== \n||   KALKULATOR SEGALA ADA     ||\n===================================")
    print("Pilih menu : ",
          "1. Kalkulator bangun ruang dan bangun datar",
          "2. Kalkulator suhu",
          "3. Kalkulator panjang dan jarak",
          "4. Kalkulator waktu",
          "5. Histori kalkulator",
          "6. Hapus histori kalkulator",
          "7. Keluar Aplikasi",
          sep="\n")
    print("Masukan menu pilihan Anda : ", end='')