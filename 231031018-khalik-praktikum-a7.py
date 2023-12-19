a = True
pw_benar = 'false'
percobaan = 3
while a: 
    inputan = input('masukkan password: ')
    if inputan == pw_benar:
        print('Login Sukses!!!!')
        a = False
    else:
        if percobaan == 0: 
            print('Maaf Anda dibanned')
            a = False
        else:
            print('Login Gagal!!!!', percobaan)
            percobaan -= 1 