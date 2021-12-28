#
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []
from random import choice

def get_jokes(n, flag=True):
    for i in range(n):
        random_idx = choice(adverbs)
        random_idx_2 = choice(adjectives)
        random_idx_3 = choice(nouns)
        result = f"{random_idx} {random_idx_2}  {random_idx_3}"
        print(result)
        list_2 = []
        if flag == True:
            list_2 = result.split()
            for noun in nouns:
                for fun in list_2:
                    if noun == fun:
                        nouns.remove(noun)

            for adverb in adverbs:
                for fun in list_2:
                    if adverb == fun:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for fun in list_2:
                    if adjective == fun:
                        adjectives.remove(adjective)


get_jokes(2)

#
#
#     return result
# print(get_jokes(0))

# for nouns_1, adverbs_1, adjectives_1 in zip(nouns, adverbs, adjectives):



    # print(f'{nouns_1} {adverbs_1} {adjectives_1}')
