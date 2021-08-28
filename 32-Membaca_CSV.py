import csv

users = open("32-files.csv", "r")

# return list
users_csv = csv.reader(users, delimiter = ",")

for user in users_csv:
    print(f"Name:{user[0]}. Umur:{user[1]}. Kota:{user[-1]}")

users.close()