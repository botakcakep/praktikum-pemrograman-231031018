nama = input('Masukkan nama karyawan: ')
pendapatan = int(input('Masukkan besaran pendapatan: '))
                 
print('Nama karyawan:', nama)
print('Pendapatan karyawan:', pendapatan)

if pendapatan > 1000:
    print('Status: Berhak')
else:
    print('Status: Tidak Berhak')

