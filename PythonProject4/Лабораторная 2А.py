# вариант 1
# Для каждой строки из файла считывается GC состав
# (отношение количества всех G и C компонентов
# ко всей длине последовательности ) и выбирается 
# наибольший из них. Результат выводится в консоль.

input_file_path = "IN 1.txt"

with open(input_file_path) as f:
    data = f.readlines()

max_gc_freq = [-1, None] # Результат, первый элемент - GC состав  в процентах, второй - его название

for i in range(len(data)):
    if i == 0:
        cur_struct = data[0][1:].strip()
        gc_num = 0
        struct_len = 0
        continue

    line = data[i].strip()

    if line[0] == ">": 
        gc_freq = gc_num / struct_len * 100 # Вычисляем GC состав для предыдущей последовательности

        if gc_freq > max_gc_freq[0]:
            max_gc_freq[0] = gc_freq
            max_gc_freq[1] = cur_struct

        cur_struct = line[1:] # Название новой последовательности
        gc_num = 0
        struct_len = 0 

    else:
        gc_num += line.count("G") + line.count("C") 
        struct_len += len(line)

gc_freq = gc_num / struct_len * 100

if gc_freq > max_gc_freq[0]: 
        max_gc_freq[0] = gc_freq
        max_gc_freq[1] = cur_struct

print(max_gc_freq[1])
print(max_gc_freq[0])