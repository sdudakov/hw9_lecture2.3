def load_cook_book(file_name):
	import json
	with open(file_name, "r", encoding="utf-8") as file:
		cook_book = json.load(file)
	# cook_book = {}
	# with open(file_name, "r", encoding="utf-8") as f:
	# 	for dish in f:
	# 		ingridient_count = int(f.readline())
	# 		ingridient_list = [] #создаю пустой список, который будет обнуляться на следующей итерации
	# 		for _ in range(ingridient_count):
	# 			ingridient = f.readline()
	# 			ingridient = ingridient.strip()
	# 			ingridient = ingridient.split(" | ")
	# 			ingridient_item = dict({"ingridient_name": ingridient[0], "quantity": int(ingridient[1]), "measure": ingridient[2]})
	# 			ingridient_list.append(ingridient_item) #на каждой итерации добавляю в список словарь
	# 		cook_book[dish.strip()] = ingridient_list #присваиваю ключу dish словаря cook_book значение - список, состоящий из словарей
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
  cook_book = load_cook_book("data_hw9.json")
  shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
  print_shop_list(shop_list)

#create_shop_list()

# записать cook_book в файл data_hw9.json
# cook_book = load_cook_book("data_hw7.txt")
# import json
# with open("data_hw9.json", "w", encoding="utf-8") as file:
# 	json.dump(cook_book, file, ensure_ascii=False, indent=2)

# прочитать cook_book из файла data_hw9.json
# import json
# from pprint import pprint
# with open("data_hw9.json", "r", encoding="utf-8") as file:
# 	cook_book = json.load(file)
# pprint(cook_book)

import yaml
cook_book = load_cook_book("data_hw9.json")
with open("data_hw9.yml", "w", encoding="utf-8") as file:
 	yaml.dump(cook_book, file, allow_unicode = True, encoding = None, indent=2)

# with open(data_hw9.yml, "r", encoding="utf-8") as file:
# 	cook_book = yaml.load(file)
# 	pprint(cook_book)
