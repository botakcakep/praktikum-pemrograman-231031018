print('Tugas Praktikum 3'.center(40))
nama = 'Abriel Yosua Nathanael Leskona'
nim  = '231031013'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi} \n''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


str1 = 'duFort Frankel Von Neumann'
print(str1, '\n')
up = str1.upper()
up = up.split()
print(up[3], up[0], up[1], up[2], '\n')
#output: NEUMANN DUFORT FRANKEL VON

str2 = 'duFort Frankel Von Neumann'
up = str2.upper()
up = up.split()
print(up[0][0]+up[1][0]+up[2][0], up[3], '\n')
#output: DFV NEUMANN

str3 = 'duFort Frankel Von Neumann'
up = str3.upper()
up = up.split()
print(up[0], up[1][0]+up[2][0]+up[3][0], '\n')
#output: DUFORT FVN

str4 = 'duFort Frankel Von Neumann'
up = str4.split()
print(up[3][0], up[0], up[1][0]+up[2][0], '\n')
#output: N duFort FV

str5 = 'duFort Frankel Von Neumann'
up = str5.split()
print(up[3].upper(), up[0][0], up[1][0].lower(), up[2][0].lower(), '\n')
#output: NEUMANN d f v

str6 = 'duFort Frankel Von Neumann'
up = str6.upper()
up = up.split()
print(up[3], up[0][0]+up[1][0]+up[2][0], '\n')
#output: NEUMANN DFV

str7 = '@duFort Frankel Von Neumann$'
up = str7.split()
print(up[0][1:], up[1], up[2], up[3][0:-1].upper(), '\n')
#output: duFort Frankel Von NEUMANN

str8 = '#duFort4Frankel4Von4Neumann$'
# sr = str8.strip('#$').replace('4', ' ')
# print(sr)
print(str8[1:-1].replace('4', ' '), '\n')
#output: duFort Frankel Von Neumann

str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
df = str9.replace('-', ' ')
df = df.split()
print(df[0].strip('@'), df[1].strip('^*'), df[2].strip('('), df[3].strip('($'), '\n')

#output: duFort Frankel Von Neumann

str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
rp = str10.replace('1', ' ')
rp = rp.split()
print(rp[0][1:3].lower()+rp[0][3:7], rp[1].strip('^*').title(), rp[2].strip('(').title(), rp[3].strip('(^').title())
#output: duFort Frankel Von Neumann