total_belanja = 0
barang_list = []

def tampilkan_daftar_barang():
    if not barang_list:
        print("\nDaftar barang masih kosong.")
    else:
        print("\nDaftar Barang:")
        for barang in barang_list:
            print(f"{barang['jumlah']} x {barang['nama']} - Rp{barang['harga']:.2f}")

while True:
    print("\nMenu Kasir:")
    print("1. Tambah Barang")
    print("2. Lihat Daftar Barang")
    print("3. Selesai dan Bayar")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    if pilihan == '1':
        nama_barang = input("Masukkan nama barang: ")
        harga = float(input("Masukkan harga barang: "))
        jumlah = int(input("Masukkan jumlah barang: "))
        total_belanja += harga * jumlah
        barang_list.append({"nama": nama_barang, "harga": harga, "jumlah": jumlah})
        print(f"{jumlah} x {nama_barang} ditambahkan ke total.")
    elif pilihan == '2':
        tampilkan_daftar_barang()
    elif pilihan == '3':
        tampilkan_daftar_barang()
        diskon = total_belanja * 0.25
        total_setelah_diskon = total_belanja - diskon
        print(f"\nTotal sebelum diskon: Rp{total_belanja:.2f}")
        print(f"Diskon 25%: Rp{diskon:.2f}")
        print(f"Total yang harus dibayar: Rp{total_setelah_diskon:.2f}")
        uang = float(input("Masukkan uang pembayaran: "))
        if uang >= total_setelah_diskon:
            kembalian = uang - total_setelah_diskon
            print(f"Terima kasih! Kembalian Anda: Rp{kembalian:.2f}")
        else:
            print("Uang tidak cukup! Harap masukkan jumlah yang sesuai.")
        break
    elif pilihan == '3':
        total_belanja = 0
barang_list = []

def tampilkan_daftar_barang():
    if not barang_list:
        print("\nDaftar barang masih kosong.")
    else:
        print("\nDaftar Barang:")
        for barang in barang_list:
            print(f"{barang['jumlah']} x {barang['nama']} - Rp{barang['harga']:.2f}")

while True:
    print("\nMenu Kasir:")
    print("1. Tambah Barang")
    print("2. Lihat Daftar Barang")
    print("3. Selesai dan Bayar")
    print("4. keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    if pilihan == '1':
        nama_barang = input("Masukkan nama barang: ")
        harga = float(input("Masukkan harga barang: "))
        jumlah = int(input("Masukkan jumlah barang: "))
        total_belanja += harga * jumlah
        barang_list.append({"nama": nama_barang, "harga": harga, "jumlah": jumlah})
        print(f"{jumlah} x {nama_barang} ditambahkan ke total.")
    elif pilihan == '2':
        tampilkan_daftar_barang()
    elif pilihan == '3':
        tampilkan_daftar_barang()
        diskon = total_belanja * 0.25
        total_setelah_diskon = total_belanja - diskon
        print(f"\nTotal sebelum diskon: Rp{total_belanja:.2f}")
        print(f"Diskon 25%: Rp{diskon:.2f}")
        print(f"Total yang harus dibayar: Rp{total_setelah_diskon:.2f}")
        uang = float(input("Masukkan uang pembayaran: "))
        if uang >= total_setelah_diskon:
            kembalian = uang - total_setelah_diskon
            print(f"Terima kasih! Kembalian Anda: Rp{kembalian:.2f}")
        else:
            print("Uang tidak cukup! Harap masukkan jumlah yang sesuai.")
        break
    elif pilihan == '4':
        isContinue = input("apakah sudah selesai (y/n)?")
        if isContinue == "n":
            break
        print ('program selesai')
    else:
        print("Pilihan tidak valid, silakan pilih lagi.")

