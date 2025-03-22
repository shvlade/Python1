import random

random_numbers = [random.randint(1, 100) for _ in range(20)]
print(random_numbers)
chetn_chislo = [num for num  in random_numbers if num % 2 == 0]
print(chetn_chislo)
del_3 = [num for num in random_numbers if num % 3 == 0]
print(del_3)
sr_snach = [sum(random_numbers) // len(random_numbers)]
print(sr_snach)