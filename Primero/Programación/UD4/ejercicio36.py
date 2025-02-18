"""
Crea un programa que lea números hasta que insertes un cero. A continuación te volverá a pedir un número n y mostrará los últimos n número introducidos. 
"""


nums = []
while True:
    n = int(input("Inserta un número: "))
    if n == 0:
        break
    else:
        nums.append(n)

n_ultimos = int(input("Cuantos números quieres mostrar? "))
nums.reverse()
print(f"Los últimos {n_ultimos} números son:")
for i in range(n_ultimos):
    print(nums[i])