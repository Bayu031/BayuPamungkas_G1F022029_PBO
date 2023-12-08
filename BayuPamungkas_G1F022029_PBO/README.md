<div align="center">

<a href="https://www.facebook.com/profile.php?id=100030246067484"><img src="https://img.shields.io/badge/Facebook-Follow%20Me-blue?style=flat&logo=facebook" alt="Facebook"></a>
<a href="https://instagram.com/bayu_pamungkas031?igshid=NzZlODBkYWE4Ng=="><img src="https://img.shields.io/badge/Instagram-Follow%20Me-orange?style=flat&logo=instagram" alt="Instagram"></a>

</div>

# _Tugas Pemrograman Berbasis Objek_

## 1. _Buatlah perulangan hingga 100 menggunakan Python_
program Python yang menggunakan perulangan while untuk mencetak angka dari 1 hingga 100. Ketika nilai angka adalah kelipatan 10, program mencetak nama "Bayu" tiga kali pada baris baru. Jika tidak, program mencetak nilai angka itu sendiri.

<div align="center">

![Alt text](image_no1.jpg)

</div>

#### Luaran

1
2
3
4
5
6
7
8
9
Bayu 
Bayu 
Bayu
11
12
13
14
15
16
17
18
19
Bayu 
Bayu 
Bayu
21
22
23
24
25
26
27
28
29
Bayu 
Bayu 
Bayu
31
32
33
34
35
36
37
38
39
Bayu 
Bayu 
Bayu
41
42
43
44
45
46
47
48
49
Bayu 
Bayu 
Bayu
51
52
53
54
55
56
57
58
59
Bayu 
Bayu 
Bayu
61
62
63
64
65
66
67
68
69
Bayu 
Bayu 
Bayu
71
72
73
74
75
76
77
78
79
Bayu 
Bayu 
Bayu
81
82
83
84
85
86
87
88
89
Bayu 
Bayu 
Bayu
91
92
93
94
95
96
97
98
99
Bayu 
Bayu 
Bayu

Table 1. Penjelasan Tiap Section Code Dari No 1
<div align="center">


| Code                        | Penjelasan                                                                                                                                                                                                                          |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `b = 1`                     | Inisialisasi variabel `b` dengan nilai awal 1. Variabel ini digunakan sebagai pengontrol perulangan `while`.                                                                                                                    |
| `while b <= 100:`           | Pernyataan `while` yang menjalankan blok kode di dalamnya selama kondisi `b <= 100` benar (True). Perulangan akan berlanjut selama nilai `b` kurang dari atau sama dengan 100.                               |
| `  if b % 10 == 0:`         | Blok `if`. Jika nilai `b` merupakan kelipatan 10 (diperiksa menggunakan `b % 10 == 0`), maka program akan mencetak string "Bayu" tiga kali dengan menggunakan `\n` untuk mencetak baris baru setelah setiap "Bayu".               |
| `    print("Bayu \nBayu \nBayu")` | Mencetak string "Bayu" tiga kali jika nilai `b` adalah kelipatan 10.                                                                                                                                                                  |
| `  else:`                   | Blok `else` yang terkait dengan blok `if`. Jika kondisi pada `if` tidak terpenuhi (nilai `b` bukan kelipatan 10), maka program akan mencetak nilai `b`.                                                                           |
| `    print(b)`              | Mencetak nilai `b` jika nilai `b` bukan kelipatan 10.                                                                                                                                                                              |
| `b += 1`                    | Menginkremen `b` dengan 1 setiap kali iterasi perulangan selesai. Penting untuk mencegah perulangan tak terbatas (infinite loop) dan memastikan bahwa suatu saat kondisi `while` tidak terpenuhi sehingga perulangan berhenti.   |

</div>

## 2. _Buatlah program bebas, dengan menerapkan if else pada :_
### a. _For Loops_
Program berikut adalah program sederhana yang menggunakan for loop untuk menghitung total nilai mata kuliah dan rata-rata nilai kelas. 

<div align="center">

![Alt text](for_loop.jpg)

</div>

### Luaran

<div align="center">

![Alt text](luaran_for.jpg)

</div>

Table 2. Penjelasan Tiap Section Code For Loops
<div align="center">

| Code                                      | Penjelasan                                                                                       |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `def hitung_total_nilai():`               | Mendefinisikan fungsi `hitung_total_nilai()`.                                                  |
| `jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))` | Meminta pengguna memasukkan jumlah mahasiswa dan menyimpannya dalam variabel `jumlah_mahasiswa`.|
| `total_nilai = 0`                          | Menginisialisasi variabel `total_nilai` sebagai 0 untuk menyimpan total nilai mahasiswa.          |
| `for mahasiswa in range(1, jumlah_mahasiswa + 1):` | Memulai `for loop` untuk mengiterasi melalui setiap mahasiswa dalam rentang 1 hingga `jumlah_mahasiswa + 1`.|
| `nilai = float(input(f"Masukkan nilai mahasiswa ke-{mahasiswa}: "))` | Meminta pengguna memasukkan nilai untuk mahasiswa ke-`mahasiswa` dan menyimpannya dalam variabel `nilai`.|
| `total_nilai += nilai`                     | Menambahkan nilai mahasiswa ke total nilai.                                                     |
| `rata_rata = total_nilai / jumlah_mahasiswa` | Menghitung rata-rata nilai dengan membagi total nilai dengan jumlah mahasiswa.                |
| `print(f"\nTotal nilai semua mahasiswa: {total_nilai}")` | Mencetak total nilai semua mahasiswa setelah keluar dari `for loop`.                     |
| `print(f"Rata-rata nilai mahasiswa: {rata_rata}")` | Mencetak rata-rata nilai mahasiswa.                                                           |
| `if rata_rata >= 70:`                     | Memulai blok `if` untuk memeriksa apakah rata-rata nilai PBO di atas atau sama dengan 70.     |
| `    print("Selamat! Rata-rata nilai PBO di atas 70.")` | Jika rata-rata nilai di atas atau sama dengan 70, cetak pesan selamat.                    |
| `else:`                                   | Blok `else` yang akan dieksekusi jika kondisi pada `if` tidak terpenuhi, yaitu rata-rata nilai PBO di bawah 70.|
| `    print("Perlu perbaikan! Rata-rata nilai PBO di bawah 70.")` | Cetak pesan bahwa perlu perbaikan karena rata-rata nilai PBO di bawah 70.             |
| `hitung_total_nilai()`                    | Pemanggilan fungsi untuk menjalankan program.                                                 |



</div>

### b. _While Loops_
Program berikut adalah program sederhana yang menggunakan while loop untuk menghitung total nilai mata kuliah PBO dan rata-rata nilai kelas. 


<div align="center">

![Alt text](while_loop.jpg)

</div>

#### Luaran

<div align="center">

![Alt text](luaran_while.jpg)

</div>

Table 3. Penjelasan Tiap Section Code While Loops
<div align="center">

| Code                                      | Penjelasan                                                                                      |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `def hitung_total_nilai_while():`          | Mendefinisikan fungsi `hitung_total_nilai_while()`.                                            |
| `jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))` | Meminta pengguna memasukkan jumlah mahasiswa dan menyimpannya dalam variabel `jumlah_mahasiswa`. |
| `total_nilai = 0`                          | Menginisialisasi variabel `total_nilai` sebagai 0 untuk menyimpan total nilai mahasiswa.         |
| `counter = 1`                              | Menginisialisasi variabel `counter` sebagai 1 untuk melacak nomor mahasiswa yang sedang diinput.|
| `while counter <= jumlah_mahasiswa:`      | Memulai `while loop` yang akan terus berjalan selama nilai `counter` kurang dari atau sama dengan `jumlah_mahasiswa`. |
| `nilai = float(input(f"Masukkan nilai mahasiswa ke-{counter}: "))` | Meminta pengguna memasukkan nilai untuk mahasiswa ke-`counter` dan menyimpannya dalam variabel `nilai`.|
| `total_nilai += nilai`                     | Menambahkan nilai mahasiswa ke total nilai.                                                    |
| `counter += 1`                             | Meningkatkan nilai `counter` untuk melacak mahasiswa berikutnya.                                |
| `rata_rata = total_nilai / jumlah_mahasiswa` | Menghitung rata-rata nilai dengan membagi total nilai dengan jumlah mahasiswa.               |
| `print(f"\nTotal nilai semua mahasiswa: {total_nilai}")` | Mencetak total nilai semua mahasiswa setelah keluar dari `while loop`.                    |
| `print(f"Rata-rata nilai mahasiswa: {rata_rata}")` | Mencetak rata-rata nilai mahasiswa.                                                          |
| `if rata_rata >= 70:`                     | Memulai blok `if` untuk memeriksa apakah rata-rata nilai kelas PBO di atas atau sama dengan 70.|
| `    print("Selamat! Rata-rata nilai PBO di atas 70.")` | Jika rata-rata nilai di atas atau sama dengan 70, cetak pesan selamat.                    |
| `else:`                                   | Blok `else` yang akan dieksekusi jika kondisi pada `if` tidak terpenuhi, yaitu rata-rata nilai PBO di bawah 70.|
| `    print("Perlu perbaikan! Rata-rata nilai PBO di bawah 70.")` | Cetak pesan bahwa perlu perbaikan karena rata-rata nilai PBO di bawah 70.                |
| `hitung_total_nilai_while()`               | Pemanggilan fungsi untuk menjalankan program.                                                |

</div>

## 3. _Buatlah sebuah variabel dengan tipe data array, kemudian tampilkan semua nilai dalam variabel tersebut menggunakan perulangan for_

<div align="center">

![Alt text](no3.jpg)

</div>

### Luaran

<div align="center">

![Alt text](luaran_no3.jpg)

</div>


Table 4. Penjelasan Tiap Section Code perulangan for menggunakan tipe data array

<div align="center">

| Code                       | Penjelasan                                                                                      |
| -------------------------- | ----------------------------------------------------------------------------------------------- |
| `array = [10, 20, 30, 40, 50]` | Variabel yang berisi list dengan beberapa nilai.                                                |
| `for value in array:`      | Pernyataan `for` yang akan mengiterasi melalui setiap nilai dalam list `array`.                |
| `    print(value)`         | Mencetak nilai `value` pada setiap iterasi.                                                    |

</div>
