a = True # Membuat variabel a dengan nilai true yang akan digunakan di perulangan while

while a: # Perulangan while dimulai
    pilih = input('Pilihan: ') # Membuat variabel input yang akan meminta input dari pengguna
    if pilih == 'ya':  # Membuat percabangan untuk mengecek inputan dari pengguna apakah berisi "ya"
        print('Selamat Datang') # penugasan 
    elif pilih == 'tidak': # Membuat percabangan untuk mengecek inputan dari pengguna apakah berisi "tidak"
        print('Smapai Jumpa') # penugasan
    else: # Membuat else 
        a = False # Membuat variabel bernila false untuk menghentikan program
