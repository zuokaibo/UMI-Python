import json

data = '''
{
    "name" : "chuck",
    "phone": {"type":"intl", "number":"47720429865"},
    "email": {"hide" : "yes"}
}
'''

info = json.loads(data)
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])