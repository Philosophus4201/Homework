n = int(input('Кол-во покупок '))
purch_list=[]
for purch in range(n):
    purch = input('Покупка')
    purch_list.append(purch)
for purch in purch_list:
    print(purch)