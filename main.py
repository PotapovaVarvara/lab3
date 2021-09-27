"""""
8.2 Дан одномерный массив из 100 положительных чисел от 1 до 5. Вывести на экран
количество повторений каждого из 5 чисел.
"""""
import random
import lab3_ex_8_2_module_

random_list = []
numbers_to_search = [5, 7, 6, 2, 4]

i = 0
while i < 100:
    random_list.append(random.randrange(1, 10))
    i = i+1

lab3_ex_8_2_module_.get_repeat_count(random_list, numbers_to_search)
