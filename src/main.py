import mylib

daftarBuah = [
    [0, 'Apel', 20, 10000],
    [1, 'Jeruk', 15, 15000],
    [2, 'Anggur', 25, 25000]
]

def main():
    listMenu = '''
Selamat Datang di Pasar Buah!

List Menu:
1. Show
2. Add
3. Delete
4. Buy
5. Exit
'''
    while True:
        #menampilkan tampilan utama
        print(listMenu)
        
        #meminta input opsi yang akan dijalankan
        option = input("Masukan angka sesuai menu: ")

        #menjalankan function yang dijalankan
        if option == '1':
            mylib.show(daftarBuah)
        elif option == '2':
            mylib.add(daftarBuah)
        elif option == '3':
            mylib.delete(daftarBuah)
        elif option == '4':
            mylib.buy(daftarBuah)
        elif option == '5':
            break
        else:
            print('Input anda salah. Silahkan input ulang')

main()