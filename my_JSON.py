import json

my_dict = {'class': 'Mage', 'level': 5, 'items': ['sword', 'potion']}

to_json = json.dumps(my_dict, indent=5)
print(to_json)