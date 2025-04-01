import math 

nama = input("Masukkan Nama : ")
n = float(input("Masukkan Panjang Sisi Persegi : "))
t = float(input("Masukkan Panjang Sisi Trapesium : "))
jml = int(input("Banyak Nametag : "))
set_lingkaran = (math.pi*float(float(n)/2) ** 2)/2
persegi = n * n
segitiga = (n * n) / 2
trapesium = (n + t) * n / 2
nametag = set_lingkaran + persegi + segitiga + trapesium
nametag_total = nametag * int(jml)
biaya = math.ceil((nametag_total * 0.40) / 1000) * 1000
print("Halo, ", nama , " Berikut adalah informasi lebih lanjut mengenai nametag yang akan kamu buat")
print(f"Luas 1 nametag: {nametag:.2f} cm^2")
print(f"Luas total nametag: {nametag_total:.2f} cm^2")
print("Uang yang diperlukan: Rp. ", biaya)
