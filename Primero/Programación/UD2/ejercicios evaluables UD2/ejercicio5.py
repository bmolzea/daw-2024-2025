def divisores(num: int):
    for i in range(1, num+1):
        if num % i == 0:
            print(i)

num = int(input("Inserta un número: "))
print("Los divisores son: ")
divisores(num)