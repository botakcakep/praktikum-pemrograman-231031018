database = {
    'user1': {'username': 'user1', 'password': 'pass1', 'role': 'leader'},
    'user2': {'username': 'user2', 'password': 'pass2', 'role': 'officer'},
    'user3': {'username': 'user3', 'password': 'pass3', 'role': 'member'},
}

def login():
    attempts = 3  
    while attempts > 0:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in database:
            if password == database[username]['password']:
                print("Login berhasil!")
                print(f"Selamat datang, {username} ({database[username]['role']})")
                return True
            else:
                attempts -= 1
                print(f"Password salah! Anda memiliki {attempts} percobaan lagi.")
        else:
            attempts -= 1
            print(f"Username '{username}' tidak ditemukan! Anda memiliki {attempts} percobaan lagi.")

    print("Anda telah melebihi batas percobaan login.")
    return False

login()
