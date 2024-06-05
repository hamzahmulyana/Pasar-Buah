#Minta input user
nApel = int(input("Masukan jumlah Apel: "))
nJeruk = int(input("Masukan jumlah Jeruk: "))
nAnggur = int(input("Masukan jumlah Anggur: "))

#Definisikan harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

#Menghitung total harga perbuah
totalHargaApel = nApel * hargaApel
totalHargaJeruk = nJeruk * hargaJeruk
totalHargaAnggur = nAnggur * hargaAnggur

#Menghitung total harga keseluruhan
totalHargaBelanja = totalHargaApel + totalHargaJeruk + totalHargaAnggur

#Tampilkan output
print(f'''
Detail Belanja

Apel : {nApel} x {hargaApel} = {totalHargaApel}
Jeruk : {nJeruk} x {hargaJeruk} = {totalHargaJeruk}
Anggur : {nAnggur} x {hargaAnggur} = {totalHargaAnggur}

Total Harga : {totalHargaBelanja}

''')