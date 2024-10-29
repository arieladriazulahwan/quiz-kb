
a = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
x = int(input("Masukkan nilai x: "))


if x in a:
    
    count = a.count(x)
    
    
    indices = [i for i, value in enumerate(a) if value == x]
    
    print(f"Nilai {x} muncul sebanyak {count} kali pada indeks {indices}.")
else:
    print(f"Nilai {x} tidak ada dalam list a.")
