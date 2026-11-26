
import hashlib
import secrets
from bantuan import garis, judul, jeda, ambil_data, jalankan, clear


# =====================================
# PASSWORD
# =====================================

def buat_hash(password):
    salt = secrets.token_hex(16)

    hasil = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100000
    )

    return salt + ":" + hasil.hex()


def periksa_password(password, password_hash):
    salt, hash_asli = password_hash.split(":")

    hasil = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100000
    )

    return hasil.hex() == hash_asli


# =====================================
# REGISTRASI MAHASISWA
# =====================================

def registrasi():
    while True:
        while True:
            clear()
            judul("REGISTRASI MAHASISWA")

            print("\nSilakan isi data berikut:\n")

            nama = input("Nama Lengkap : ").strip()

            if not nama:
                print("\nNama tidak boleh kosong.")
                jeda()
                return

            if not all(huruf.isalpha() or huruf == " " for huruf in nama):
                print("\nNama hanya boleh berisi huruf dan spasi.")
                jeda()
                return

            nama = nama.title()
            break

        pesan_error = ""

        while True:
            clear()
            judul("REGISTRASI MAHASISWA")

            print("\nSilakan isi data berikut:\n")
            print("Ketentuan Username:")
            print("- Diharuskan 4-20 karakter")
            print("- Mengandung minimal 1 huruf")
            print("- Menggunakan huruf, angka, dan underscore (_)")
            print("- Tidak boleh menggunakan spasi\n")

            print("Nama Lengkap :", nama)

            username = input("Username     : ").strip()

            if not username:
                pesan_error = "Username tidak boleh kosong."

            elif len(username) < 4 or len(username) > 20:
                pesan_error = "Username harus terdiri dari 4-20 karakter."

            elif not any(huruf.isalpha() for huruf in username):
                pesan_error = "Username harus mengandung minimal satu huruf."

            elif any(huruf.isspace() for huruf in username):
                pesan_error = "Username tidak boleh menggunakan spasi."

            elif not username.replace("_", "").isalnum():
                pesan_error = "Username hanya boleh berisi huruf, angka, dan underscore (_)."

            else:
                username_ada = ambil_data("""
                    SELECT id_pengguna
                    FROM pengguna
                    WHERE username = %s
                """, (username,))

                if len(username_ada) > 0:
                    pesan_error = "Username sudah digunakan."

                else:
                    break

            print("\n" + pesan_error)
            input("\nTekan ENTER untuk mencoba lagi...")

        while True:
            clear()
            judul("REGISTRASI MAHASISWA")

            print("\nSilakan isi data berikut:\n")
            print("Ketentuan Password:")
            print("- Terdiri dari 6-20 karakter")
            print("- Mengandung minimal 1 huruf besar (A-Z)")
            print("- Mengandung minimal 1 huruf kecil (a-z)")
            print("- Mengandung minimal 1 angka atau simbol")
            print("- Tidak boleh menggunakan spasi\n")

            print("Nama Lengkap :", nama)
            print("Username     :", username)

            password = input("Password     : ").strip()

            if not password:
                pesan_error = "Password tidak boleh kosong."

            elif len(password) < 6 or len(password) > 20:
                pesan_error = "Password harus terdiri dari 6-20 karakter."

            elif not any(huruf.isupper() for huruf in password):
                pesan_error = "Password harus mengandung minimal 1 huruf besar."

            elif not any(huruf.islower() for huruf in password):
                pesan_error = "Password harus mengandung minimal 1 huruf kecil."

            elif any(huruf.isspace() for huruf in password):
                pesan_error = "Password tidak boleh menggunakan spasi."

            elif not any(huruf.isdigit() or not huruf.isalnum() for huruf in password):
                pesan_error = "Password harus mengandung minimal 1 angka atau simbol."

            else:
                break

            print("\n" + pesan_error)
            input("\nTekan ENTER untuk mencoba lagi...")

        print()
        garis()
        print("[1] Daftar")
        print("[2] Kembali")

        pilih = input("\nPilih menu: ")

        if pilih == "1":
            role = ambil_data("""
                SELECT id_role
                FROM role_pengguna
                WHERE nama_role = 'Mahasiswa'
            """)

            if len(role) == 0:
                print("\nRole Mahasiswa belum tersedia.")
                jeda()
                return False

            password_hash = buat_hash(password)

            hasil = jalankan("""
                INSERT INTO pengguna
                (nama_pengguna, username, password_hash, id_role)
                VALUES (%s, %s, %s, %s)
            """, (nama, username, password_hash, role[0][0]))

            if hasil == 0:
                print("\nRegistrasi gagal. Data tidak berhasil disimpan.")
                jeda()
                return False

            print("\nRegistrasi berhasil!")
            input("\nTekan ENTER untuk melanjutkan ke login...")
            return True

        elif pilih == "2":
            return False

        else:
            print("\nPilihan tidak tersedia.")
            jeda()


# =====================================
# LOGIN
# =====================================

def login():
    clear()
    judul("LOGIN SIAPUJI")

    print("\nMasukkan data akun Anda:\n")

    username = input("Username : ")
    password = input("Password : ")

    print()
    garis()
    print("[1] Login")
    print("[2] Kembali")

    pilih = input("\nPilih menu: ")

    if pilih == "2":
        return None

    if pilih != "1":
        print("\nPilihan tidak tersedia.")
        jeda()
        return None

    data = ambil_data("""
        SELECT
            pengguna.id_pengguna,
            pengguna.nama_pengguna,
            pengguna.password_hash,
            role_pengguna.nama_role
        FROM pengguna
        JOIN role_pengguna
        ON pengguna.id_role = role_pengguna.id_role
        WHERE pengguna.username = %s
    """, (username,))

    if len(data) == 0:
        print("\nUsername tidak ditemukan.")
        jeda()
        return None

    if periksa_password(password, data[0][2]):
        print("\nLogin berhasil!")
        jeda()
        return (data[0][0], data[0][1], data[0][3])

    print("\nPassword salah.")
    jeda()
    return None
