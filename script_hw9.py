def load_cook_book_json(file_name):
	import json
	with open(file_name, "r", encoding="utf-8") as file:
		cook_book = json.load(file)
	return cook_book

def load_cook_book_yaml(file_name):
	import yaml
	with open(file_name, "r", encoding="utf-8") as file:
		cook_book = yaml.load(file)
	return cook_book

def get_shop_list_by_dishes(cook_book, dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
	for shop_list_item in shop_list.values():
		print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
    
def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
  cook_book = load_cook_book_json("data_hw9.json") #данные берутся из файла в формате json
  # cook_book = load_cook_book_yaml("data_hw9.yml") #данные берутся из файла в формате yaml
  shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()

