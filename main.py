"""""
8.2 Дан одномерный массив из 100 положительных чисел от 1 до 5. Вывести на экран
количество повторений каждого из 5 чисел.
"""""
import random
import lab3_ex_8_2_module_

random_list = []
numbers_to_search = [1, 2, 3, 4, 5]

i = 0
while i < 100:
    random_list.append(random.randrange(1, 6))
    i = i+1

i = 0
startArray = ""
print("Start array")
while i < 100:
    if i > 0 and i % 10 == 0:
        startArray = startArray + str(random_list[i]) + ',' + '\n'
    else:
        startArray = startArray + str(random_list[i]) + ','
    i = i+1

print(startArray)

lab3_ex_8_2_module_.get_repeat_count(random_list, numbers_to_search)
