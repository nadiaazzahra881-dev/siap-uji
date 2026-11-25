import psycopg2


def buka_koneksi():
    koneksi = psycopg2.connect(
        host="localhost",
        database="siapuji 2 sql",
        user="postgres",
        password="nara789",
        port="5432"
    )

    return koneksi

