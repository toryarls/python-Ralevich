# 3 задание
def run_timing():
    """Просим пользователя несколько раз ввести числовые данные. Печатает среднее время и количество
запусков."""
    number_of_runs = 0
    total_time = 0.0

    while True:
        one_run = input('Введите время пробега 10 км (в минутах): ')
        if not one_run:
            break

        try:
            total_time += float(one_run)
            number_of_runs += 1
        except ValueError:
            print("Пожалуйста, введите допустимое число.")

    if number_of_runs > 0:
        average_time = total_time / number_of_runs
        print(f'Среднее время: {average_time:.2f} мин, для {number_of_runs} пробежек')
    else:
        print('Нет данных о пробежках.')


run_timing()