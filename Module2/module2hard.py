import random

number_left = random.randint(3, 20)
print(number_left)

result = ''

for num_1 in range(1, 21):
    for num_2 in range(1, 21):
        if num_1 != num_2:
            if number_left % (num_1 + num_2) == 0:
                if num_1 < num_2:
                    result += str(num_1) + str(num_2)

print(result)





