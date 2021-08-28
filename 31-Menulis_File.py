# users = open("30-files.txt", "w")

# # Cek apakah suatu file dapat dibaca atau tidak
# print(users.readable())
# # Cek apakah suatu file dapat ditulis atau tidak
# print(users.writable())
# users.close() 

users = open("30-files.txt", "a")

users.write("\nRiqza - 14 - Bandung")
users.close() 