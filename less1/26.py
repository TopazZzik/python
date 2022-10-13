# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
with open('text2.txt', 'r') as data:
    text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

str_code = encode_rle(text)
print(f'Сжатые данные из файла text2.txt: {text} => {str_code}')

with open('text3.txt', 'r') as data:
    text = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(text)
print(f'Восстановленные данные из файла text3.txt: {text} => {str_decode}')