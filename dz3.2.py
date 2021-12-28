# thesaurus_dict = {
#     'И': ['Иван', 'Илья'],
#     'М': ['Мария'],
#     'П': ['Петр']
# }
name_list = ('Иван', 'Илья', 'Мария', 'Петр', 'Тимофей')

# name_1 = thesaurus_list[0]
# print(name_1[:1])
def thesaurus(*args):
    letter_dict = {}
    for i in args:
        a = i[:1]
        # name_2 = ''.join(list(i))
        # if name == name_2[:1]:
        name_filter = list(filter(lambda el: el.startswith(a), args))
        letter_dict.setdefault(a, name_filter)
    return letter_dict
# print(list_name)
print(thesaurus('Иван', 'Мария', 'Гена', 'Илья', 'Тимофей', 'Петя', 'Галя'))


