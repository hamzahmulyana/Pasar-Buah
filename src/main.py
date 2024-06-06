print('Selamat Datang di Pasar Buah!')

#Definisikan stock buah
stockApel = 10
stockJeruk = 8
stockAnggur = 15

#Definisikan harga buah
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

#Minta input jumlah apel
while True:
    nApel = int(input("Masukan jumlah Apel: "))

    #Membandingkan antara permintaan dengan stock
    if nApel > stockApel:
        print(f'Jumlah terlalu banyak, stock tersisa {stockApel} buah')
        continue
    
    #Berhenti minta input, ketika permintaan terpenuhi
    break

#Minta input jumlah jeruk
while True:
    nJeruk = int(input("Masukan jumlah Jeruk: "))

    #Membandingkan antara permintaan dengan stock
    if nJeruk > stockJeruk:
        print(f'Jumlah terlalu banyak, stock tersisa {stockJeruk} buah')
        continue
    
    #Berhenti minta input, ketika permintaan terpenuhi
    break

#Minta input jumlah jeruk
while True:
    nAnggur = int(input("Masukan jumlah Anggur: "))

    #Membandingkan antara permintaan dengan stock
    if nAnggur > stockAnggur:
        print(f'Jumlah terlalu banyak, stock tersisa {stockAnggur} buah')
        continue
    
    #Berhenti minta input, ketika permintaan terpenuhi
    break

#Menghitung total harga perbuah
totalHargaApel = nApel * hargaApel
totalHargaJeruk = nJeruk * hargaJeruk
totalHargaAnggur = nAnggur * hargaAnggur

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
