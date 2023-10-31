"""Тесты"""

import pytest
from algorithm import compress, decompress


# Тест функции архиватора
def test_compress():
    data = 'ABABABAACADADA'
    result = '65 66 256 258 65 67 65 68 262 65'
    compressed_data = compress(data)
    assert compressed_data == result


# Тест функции разархивирования
def test_decompress():
    data = '65 66 256 258 65 67 65 68 262 65'
    result = 'ABABABAACADADA'
    decompressed_data = decompress(data)
    assert decompressed_data == result


# Задачи
def test():
    test_compress()
    test_decompress()


if __name__ == '__main__':
    pytest.main([__file__])
