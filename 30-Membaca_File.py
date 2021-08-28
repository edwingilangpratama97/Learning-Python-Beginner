users = open("30-files.txt", "r")

# Cara 1
# print(users.read())
# Cara 2
# print(users.readline())
# print(users.readline())
# Cara 3
index = 1
# Return List/Array
list_user = users.readlines()
for user in list_user:
    print(f"{index}-{user}")
    index += 1
users.close() 