n = int (input("Masukkan Jumlah Suku (n): "))
a, b = 0, 1

if n <=0:
    print("Masukkan angka positif")

if n <=0:
    print("Masukkan angka positif")
kalau tidak:
    print("Deret Fibonacci: ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()   