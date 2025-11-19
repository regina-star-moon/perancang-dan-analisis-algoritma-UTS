harga = [int(input('masukkan harga barang :')) for x in range(4)]

budget = int(input('masukkan budget : '))
barang_terbeli = 0
total_biaya = 0

for j in range(len(harga)):
    for k in range(j + 1, len(harga)):
        if harga[j] > harga[k]:
            harga[j], harga[k] = harga[k], harga[j]

print(f"harga barang yang sudah di urutkan : {harga} \n")

# PROSES GREEDY: AMBIL BARANG DARI YANG PALING MURAH

for i in range(len(harga)):

    # Jika harga barang masih bisa dibeli sesuai budget
    if harga[i] <= budget:
        
        # Kurangi budget dengan harga barang
        budget -= harga[i]

        # Tampilkan barang yang diambil dan sisa uang
        print(f"ambil {harga[i]} sisa {budget}")

        # Tambah jumlah barang yang terbeli
        barang_terbeli += 1

        # Tambah total biaya yang dikeluarkan
        total_biaya += harga[i]

print(f"\nTotal barang terbeli : {barang_terbeli}")
print(f"Total biaya : {total_biaya}")
