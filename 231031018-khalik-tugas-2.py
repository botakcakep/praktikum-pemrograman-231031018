# PROGRAM PENJUMLAHAN WAKTU
from datetime import datetime, timedelta

# Input waktu awal dalam format HH:MM:SS
waktu_awal = input("Masukkan waktu awal (HH:MM): ")

# Input durasi waktu yang akan ditambahkan dalam format HH:MM:SS
durasi = input("Masukkan durasi waktu (HH:MM): ")

# Parsing waktu awal dan durasi
try:
    waktu_awal_obj = datetime.strptime(waktu_awal, "%H:%M")
    durasi_obj = datetime.strptime(durasi, "%H:%M")
except ValueError:
    print("Format waktu tidak valid. Gunakan format HH:MM")
    exit()

# Menambahkan durasi ke waktu awal
waktu_hasil = waktu_awal_obj + timedelta(hours=durasi_obj.hour, minutes=durasi_obj.minute, seconds=durasi_obj.second)

# Cetak hasil
print("Waktu awal: ", waktu_awal_obj.time())
print("Durasi: ", durasi_obj.time())
print("Waktu hasil: ", waktu_hasil.time())

# PROGRAM SELISIH WAKTU

from datetime import datetime

# Input waktu pertama dalam format HH:MM:SS
waktu1_str = input("Masukkan waktu pertama (HH:MM): ")

# Input waktu kedua dalam format HH:MM:SS
waktu2_str = input("Masukkan waktu kedua (HH:MM): ")

# Parsing waktu pertama dan waktu kedua
try:
    waktu1 = datetime.strptime(waktu1_str, "%H:%M")
    waktu2 = datetime.strptime(waktu2_str, "%H:%M")
except ValueError:
    print("Format waktu tidak valid. Gunakan format HH:MM")
    exit()

# Menghitung selisih waktu
selisih_waktu = abs(waktu2 - waktu1)

# Cetak hasil
print("Waktu pertama: ", waktu1.time())
print("Waktu kedua: ", waktu2.time())
print("Selisih waktu: ", selisih_waktu)




