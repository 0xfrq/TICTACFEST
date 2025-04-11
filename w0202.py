print("Selamat datang di Bunker Hacker!")

total = int(input("Masukkan jumlah angka yang ingin dikonversi : "))

for i in range(total):
    user_input = int(input(f"Masukkn angka ke-{i+1} yang ingin dikonversikan (dalam desimal) : "))
    oc = user_input%8
    while user_input >= 8:
        user_input = user_input // 8
        oc = str(user_input%8) + str(oc)
    print(f"Hasil konversi desimal ke basis 8 adalah : {oc}")

print("Terimakasih telah menggunakan Bunker Hacker!")