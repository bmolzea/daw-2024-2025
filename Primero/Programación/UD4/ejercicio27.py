import random

nums = []
for _ in range(1000):
    nums.append(random.randint(1, 100))

n_mas_repetido = nums[0]
n_veces_mayor = nums.count(n_mas_repetido)

for n in nums:
    n_veces = nums.count(n)
    if n_veces > n_veces_mayor:
        n_veces_mayor = n_veces
        n_mas_repetido = n

print(f"El número más repetido es: {n_mas_repetido} y se repite {n_veces_mayor}")