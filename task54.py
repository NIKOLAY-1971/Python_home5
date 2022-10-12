# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

source_text = 'qqqqaskkkkererekkkkrcccccmmnqq'
data = open('text.txt', 'w')
data.writelines(source_text)
data.close()
print('Исходный текст: \n', source_text)

def coding(text):
    numberElements = ''
    previousElement = ''
    count = 1
    for char in text:
        if char != previousElement:
            if previousElement:
                numberElements += str(count) + previousElement
            count = 1
            previousElement = char
        else:
            count += 1
    else:
        numberElements += str(count) + previousElement
    return numberElements

def decoding(code):
    decoder = ''
    count = ''
    for el in code:
        if el.isdigit():
            count += el
        else:
            decoder += el * int(count)
            count = ''
    return decoder

text = open('text.txt', 'r')

codingElem = coding(*text)
print('Закодированный текст: \n', codingElem)

decodingElem = decoding(codingElem)
print('Раскодированный текст: \n', decodingElem)
