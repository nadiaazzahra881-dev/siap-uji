import psycopg2


def buka_koneksi():
    koneksi = psycopg2.connect(
        host="localhost",
        database="siapuji2sql",
        user="postgres",
        password="nara789",
        port="5432"
    )

    return koneksi

