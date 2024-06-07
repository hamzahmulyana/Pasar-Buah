import mylib

print('Selamat Datang di Pasar Buah!')

#Definisikan stock buah
stockApel = 10
stockJeruk = 8
stockAnggur = 15

#Definisikan harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

#minta input jumlah buah dan hitung harga buah
nApel, totalHargaApel = mylib.inputBuah(nama='Apel', stock=stockApel, harga=hargaApel)
nJeruk, totalHargaJeruk = mylib.inputBuah(nama='Jeruk', stock=stockJeruk, harga=hargaJeruk)
nAnggur, totalHargaAnggur = mylib.inputBuah(nama='Anggur', stock=stockAnggur, harga=hargaAnggur)

#Menghitung total harga keseluruhan
totalHargaBelanja = totalHargaApel + totalHargaJeruk + totalHargaAnggur

#Tampilkan rincian belanja
print(f'''
Detail Belanja

Apel : {nApel} x {hargaApel} = {totalHargaApel}
Jeruk : {nJeruk} x {hargaJeruk} = {totalHargaJeruk}
Anggur : {nAnggur} x {hargaAnggur} = {totalHargaAnggur}

Total Harga : {totalHargaBelanja}

''')

#Proses pembayaran
while True:
    #Input jumlah uang
    bayar = int(input('Silahkan masukan uang anda: '))

    #Hitung selihih antara bayar dengan total
    selisih = totalHargaBelanja - bayar

    #Bandingkan antara uang dengan total harga
    if selisih > 0:
        print(f'Uang anda kurang sebesar Rp.{selisih}')
        continue
    else:
        print(f'''Terimakasih Uang kembalian anda sebesar Rp.{abs(selisih)}''')
        break
