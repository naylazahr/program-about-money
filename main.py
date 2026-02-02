saldo = 0
daftar_pemasukan = []
daftar_pengeluaran = []

def tambah_pemasukan():
    global saldo, daftar_pemasukan
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    saldo = saldo + jumlah
    daftar_pemasukan.append(jumlah)
    print(f"Pemasukan sebesar Rp{jumlah} berhasil ditambahkan!")

def tambah_pengeluaran():
    global saldo, daftar_pengeluaran
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if jumlah > saldo:
        print(f"Peringatan! Saldo tidak cukup. Saldo Anda: Rp{saldo}")
    else:
        saldo = saldo - jumlah
        daftar_pengeluaran.append(jumlah)
        print(f"Pengeluaran sebesar Rp{jumlah} berhasil dicatat!")

def lihat_saldo():
    print("=" * 30)
    print(f"Saldo Anda saat ini: Rp{saldo:,}")
    print("=" * 30)

def lihat_laporan():
    total_pemasukan = sum(daftar_pemasukan) if daftar_pemasukan else 0
    total_pengeluaran = sum(daftar_pengeluaran) if daftar_pengeluaran else 0
    
    print("\n" + "=" * 40)
    print("LAPORAN KEUANGAN UANG SAKU")
    print("=" * 40)
    print(f"Total Pemasukan: Rp{total_pemasukan:,}")
    print(f"Total Pengeluaran: Rp{total_pengeluaran:,}")
    print("-" * 40)
    print(f"Saldo Akhir: Rp{saldo:,}")
    print("=" * 40 + "\n")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat laporan")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        lihat_laporan()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")