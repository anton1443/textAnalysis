import re # Модуль для работы с регулярными выражениями

def word_count(tupl): # Нахождение количества слов
    print('Длина текста составляет: ', len(tupl))
    
def average_word_length(tupl): # Нахождение средней длины слова
    all_words_len = 0
    for i in tupl:
        all_words_len += len(i)
    print('Средняя длина слова составляет: ', (all_words_len / len(tupl)))
    
def most_common_word(tupl): # Нахождение наиболее часто встречающегося слова
    my_dict = dict.fromkeys(tupl, 0)
    my_set = set(tupl)
    for i in my_set:
        countt = tupl.count(i)
        my_dict[i] = countt
    word, count = max(my_dict.items(), key=lambda x: x[1])
    print('Наиболее часто встречающееся слово: ', word)

    
data_type = int(input('Данные это файл .txt(для выбора введите 1) или введенный вами текст(для выбора введите 0): '))

if data_type == 1:
    path =  input('Укажите путь: ')                                        # Пример:'D:/ProgrProjects/textAnalysis/text.txt'
    my_list = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = re.sub(r'\W+', ' ', line.lower()) # Замена всех небуквенно-цифровых символов на пустую строку
            line = (line.strip()) # Удаление лишних пробелов
            line = (line.split()) # Раздление строки на слова
            for i in line:
                my_list.append(i)
    my_tuple = tuple(my_list)
    word_count(my_tuple)
    average_word_length(my_tuple)
    most_common_word(my_tuple)
elif data_type == 0:
    text = input('Напечатайте текст: ')
    text = text.split('.') # Раздление по точкам
    my_list = []
    for i in text:
        words = re.sub(r'\W+', ' ', i.lower()) # Замена всех небуквенно-цифровых символов на пустую строку
        words = words.split() # Удаление лишних пробелов
        for j in words:
            my_list.append(j)
    my_tuple = tuple(my_list)
    word_count(my_tuple)
    average_word_length(my_tuple)
    most_common_word(my_tuple)
else:
    print('Ошибка. Такого ключа не существует. Допустимы только значения 1 и 0. Запустите программу заново.')
