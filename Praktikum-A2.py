print('praktikum-a2\n')
print()

print('NAMA   : ABDUL KHALIK HARTONO')
print('NIM    : 231031018')
print('PRODI  : Sistem Informasi-A\n')

# INI OPERATOR ASSIGMENT
a=19
print('Nilai a adalah',a)
a+=3
print('Nilai a+=3 adalah',a)

a=19
print('Nilai a adalah',a)
a-=3
print('Nilai a-=3 adalah',a)

a=19
print('Nilai a adalah',a)
a*=2
print('Nilai a*= adalah',a)

a=19
print('Nilai a adalah',a)
a/=2
print('Nilai a/= adalah',a)

a=3
print('Nilai a adalah',a)
a**=2
print('Nilai a**= adalah',a)

a=35
print('Nilai a adalah',a)
a%=32
print('Nilai a%= adalah',a)

a=35
print('Nilai a adalah',a)
a//=32
print('Nilai a//= adalah',a)

# TUGAS MELANJUTKAN UNTUK OPERATOR SELANJUTNYA LINE 25-LINE 59
# OR
b = True
print('Nilai b=',b)
b |= False
print('Nilai b|= False akan menjadi', b)
b = False
print('Nilai b =', b)
b |=False
print('Nilai b|= False akan menjadi', b)

#AND
b = True
print('Nilai b =', b)
b &= False
print('Nilai b&= False akan menjadi', b)
b = False
print('Nilai b =', b)
b &=False
print('Nilai b&= False akan menjadi', b)

#XOR
b = True
print('Nilai b =', b)
b ^= False
print('Nilai b^= False akan menjadi', b)
b = False
print('Nilai b =', b)
b ^=False
print('Nilai b^= False akan menjadi', b)

#SHIFTING
c = 0b0100
print('Nilai c =', format(c, '04b'))
c >>= 1
print('Nilai c >>=1 akan menjadi', format(c, '04b'))
c = 0b0100
c <<=1
print('Nilai c <<=1 akan menjadi', format(c, '04b'))

# OPERATOR PERBANDINGAN 
a=9
b=18
print('\n----------------- Besar dari 13')
hasil= a > 18
print(a,'> 18 adalah', hasil)
hasil= b > 18
print(b,'> 18 adalah', hasil)

print('\n----------------- Kecil dari 13')
hasil= a < 18
print(a,'< 18 adalah', hasil)
hasil= b < 18
print(b,'< 18 adalah', hasil)

# TUGAS 
print('\n------------ Besar atau sama dari 13 #ujung nim')
hasil = a >= 18
print(a, '>= 18 adalah', hasil)
hasil = b >= 18
print(b, '>= 18 adalah', hasil)

print('\n------------ Kecil atau sama dari 13 #ujung nim')
hasil = a <= 18
print(a, '<= 18 adalah', hasil)
hasil = b <= 18
print(b, '<= 18 adalah', hasil)

print('\n------------ Sama dari 13 #ujung nim')
hasil = a == 18
print(a, '== 18 adalah', hasil)
hasil = b == 18
print(b, '== 18 adalah', hasil)

print('\n------------ Tidak Sama dari 13 #ujung nim')
hasil = a != 18
print(a, '!= 18 adalah', hasil)
hasil = b != 18
print(b, '!= 18 adalah', hasil)


# OPERATOR LOGIKA
a= True
b= False
print('\n==========AND==========')
# hasil = a and b
# hasil = a and b 
# hasil = b and a
# hasil = b and b

hasil= a and a
print(a,'and',b,'hasilnya=',hasil)
hasil= a and b
print(a,'and',b,'hasilnya=',hasil)
hasil= b and a
print(a,'and',b,'hasilnya=',hasil)
hasil= b and b
print(a,'and',b,'hasilnya=',hasil)

print('\n==========XOR==========')
# hasil = a or b
# hasil = a or b 
# hasil = b or a
# hasil = b or b
hasil= a ^ a
print(a,'xor',b,'hasilnya=',hasil)
hasil= a ^ b
print(a,'xor',b,'hasilnya=',hasil)
hasil= b ^ a
print(a,'xor',b,'hasilnya=',hasil)
hasil= b ^ b
print(a,'xor',b,'hasilnya=',hasil)

print('\n==========NOT==========')
hasil= not a
print('not',a,'hasilnya =',hasil)
hasil= not b
print('not',b,'hasilnya =',hasil)

# OPERATOR MEMBERSHIP

print('\n=============================IN')
nama = 'khalik'
test = 'ai'
cek = test in nama 
print(test,'terdapat di',nama,'adalah',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'
cek = test1 in nama 
print(test1,'terdapat di',nama,'adalah',cek)
cek = test2 in nama 
print(test2,'terdapat di',nama,'adalah',cek)
cek = test3 in nama 
print(test3,'terdapat di',nama,'adalah',cek)
cek = test4 in nama 
print(test4,'terdapat di',nama,'adalah',cek)
cek = test5 in nama 
print(test5,'terdapat di',nama,'adalah',cek)

print('\n=============================NOT IN')
nama = 'khalik'
test = 'ai'
cek = test not in nama 
print(test,'tidak terdapat di',nama,'adalah',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'
cek = test1 not in nama 
print(test1,'tidak terdapat di',nama,'adalah',cek)
cek = test2 not in nama 
print(test2,'tidak terdapat di',nama,'adalah',cek)
cek = test3 not in nama 
print(test3,'tidak terdapat di',nama,'adalah',cek)
cek = test4 not in nama 
print(test4,'tidak terdapat di',nama,'adalah',cek)
cek = test5 not in nama 
print(test5,'tidak terdapat di',nama,'adalah',cek)

