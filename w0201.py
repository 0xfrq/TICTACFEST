


total = input("Masukkan jumlah destinasi: ")

def isdigit():
    if total.isdigit() == False:
        return False
    else:
        return True

while isdigit()== False:
    print("Input tidak valid. Silahkan masukkan input kembali.")
    total = input("Masukkan jumlah destinasi: ")

total = int(total)

destinasi = []
rating = [] 
for i in range(total):
    nama_destinasi = input(f"Masukkan nama destinasi ke-{i+1}: ")
    destinasi.append(nama_destinasi)
    jumlah_rating = int(input(f"Masukkan rating dari destinasi {nama_destinasi} (indeks dari 1-10): "))  
    if (jumlah_rating < 1) | (jumlah_rating > 10):
        print("Input tidak valid. Silahkan masukkan input kembali.")
        jumlah_rating = int(input(f"Masukkan rating dari destinasi {nama_destinasi} (indeks dari 1-10): "))  
    rating.append(jumlah_rating)

for i in range(total):
    if rating[i] == max(rating):
        print(f"Perjalanan paling mengesankan adalah ketika pergi ke {destinasi[i]}")

    
hasil = sum(rating) / total
print(f"Skala kebahagiaan Dek Depe adalah  {hasil:.2f}")

if (hasil >= 8) & (hasil <= 10):
    print("Dek Depe bahagia karena pengalamannya menyenangkan.")
elif hasil >= 5 and hasil < 8:
    print("Dek Depe senang karena pengalamannya cukup baik.")
elif hasil >= 1 and hasil < 5:
    print("Dek Depe sedih karena pengalamannya buruk.")
        

print("\n\nTerimakasih telah menggunakan Dek Depe Holiday Tracker!")