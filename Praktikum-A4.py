nim = ['6','0','0','2','0','1','0','1','4']
# nim2 = '231031018'
print(nim[1:3])
# print(nim2[1:3])

# akses item
print(f'item index 0:{nim[0]}')
print(f'item index 4:{nim[4]}')
print(f'item index terakhir:{nim[len(nim)-1]}\n')


# akses indeks terakhir
print(f'item index terakhir:{nim[-1]}')
print(f'item index pertama:{nim[-len(nim)]}')
print(f'item index 6 [-3]:{nim[-3]}')
print(f'item index 4 [-5]:{nim[-5]}')
print(f'item index 7 [-2]:{nim[-2]}\n')

# akses indeks batas
print(f'item index 1,2,3......:\n{nim[1:]}')
print(f'item index 3,4,5......:\n{nim[3:]}')
print(f'item index 0,1,2......:\n{nim[:3]}')
print(f'item index 0,1,2,4......:\n{nim[:4]}')
print(f'item index semua:\n{nim[:]}')
print(f'item index [:8]:\n{nim[:-1]}')
print(f'item index [:6]:\n{nim[:-3]}\n')

# pengirisan 
print(f'item index 1,2:\n{nim[1:3]}')
print(f'item index 2,3,4:\n{nim[2:5]}')
print(f'item index kosong:\n{nim[3:3]}')
print(f'item index [8:8] kosong:\n{nim[-1:-1]}')
print(f'item index [1:8] kosong:\n{nim[1:-1]}')
print(f'item index [2:7] kosong:\n{nim[2:-2]}\n')

# latihan list
data = ['ABDUL KHALIK HARTONO',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

print(f'{data[0]} status Kuliah :{data[2]}')
print(f'Data terbesar nilai adalah :{max(nilai)}')
print(f'Data terkecil nilai adalah :{min(nilai)}')
print(f'Rata-rata nilai adalah :{sum(nilai)/len(nilai)}\n')

# latihan tuple
data = ['ABDUL KHALIK HARTONO',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

print(f'{data[0]} status Kuliah :{len(nilai)}')
print(f'Data terbesar nilai adalah :{max(nilai)}')
print(f'Data terkecil nilai adalah :{min(nilai)}')
print(f'Rata-rata nilai adalah :{sum(nilai)/len(nilai)}\n')

# latihan nested list
data1 = [['ABDUL KHALIK HARTONO',2023,'Aktif'],
        [90,89,93,97],
        [20,22], 
        ['S1-Reguler','Ganjil']]

matkul = ['cinta','pti','prog','agama','b.indo','sainster','pancasila','kaldas 1']
sks    = [2,3,3,2,2,3,2,3]
# Tugas tambahkan matkul dan sks kedalam data (di akhhir)
data1.append(matkul)
data1.append(sks)
# Mata kuliah 1: cinta dengan jumlah sks 2
print(f'Mata kuliah 1: {data1[4][0]} dengan jumlah sks {data1[5][0]}')
# Mata kuliah 2: pti dengan jumlah sks 3
print(f'Mata kuliah 2: {data1[4][1]} dengan jumlah sks {data1[5][1]}')
# Mata kuliah 3: prog dengan jumlah sks 3
print(f'Mata kuliah 3: {data1[4][2]} dengan jumlah sks {data1[5][2]}')
# Mata kuliah 4: agama dengan jumlah sks 2
print(f'Mata kuliah 4: {data1[4][3]} dengan jumlah sks {data1[5][3]}')
# Mata kuliah 5: agama dengan jumlah sks 2
print(f'Mata kuliah 5: {data1[4][4]} dengan jumlah sks {data1[5][4]}')
# Mata kuliah 6: agama dengan jumlah sks 3
print(f'Mata kuliah 6: {data1[4][5]} dengan jumlah sks {data1[5][5]}')
# Mata kuliah 7: agama dengan jumlah sks 2
print(f'Mata kuliah 7: {data1[4][6]} dengan jumlah sks {data1[5][6]}')
# Mata kuliah 8: agama dengan jumlah sks 3
print(f'Mata kuliah 8: {data1[4][7]} dengan jumlah sks {data1[5][7]}')

print(data1[0][0])
print(data1[-1][0])
print(data1[2][0:])

print(f'Program pendidikan {data1[0][0]}:{data1[3][0]}')
print(f'Angkatan : {data1[0][1]}-{data1[3][1]}')
print(f'Jumlah nilai {data1[0][0]} adalah : {len(data1)}')
print(f'Data terbesar {data1[0][0]} adalah : {max(data1[1])}')
print(f'Data terbesar {data1[0][0]} adalah : {min(data1[1])}')
print(f'Rata-rata nilai {data1[0][0]} adalah : {sum(data1[1])/len(data1[1])}')