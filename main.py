import psycopg2

from koneksi import buka_koneksi
from bantuan import garis, judul, jeda, clear, banner
from akun import registrasi, login
from riwayat import tampilkan_riwayat
from latihan import mulai_latihan, menu_admin, tampilkan_prioritas


# =====================================
# MENU MAHASISWA
# =====================================

def menu_mahasiswa(data_pengguna):
    id_pengguna = data_pengguna[0]
    nama = data_pengguna[1]

    while True:
        clear()
        judul("MENU MAHASISWA")

        print()
        print(f"Selamat Datang, {nama}!")
        print("\nSilakan pilih fitur yang ingin digunakan.\n")

        print("-" * 50)
        print("[1] Mulai Latihan")
        print("[2] Riwayat Latihan")
        print("[3] Prioritas Belajar")
        print("[4] Logout")
        print("-" * 50)

        pilih = input("\nPilih menu: ")

        if pilih == "1":
            mulai_latihan(id_pengguna)

        elif pilih == "2":
            tampilkan_riwayat(id_pengguna)

        elif pilih == "3":
            tampilkan_prioritas(id_pengguna)
            jeda()

        elif pilih == "4":
            print("\nApakah Anda yakin ingin logout?")
            print("[1] Ya")
            print("[2] Tidak")

            keluar = input("\nPilih menu: ")

            if keluar == "1":
                print("\nBerhasil logout.")
                break

        else:
            print("\nPilihan tidak tersedia.")
            jeda()


# =====================================
# MENU AWAL SIAPUJI
# =====================================

def menu_awal():
    while True:
        clear()
        banner()

        print("\n")
        print("Selamat Datang di SiapUji!")
        print("Silakan pilih menu yang tersedia.")

        print("\n" + "-" * 50)
        print("[1] Registrasi Mahasiswa")
        print("[2] Login")
        print("[3] Keluar")
        print("-" * 50)

        pilih = input("\nPilih menu: ")

        if pilih == "1":
            berhasil = registrasi()

            if berhasil:
                pengguna = login()

                if pengguna is not None:
                    if pengguna[2] == "Admin":
                        menu_admin()
                    elif pengguna[2] == "Mahasiswa":
                        menu_mahasiswa(pengguna)

        elif pilih == "2":
            pengguna = login()

            if pengguna is not None:
                if pengguna[2] == "Admin":
                    menu_admin()
                elif pengguna[2] == "Mahasiswa":
                    menu_mahasiswa(pengguna)

        elif pilih == "3":
            judul("SIAPUJI SELESAI")

            print("\nTerima kasih telah menggunakan SiapUji!")
            print("Semoga latihan yang dilakukan membantu")
            print("meningkatkan kesiapan ujian Anda.")

            garis()
            print("PROGRAM SELESAI")
            garis()
            break

        else:
            print("\nPilihan tidak tersedia.")
            jeda()


# =====================================
# MENJALANKAN PROGRAM
# =====================================

def main():
    try:
        koneksi = buka_koneksi()
        koneksi.close()

        print("Koneksi database berhasil!")

        menu_awal()

    except psycopg2.Error:
        print("Koneksi database gagal")


if __name__ == "__main__":
    main()
