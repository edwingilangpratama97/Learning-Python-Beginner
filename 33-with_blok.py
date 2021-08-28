import csv

# Penggunaan with dipakai untuk : 
# 1. Lupa Close File
# 2. Ada error / crash setelah berhasil open file
with open("32-files.csv", "r") as users:
    users_csv = csv.reader(users, delimiter = ",")

    for user in users_csv:
        print(f"Name:{user[0]}. Umur:{user[1]}. Kota:{user[-1]}")
