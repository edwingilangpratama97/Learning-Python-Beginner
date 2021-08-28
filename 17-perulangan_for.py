numbers = [1, 2, 3, 4, 5, 6, 7]

for item in numbers:
    print(item * 5)

for item in range(1, 10, 2):
    print(item)

for baris in range(5):
    for kolom in range(7):
        print('o', end = ' ')
    else:
        print('')

listKota = [
  'Jakarta', 'Surabaya', 'Makassar'
]

for kota in listKota:
    print(kota)
    
    listTempat = [
        'Taman', 'Lapangan', 'Mall'
    ]

    while listTempat:
        print('-->', listTempat.pop(0))

    # for tempat in listTempat:
    #     print('-->', tempat)