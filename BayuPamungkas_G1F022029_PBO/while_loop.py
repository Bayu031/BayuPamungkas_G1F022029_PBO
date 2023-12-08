def hitung_total_nilai_while():
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    total_nilai = 0
    counter = 1

    while counter <= jumlah_mahasiswa:
        nilai = float(input(f"Masukkan nilai mahasiswa ke-{counter}: "))
        total_nilai += nilai
        counter += 1

    rata_rata = total_nilai / jumlah_mahasiswa

    print(f"\nTotal nilai semua mahasiswa: {total_nilai}")
    print(f"Rata-rata nilai mahasiswa: {rata_rata}")

    if rata_rata >= 70:
        print("Selamat! Rata-rata nilai PBO di atas 70.")
    else:
        print("Perlu perbaikan! Rata-rata nilai PBO di bawah 70.")

hitung_total_nilai_while()
