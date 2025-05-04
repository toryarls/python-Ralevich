# упражнение 2 + доп задания  стр34
def mysum(start=0, *numbers):
    output = start
    for number in numbers:
        output += number
    return output

print (mysum (10, 20, 30, 40))

# упражнение 2  доп задание 2 стр34
def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print (average (10, 20, 30, 40))

# упражнение 2  доп задание 3 стр34

def word_lengths(words):
    if not words:
        return (0, 0, 0)

    lengths = [len(word) for word in words]
    min_length = min(lengths)
    max_length = max(lengths)
    average_length = sum(lengths) // len(lengths)

    return (min_length, max_length, average_length)

print(word_lengths(["hello", "world", "python"]))

# упражнение 2  доп задание 3 стр34

def sum_integers(objects):
    total = 0
    for obj in objects:
        try:
            total += int(obj)
        except (ValueError, TypeError):
            pass
    return total

print(sum_integers([1, 2, '3', 4.5, '5.6', 'seven', None]))