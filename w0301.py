import os #import beberapa utils yang ada pada os seperti cek ukuran file yang akan digunakan, dan cek keberadaan file

#nama file
filepath = "text14.txt"

#cek apakah file ada
if os.path.exists(filepath):
    #buka file input
    my_file = open(filepath, "r")

    #cek apakah ukuran file nya 0 byte (file ada tapi kosong)
    if os.path.getsize(filepath) == 0: 
        print("File input ada tapi kosong")
    else:
        #judul
        print(f'{"Nama Barang":<15} | {"Jumlah":>6} | {"Kembalian":>6} ')
        print("-"*36)

        #iterasi untuk setiap line yang ada pada file
        for line in my_file:
            #disini kita punya 3 data yang dipisahkan dengan spasi, yakni nama barang, uang total dan harga satuan, gunakan split untuk memisahkan ketiganya dengan identifier spasi
            split = line.split()
            #untuk memastikan data yang digunakan terdiri dari 3 bagian, selain itu maka baris itu akan di skip (extra security)
            if len(split) == 3:
                #karena sudah pasti 3 data dan blok data pasti sama, maka kita definisikan blok 1 sebagai nama barang, blok 2 sebagai harga 1 dan blok 3 sebagai harga 2. ketiganyya berada pada array split 
                name, price1, price2 = split
                price1int = int(price1) #ubah ke integer
                price2int = int(price2)
                jumlah = int(price1int/price2int) 
                kembalian = int(price1int-(jumlah*price2int))
                print(f"{name:<15} | {jumlah:>6} | {kembalian:>6}")
        print("Terimakasih telah berbelanja di XSD Mart!")

    my_file.close()

else:
    print("File tidak ditemukan")