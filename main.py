import re
def word_count(tupl):
    print('Длина текста составляет: ', len(tupl))
    
def average_word_length(tupl):
    all_words_len = 0
    for i in tupl:
        all_words_len += len(i)
    print('Средняя длина слова составляет: ', (all_words_len / len(tupl)))
    
def most_common_word(tupl):
    my_dict = dict.fromkeys(tupl, 0)
    my_set = set(tupl)
    for i in my_set:
        countt = tupl.count(i)
        my_dict[i] = countt
    word, count = max(my_dict.items(), key=lambda x: x[1])
    print(word)

    
data_type = int(input('Данные это файл .txt(для выбора введите 1) или введенный вами текст(для выбора введите 0): '))
print(data_type)

if data_type == 1:
    path =  input('Укажите путь: ')                                        # Пример:'D:/ProgrProjects/textAnalysis/text.txt'
    my_list = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = re.sub(r'\W+', ' ', line.lower())
            line = (line.strip())
            line = (line.split())
            for i in line:
                my_list.append(i)
    my_tuple = tuple(my_list)
    word_count(my_tuple)
    average_word_length(my_tuple)
    most_common_word(my_tuple)
elif data_type == 0:
    text = input('Напечатайте текст: ')
    text = text.split('.')
    my_list = []
    for i in text:
        words = re.sub(r'\W+', ' ', i.lower())
        words = words.split()
        for j in words:
            my_list.append(j)
    my_tuple = tuple(my_list)
    word_count(my_tuple)
    average_word_length(my_tuple)
    most_common_word(my_tuple)
else:
    print('Ошибка. Такого ключа не существует. Допустимы только значения 1 и 0. Запустите программу заново.')