import json

FILE = 'data.json'

#сереализируем файл json в python
 
def get_data():
    with open(FILE) as f:
        return json.load(f)

# Создаем функцию которая будет добавлять id в продукт

def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id +=1
    with open('id.txt' ,'w') as file:
        file.write(str(id))
    return id 

# Создаем функцию которая будет добавлять продукт

def  create_product():
    data = get_data()
    product = {
        'id': get_id(),
        'title': input('Введите название продукта : '),
        'price': int(input('Введите цену на продукт : '))
    }

    data.append(product)
    with open(FILE, 'w') as file:
        json.dump(data,file)
    return 'Продукт создан!'

# Создаем функцию которая будет изменять продукт

def update_product():
    data = get_data()
    flag = False
    id = int(input('Введите id для изменения продукта: '))
    product = list(filter(lambda x: x['id'] == id,data))
    if not product:
        return 'Нет такого продукта!'

    index_ = data.index(product[0])
    user = input('Что вы хотите изменить? \n 1 - title \n 2 - price ')
    if user == '1':
        data[index_] ['title'] = input('Введите новое название продукта: ')
        flag = True
    elif user == '2':
        data[index_] ['price'] = input('Введите новую цену продукта: ')
        flag = True
    else:
        return 'Такой команды нет!'

    with open(FILE, 'w') as file:
        json.dump(data,file)

    if flag:
        return 'Продукт изменен!'
    
    else:
        return 'Продукт не изменен!'


# Создаем функцию которая будет удалять продукт

def delete_product():
    data = get_data()
    id = int(input('Введите id продукта для удаления: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'Нет такого продукта!'
    index_ = data.index(product[0])
    data.pop(index_)
    json.dump(data, open(FILE, 'w'))
    return 'Продукт удален!'

# Создаем функцию которая будет выводить только один продукт

def get_one_product():
    data = get_data()
    id = int(input('Введите id продукта: '))
    product = list(filter(lambda x: x['id'] == id,data))

    if product:
        return product[0]
    else:
        return 'Нет такого продукта!'
        



















