import sys

def caesar(text, shift, mode='encode'):
    """Функция для кодирования или декодирования текста с помощью шифра Цезаря"""
    result = []
    for char in text:
        #Проверяем, является ли символ кириллицей
        if ('а' <= char <= 'я') or ('А' <= char <= 'Я'):
            raise ValueError("Скрипт пока не поддерживает ваш язык")
        #Для латинских букв
        if 'a' <= char <= 'z':
            base = ord('a')
            shifted = (ord(char) - base + (shift if mode == 'encode' else -shift)) % 26
            result.append(chr(shifted + base))
        elif 'A' <= char <= 'Z':
            base = ord('A')
            shifted = (ord(char) - base + (shift if mode == 'encode' else -shift)) % 26
            result.append(chr(shifted + base))
        else:
            #Оставляем другие символы без изменений
            result.append(char)

    return ''.join(result)

def main():
    #Проверяем количество аргументов
    if len(sys.argv) != 4:
        raise ValueError("Неверное количество аргументов")
    
    mode = sys.argv[1]
    text = sys.argv[2]
    
    #Проверяем корректность режима
    if mode not in ['encode', 'decode']:
        raise ValueError("Неверный режим. Используйте 'encode' или 'decode'")
    
    #Проверяем и преобразуем сдвиг
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise ValueError("Сдвиг должен быть целым числом")
    
    #Выполняем шифрование/дешифрование
    try:
        result = caesar(text, shift, mode)
        print(result)
    except ValueError as e:
        raise e

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)