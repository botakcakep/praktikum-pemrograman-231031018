menu = {
    'Fried Chiken':15000,
    'Burger Queen':10000,
    'Rice Bowl':8000,
    'Jasmine Tea':5000,
    'Pepsi':5000
}
print('==================Daftar Menu==================')
for i in menu: 
    print('Daftar Menu : ',i,'\t Harga : ',menu[i])
print('Pembelian diatas Rp100.000,- mendapatkan diskon 15%')
print('===============================================')
beli = input('Pilih Menu : ')
jumlah = int(input('Jumlah Pesanan : '))
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar * 15/100
    total = bayar - diskon
else: 
    total = bayar 


print('================Detail Pembayaran==================')
print('Menu yang dipesan            : ',beli)
print('Jumlah yang dipesan          : ',jumlah)
print('Total biaya                  : ',bayar)
print('Total yang harus dibayar     : ',total)