import os

# Soalan Matematik Gurauan
print("Soalan: Berapa jawapan bagi 1 + 1?")
jawapan = input("Jawapan anda: ")

# Cek jawapan
if jawapan == "10":
    print("Betul! Anda genius! Sekarang komputer akan restart untuk meraikan kemenangan anda!")
else:
    print("Salah! Komputer akan restart untuk perbaiki otak anda. 😆")

# Restart PC (untuk Windows)
os.system("shutdown /r /t 5")  # /r = restart, /t 5 = tunggu 5 saat sebelum restart
