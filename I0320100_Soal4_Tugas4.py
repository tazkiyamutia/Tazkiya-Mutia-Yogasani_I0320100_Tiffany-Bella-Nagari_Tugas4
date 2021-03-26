# Soal 4 Tugas 4

usia = int(input('masukkan usia anda : ' ))
ket_lulus = input('masukkan keterangan kelulusan ujian kualifikasi (Y/T) : ')

if usia >= 21:
    if ket_lulus == 'Y':
        print('Anda dapat mendaftar di kursus')
    else:
        print('Anda tidak dapat mendaftar di kursus')
else:
    print('Anda tidak dapat mendaftar di kursus')
