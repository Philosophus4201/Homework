string_list = []
while True:
    string = input('Строка ')
    if string == 'стоп':
        break
    string_list.append(string)
flag = True
for letter in min(string_list):
    if not letter in max(string_list):
        flag = False
if flag:
    print('ДА')
else:
    print('НЕТ')
