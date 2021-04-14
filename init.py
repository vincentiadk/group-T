import main
import time

############## APLIKASI DIMULAI DI SINI ##########
main.initDb()
menu_ = True
    
while(menu_ == True):
    main.showMenu()
    try:
        menu_pilihan = int(input())
        if menu_pilihan == 1:
            main.showBangun()

        elif menu_pilihan == 2:
            main.showKonverter("suhu")

        elif menu_pilihan == 3:
            main.showKonverter("panjang dan jarak")

        elif menu_pilihan == 4:
            main.showKonverter("waktu")

        elif menu_pilihan == 5:
            main.showHistori()
            time.sleep(1)

        elif menu_pilihan == 6:
            main.delHistori()
            time.sleep(1)

        elif menu_pilihan == 7:
            menu_ = False
        else:
            print("Perintah yang Anda masukan salah, silakan coba kembali")
            continue
    except ValueError:
        print('Anda hanya diijinkan untuk melakukan input angka(integer)')
        print()
        time.sleep(1)