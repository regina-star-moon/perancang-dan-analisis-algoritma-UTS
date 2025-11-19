n = 2
dict = {}
budget = int(input("Masukkan budget: "))

barang_terbeli = 0
total_biaya = 0


#input barang
for i in range(n):
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = int(input("Masukkan harga: "))
    dict[nama_barang] = harga_barang    
print("barang barang",dict)

list_barang = list(dict.items())

# sorting barang berdasarkan harga (ascending)
for i in range(len(list_barang)):
    for j in range(i+1,len(list_barang)):
        if list_barang[i][1] > list_barang[j][1]:
            temp = list_barang[i]
            list_barang[i] = list_barang[j]
            list_barang[j] = temp


# tampilan berbentuk tabel
print("Tampilan barang dalam tabel:\n")
for i in list_barang:
    print("barang :",i[0]," || harga :",i[1])


# PROSES GREEDY: AMBIL BARANG DARI YANG PALING MURAH
i = 0
while i < len(list_barang):

    nama = list_barang[i][0]
    harga = list_barang[i][1]

    # Jika cukup untuk membeli barang
    if harga <= budget:
        budget -= harga
        print(f"Ambil barang: {nama} | Sisa budget: {budget}")

        barang_terbeli += 1
        total_biaya += harga
        
        list_barang.pop(i)
        continue
    # Jika tidak cukup untuk membeli barang
    if budget == 0:
        print("Budget sudah habis.")
        pilih = input("Apakah mau menambah budget? (y/n): ").lower()

        if pilih == "y":
            budget = int(input("Masukkan budget baru: "))
        else:
            print("Terima kasih telah berbelanja!")
            break

    i += 1

print(f"Total barang terbeli : {barang_terbeli}")
print(f"Total biaya : {total_biaya}")
print(f"Sisa budget : {budget}")
