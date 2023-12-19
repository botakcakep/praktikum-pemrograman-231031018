#Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
  if nilai<=1:
    return 1
  else:
    return nilai*faktorial(nilai-1)
nilai = int(input('Masukkan nilai: '))
#Program Utama
for i in range(nilai + 1):
    print('%2d ! = %d' % (i,faktorial(i)))