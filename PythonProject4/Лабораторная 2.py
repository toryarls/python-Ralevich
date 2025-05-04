#вариант 1
# Для каждой строки из файла считывается GC состав и
# выбирается наибольший из них. Результат выводится в
# отдельный файл OUTТ.txt

input_file_path = "IN 1.txt"
output_file_path = "OUTТ.txt"

with open(input_file_path) as f: 
    data = f.readlines()

max_gc_freq = [-1, None]

for i in range(len(data)):
    if i == 0: # Если первая строка заголовок последовательности
        cur_struct = data[0][1:].strip() # Сохраняем название последовательности
        gc_num = 0
        struct_len = 0
        continue

    line = data[i].strip() # Убираем пробелы и переносы строк

    if line[0] == ">":
        gc_freq = gc_num / struct_len * 100

        if gc_freq > max_gc_freq[0]:
            max_gc_freq[0] = gc_freq
            max_gc_freq[1] = cur_struct

        cur_struct = line[1:] # Запоминаем название новой последовательности
        gc_num = 0
        struct_len = 0

    else:
        gc_num += line.count("G") + line.count("C")
        struct_len += len(line)

gc_freq = gc_num / struct_len * 100

if gc_freq > max_gc_freq[0]:
        max_gc_freq[0] = gc_freq
        max_gc_freq[1] = cur_struct

with open(output_file_path, "w") as f:
    f.write(max_gc_freq[1] + "\n")
    f.write(str(max_gc_freq[0]))

