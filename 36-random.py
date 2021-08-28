import random

# Contoh 1
for index in range(5):
    # Range 10 - 30
    print(random.randint(10, 30))

# Contoh 2 Mutar-mutar / manual
users = ['Dada', 'Didi', 'Dudu', 'Dede']

batas_bawah = 0
batas_atas = len(users) - 1

random_int = random.randint(batas_bawah, batas_atas)
winner1 = users[random_int]
print(f"The winner is {winner1}")


# Contoh 2 Straight Forward / function
users = ['Dada', 'Didi', 'Dudu', 'Dede']

winner2 = random.choice(users)
print(f"The winner is {winner2}")