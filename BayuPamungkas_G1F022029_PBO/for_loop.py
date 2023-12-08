def hitung_total_nilai():
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    total_nilai = 0

    for mahasiswa in range(1, jumlah_mahasiswa + 1):
        nilai = float(input(f"Masukkan nilai mahasiswa ke-{mahasiswa}: "))
        total_nilai += nilai

    rata_rata = total_nilai / jumlah_mahasiswa

    print(f"\nTotal nilai semua mahasiswa: {total_nilai}")
    print(f"Rata-rata nilai mahasiswa: {rata_rata}")

    if rata_rata >= 70:
        print("Selamat! Rata-rata nilai PBO di atas 70.")
    else:
        print("Perlu perbaikan! Rata-rata nilai PBO di bawah 70.")

hitung_total_nilai()
