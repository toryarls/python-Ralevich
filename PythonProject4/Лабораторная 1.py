# вариант 3
# На вход подаются эталонная постледовательность из консоли
# и текстовый файл с последовательностями, которые сравниваются
# с эталонной. Результат зааписывается в отдельный текстовый файл,
# где каждой строчке соответствует результат сравнения эталонной
# последовательности со строкой, находящейся на строчке с таким же номером
# IN.txt файл с разными последовательностями

input_file_path = "IN.txt"
output_file_path = "OUT.txt"

with open(input_file_path) as f:
    data = f.readlines()

standart_line = input()

with open(output_file_path, "w") as f: 
    for line in data:
        hamming_dist = 0 
        line = line.strip() # Убираем значение \n в конце последовательности
        for i in range(len(line)):
            if line[i] != standart_line[i]: 
                hamming_dist += 1

        f.write(str(hamming_dist) + "\n") # Записываем результат и переходим на новую строку
  # CATCGTAATGACGGCCT