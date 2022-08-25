from views import *

def main():
    print('введите команду \n c - create \n l - listing \n r - retrieve \n u - update \n d - delete')
    users = input('->')
    if users == 'c':
        print(create_product())
    elif users == 'u':
        print(update_product())
    elif users == 'r':
        print(get_one_product())
    elif users == 'l':
        print(get_data())
    elif users == 'd':
        print(delete_product())

us = 'yes'
while True:
    print('Добро пожаловать в наш магазин!')
    ls = input('Хотите ли взойти на Кроссовочный Олимп? yes/no: ')
    if ls == 'yes':
        main()
    else:
        break





















