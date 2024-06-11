#Import lib
from tabulate import tabulate

#Fungsi memvalidasi inputan khusus string
def stringValidation(title):
    while True:
        teks = input(title)
        if teks.isalpha() == True:
            break
        else:
            print('Silahkan masukan hanya teks')
    return teks.capitalize()

#Fungsi memvalidasi inputan khusus integer
def integerValidation(title, minval=0, maxval=100):
    while True:
        num = input(title)
        try:
            num = int(num)
            if num >= minval and num <= maxval:
                break
            else:
                print('Angka yang anda masukan diluar rentang')
        except:
            print('Yang anda inputkan bilangan')
    return num

#Fungsi untuk menampilkan database dalam bentuk tabulasi
def show(database, header=['index', 'name', 'stock', 'price']):
    #Menampilkan data dalam format tabulasi
    print(tabulate(database, headers=header, tablefmt='grid'))

#Fungsi untuk menambah data pada database
def add(database):
    #Meminta input data buah baru
    name = stringValidation(title='Masukan Nama Buah: ')
    stock = integerValidation(
        title='Masukan Stock Buah: ',
        minval=0
    )
    price = integerValidation(
        title='Masukan Harga Buah: ',
        minval=0,
        maxval=100000
    )

    #Menambahkan data ke database
    for id, buah in enumerate(database):
        if name in buah:
            database[id] = [id, name, stock, price]
            break
    else:
        database.append([id+1, name, stock, price])

    #menampilkan database terupdate
    show(database)

#Fungsi untuk menghapus data pada database
def delete(database):
    #menampilkan database terbaru
    show(database)

    #meminta user input index yang akan dihapus
    idx = integerValidation(
        title='Masukan index buah yang ingin dihapus: ',
        maxval=len(database)
    )

    #melakukan proses penghapusan sesuai index
    for id in range(len(database)):
        if id == idx:
            del database[idx]
    else:
        print('Buah yang anda cari tidak ada')
    
    #memperbarui index
    for id, buah in enumerate(database):
        if id != buah[0]:
            database[id][0] = id

    #Menampilkan database terbaru
    show(database)

#Fungsi untuk membeli
def buy(database):
    #Menyalin database ke dalam penyimpanan sementara
    databaseTemp = database.copy()

    #Definisikan variabel untuk menyimpan belanjaan
    keranjang = []

    #Proses Pembelian
    reorder = None
    while reorder != 'No':
        #Menampikan database sementara
        show(databaseTemp)

        #Meminta input untuk indeks dan jumlah buah yang diinginkan
        id = integerValidation(
            title='Silahkan masukan indeks buah: ',
            minval=0,
            maxval=len(databaseTemp)-1
            )
        stock = integerValidation(
            title='Silahkan masukan jumlah buah: ',
            minval=0,
            maxval=databaseTemp[id][2]
            )
        
        #Menambahkan kedalam keranjang belanja
        keranjang.append([databaseTemp[id][1], stock, databaseTemp[id][3]])

        #Menampilkan keranjang belanja
        show(database=keranjang, header=['Nama', 'Qty', 'Harga'])

        #Melakukan konfirmasi reorder
        while True:
            status = stringValidation('Mau beli yang lain?: ').lower()
            if status in ['yes', 'y', 'ya']:
                reorder = 'Yes'
            elif status in ['no', 'n', 'tidak']:
                reorder = 'No'
            break

        #Update stock sementara
        databaseTemp[id][2] -= stock
    
    #Menghitung total harga
    total = 0
    for id, item in enumerate(keranjang):
        #Hitung total harga perbuah
        totalHargaBuah = item[1] * item[2]

        #Input total harga ke keranjang
        keranjang[id].append(totalHargaBuah)

        #Sum seluruh 
        total += totalHargaBuah
    
    #Menampilkan keranjang belanja
    show(database=keranjang, header=['Nama', 'Qty', 'Harga', 'Total Harga'])

    #Menampilkan total harga
    print(f'Uang yang harus anda bayarkan adalah Rp.{total}')
    
    #Proses Pembayaran
    pembayaran(total)

    #Update database
    database = databaseTemp.copy()

#Fungsi pembayaran
def pembayaran(totalHarga):
    #Proses pembayaran
    while True:
        #Input jumlah uang
        bayar = int(input('Silahkan masukan uang anda: '))

        #Hitung selihih antara bayar dengan total
        selisih = totalHarga - bayar

        #Bandingkan antara uang dengan total harga
        if selisih > 0:
            print(f'Uang anda kurang sebesar Rp.{selisih}')
            continue
        else:
            print(f'''Terimakasih Uang kembalian anda sebesar Rp.{abs(selisih)}''')
            break