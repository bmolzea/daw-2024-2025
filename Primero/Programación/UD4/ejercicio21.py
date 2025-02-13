nums = []

while True:
    n = int(input("Inserta un número"))

    if n == 0:
        break

    if len(nums) == 0:
        nums.append(n)
    else:
        insertado = False
        for i, e in enumerate(nums):
            if n < e:
                nums.insert(i, n)
                insertado = True
                break
        if not insertado:
            nums.append(n)
        

print(nums)