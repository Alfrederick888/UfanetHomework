"""Алгоритм Лемпеля-Зива-Вэлча"""

"""Функция архиватор"""


def compress(text: str) -> str:
    # Инициализация словаря символами ASCII
    dictionary = {chr(i): i for i in range(256)}
    # Следующий доступный код
    current_code = 256
    # Результат сжатия данных
    result = []
    # Текущая последовательность символов
    current_sequence = ""

    # Итерируем исходный текст
    for symbol in text:
        new_sequence = current_sequence + symbol

        # Проверяем, есть ли новая последовательность в словаре
        if new_sequence in dictionary:
            # Если есть, присваиваем значение для текущей последовательности
            current_sequence = new_sequence
        else:
            # Иначе добавляем код текущей последовательности в результат
            result.append(dictionary[current_sequence])
            # Добавляем новую последовательность в словарь
            dictionary[new_sequence] = current_code
            current_code += 1
            current_sequence = symbol

    # Добавляем код последней последовательности в результат
    if current_sequence:
        result.append(dictionary[current_sequence])
    # Возвращаем результат в виде строки
    return ' '.join(map(str, result))


"""Функция разархивирования"""


def decompress(text: str) -> str:
    # Преобразуем текст в список
    text = list(map(int, text.split()))
    # Инициализация словаря символами ASCII
    dictionary = {i: chr(i) for i in range(256)}
    # Следующий доступный код
    current_code = 256
    # Первый символ в распакованной последовательности
    previous_sequence = chr(text[0])
    # Добавляем первый символ в результирующий список
    result = list(previous_sequence)

    # Итерируем заархивированные входные данные
    for code in text[1:]:
        if code in dictionary:
            current_sequence = dictionary[code]
        elif code == current_code:
            current_sequence = previous_sequence + previous_sequence[0]
        else:
            raise ValueError("Некорректные данные сжатия LZW")

        # Добавляем текущую последовательность к результату
        result.append(current_sequence)

        # Обновляем словарь
        dictionary[current_code] = previous_sequence + current_sequence[0]
        current_code += 1
        previous_sequence = current_sequence

    # Возвращаем результат в виде строки
    return ''.join(result)
