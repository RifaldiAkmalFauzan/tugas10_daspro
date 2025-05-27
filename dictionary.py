# Soal 3 - Nilai minimum dari dictionary
penyanyi = {
    "Freddie Mercury,": 85,
    "Michael Jackson": 90,
    "Elvis Presley": 78,
    "Paul McCartney": 92,
    "Axl Rose": 88
}

print("Data nilai:", penyanyi)
nilai_terkecil = min(penyanyi.values())
print("Nilai minimum dari dictionary:", nilai_terkecil)

# Menampilkan siapa yang punya nilai minimum
nama_min = min(penyanyi, key=penyanyi.get)
print(f"Nilai minimum dimiliki oleh {nama_min}: {penyanyi[nama_min]}")