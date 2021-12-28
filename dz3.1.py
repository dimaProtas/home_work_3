def num_translate(num):
    num_list = {'one': 'Один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                     'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                     'nine': 'девять', 'ten': 'десять'}
# for el in num_translate.keys():
#     print(el)
# num = input('Введите число словом: ')

    for key, value in num_list.items():
        if num == key:
             # print(value)
             return value
            # break
        # elif num != key:
        #     return None
print(num_translate('two'))