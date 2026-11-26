CREATE TABLE role_pengguna (
id_role SERIAL PRIMARY KEY,
nama_role VARCHAR(20)
);

CREATE TABLE pengguna(
id_pengguna SERIAL PRIMARY KEY,
nama_pengguna VARCHAR(100),
username VARCHAR(50) UNIQUE,
password_hash VARCHAR(255),
id_role INTEGER REFERENCES role_pengguna (id_role)
);

CREATE TABLE materi(
id_materi SERIAL PRIMARY KEY,
nama_materi VARCHAR(100),
status_aktif BOOLEAN DEFAULT TRUE
);

CREATE TABLE soal(
id_soal SERIAL PRIMARY KEY,
id_materi INTEGER REFERENCES materi(id_materi),
pertanyaan TEXT,
pilihan_a TEXT,
pilihan_b TEXT,
pilihan_c TEXT,
pilihan_d TEXT,
kunci_jawaban CHAR(1),
pembahasan TEXT,
status_aktif BOOLEAN DEFAULT TRUE
);

CREATE TABLE riwayat_latihan(
id_riwayat SERIAL PRIMARY KEY,
id_pengguna INTEGER REFERENCES pengguna(id_pengguna),
id_materi INTEGER REFERENCES materi(id_materi),
tanggal_pengerjaan TIMESTAMP,
jumlah_soal INTEGER,
jumlah_benar INTEGER,
jumlah_salah INTEGER,
nilai NUMERIC(5,2)
);

CREATE TABLE detail_latihan(
id_detail SERIAL PRIMARY KEY,
id_riwayat INTEGER REFERENCES riwayat_latihan(id_riwayat),
id_soal INTEGER REFERENCES soal(id_soal),
jawaban_pengguna CHAR(1),
status_jawaban BOOLEAN
);

iNSERT INTO role_pengguna (nama_role)
VALUES
('Admin'),
('Mahasiswa');

INSERT INTO materi (nama_materi)
VALUES
('Tipe Data dan Variabel'),
('Percabangan'),
('Perulangan');

INSERT INTO soal (
    id_materi,
    pertanyaan,
    pilihan_a,
    pilihan_b,
    pilihan_c,
    pilihan_d,
    kunci_jawaban,
    pembahasan)
VALUES
(1,
    'Apa fungsi variabel?',
    'Menghapus data',
    'Menyimpan data',
    'Mengulang program',
    'Menghentikan program',
    'B',
    'Variabel digunakan untuk menyimpan data.'),
	(1,
    'Manakah tipe data untuk teks?',
    'int',
    'float',
    'str',
    'bool',
    'C',
    'Tipe data str digunakan untuk menyimpan teks.'),
	(1,
    'Tipe data dari nilai 10 adalah?',
    'int',
    'str',
    'bool',
    'list',
    'A',
    'Angka bulat seperti 10 bertipe int.'),
	(2,
    'Apa fungsi pernyataan if?',
    'Mengulang perintah',
    'Memeriksa kondisi',
    'Menyimpan file',
    'Membuat komentar',
    'B',
    'If digunakan untuk memeriksa kondisi.'),
	(2,
    'Apa fungsi else?',
    'Menangani kondisi alternatif',
    'Mengulang data',
    'Membuat variabel',
    'Menghapus fungsi',
    'A',
    'Else dijalankan ketika kondisi sebelumnya tidak terpenuhi.'),
	(2,
    'Manakah operator perbandingan sama dengan?',
    '=',
    '!=',
    '==',
    '>=',
    'C',
    'Operator == digunakan untuk membandingkan kesamaan dua nilai.'),
	(3,
    'Apa fungsi perulangan for?',
    'Mengulang proses',
    'Menghapus variabel',
    'Menghentikan komputer',
    'Mengubah komentar',
    'A',
    'For digunakan untuk mengulang proses pada kumpulan data atau rentang.'),
	(3,
    'Perulangan while berjalan selama...',
    'Program tidak memiliki variabel',
    'Kondisi bernilai benar',
    'Semua data terhapus',
    'Tidak ada kondisi',
    'B',
    'While mengulang perintah selama kondisinya bernilai True.'),
	(3,
	'Apa fungsi break?',
	'Menghentikan perulangan',
	'Menambah angka',
	'Mencetak teks saja',
	'Membuat list',
	'A',
	'Break digunakan untuk menghentikan perulangan yang sedang berjalan.'
	);
	
SELECT
    s.id_soal,
    m.nama_materi,
    s.pertanyaan,
    s.kunci_jawaban,
    s.pembahasan
FROM soal s
JOIN materi m
ON s.id_materi = m.id_materi;

SELECT
    s.id_soal,
    m.nama_materi,
    s.pertanyaan
FROM soal s
JOIN materi m
ON s.id_materi = m.id_materi;

SELECT
    riwayat_latihan.id_riwayat,
    pengguna.nama_pengguna,
    materi.nama_materi,
    riwayat_latihan.nilai
FROM riwayat_latihan
JOIN pengguna
ON riwayat_latihan.id_pengguna = pengguna.id_pengguna
JOIN materi
ON riwayat_latihan.id_materi = materi.id_materi;

SELECT * FROM role_pengguna;
SELECT * FROM pengguna;
SELECT * FROM materi;
SELECT * FROM soal;
SELECT * FROM riwayat_latihan;
SELECT * FROM detail_latihan;