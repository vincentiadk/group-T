Kalkulator Segala Ada ini berjalan pada command CLI dengan bahasa pemmrograman python 3.*

Aplikasi memiliki 4 jenis kalkulator utama untuk mengkonversi dan melakukan perhitungan sehari-hari seperti menghitung luas, volume, keliling, konversi suhu, panjang dan jarak serta waktu, yang terdiri dari 7 menu utama, yaitu :

1. Kalkulator bangun ruang dan bangun datar
2. Kalkulator suhu
3. Kalkulator panjang dan jarak
4. Kalkulator waktu
5. Histori kalkulator
6. Hapus histori kalkulator
7. Keluar Aplikasi

Setiap perhitungan Anda akan disimpan dalam histori kalkulator, dan Anda dapat melihat perhitungan yang telah Anda lakukan sebelumnya.

untuk menjalankan aplikasi buka command line Anda, arahkan ke dalam folder aplikasi ini, lalu ketik :
>> python init.py

Aplikasi ini bersifat modular, Anda dapat menambahkan fitur konversi dan perhitungan lainnya bila dibutuhkan. 
- Folder Konverter berisi modul-modul untuk melakukan konversi satuan ukuran seperti luas, panjang, dan waktu. 
- Dimensi2 merupakan folder untuk modul perhitungan bangun datar
- Dimensi3 merupakan folder untuk modul perhitungan bangun ruang.

import modul penghitungan konverter atau package lain yang Anda buat dalam main.py dan ubah menu utama aplikasi pada function showMenu()