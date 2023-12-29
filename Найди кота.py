n = int(input('Число строк'))
flag = False
for string in range(n):
    string = input('Введите строку')
    if 'Кот' in string or 'кот' in string:
        flag = True
if flag:
    print('МЯУ')
else:
    print('НЕТ')