import json

input = '''
[ 
  {"id":"001", "x":"12", "name":"chuck"},
  {"id":"002", "x":"18", "name":"Bo"}
]
'''

info = json.loads(input)
print('Counts: ', len(info))

for item in info:
    print('Name', item['name'])
    print('ID', item['id'])
    print('Attribute', item['x'])