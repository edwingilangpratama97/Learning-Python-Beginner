# Spesifik Exception
try:
    level = int(input("Masukkan level   : "))
    level = level / 0
    print(level)
except ZeroDivisionError:
    print("Error tidak bisa dibagi 0")
except ValueError:
    print("Inputan anda bukan angka")

# General Exception
try:
    level = int(input("Masukkan level   : "))
    level = level / 0
    print(level)
except:
    print("Terjadi kesalahan")
