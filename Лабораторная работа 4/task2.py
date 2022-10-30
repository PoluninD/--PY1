def get_count_char(str_):
    words_list = str_.lower().split()
    new_str = "".join(words_list)
    dict = {}
    for i in new_str:
        if i.isalpha() and  i in dict:
            dict[i] += 1
        elif i.isalpha() and i not in dict:
            dict[i] = 1
    return dict
def densit(Dict_): # Функция возвращаюшая %  - ое соотношение
    for i in Dict_:
        Dict_[i] = (Dict_[i] / sum(Dict_.values())) * 100
    return Dict_



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print (densit(get_count_char(main_str)))