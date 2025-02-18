nums = input("Inserta números separados por ;").split(";")

for i in range(len(nums)):
    nums[i] = int(nums[i])

print(nums)

print(f"El número mayor es {max(nums)}")
print(f"El número menor es {min(nums)}")
suma = sum(nums)
print(f"La media es {suma}")
print(f"La media es {suma/len(nums)}")