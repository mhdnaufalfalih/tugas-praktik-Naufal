#input
tugas = float(input("nilai tugas: "))
uts = float(input("nilai uts: "))
uas = float(input("nilai uas: "))
kehadiran = float(input("kehadiran: "))

#proses
nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

#output
print("nilai akhir:", nilai_akhir)

#seleksi
if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    print ("status: LULUS DENGAN PREDIKAT")
elif nilai_akhir >= 75 and kehadiran >= 80:
    print("status: LULUS")
else:
    print("status: BELUM LULUS")
