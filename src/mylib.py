#definisikan fungsi
def inputBuah(nama, stock, harga):
    """Fungsi meminta user untuk input jumlah buah
    dan menghitung harganya

    Args:
        nama (String)`: Nama buah yang akan dibeli
        stock (Integer)`: Stock buah yang akan dibeli
        harga (Integer)`: Harga buah per kilogram

    Returns:
        nBuah (Integer) : Jumlah buah yang dipesan
        hargaBuah (Integer): Total harga buah
    """
    while True:
        #minta input jumlah buah
        nBuah = int(input(f'Masukan jumlah {nama}: '))

        #Membandingkan antara permintaan dengan stock   
        if nBuah > stock:
            print(f'Jumlah terlalu banyak, stock tersisa {stock} buah')
            continue
    
        #Berhenti minta input, ketika permintaan terpenuhi
        break

    #Hitung harga untuk buah tersebut
    hargaBuah = nBuah * harga

    return nBuah, hargaBuah
