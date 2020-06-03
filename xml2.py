import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Jordan</name>
        </user>
        <user x="3">
            <id>002</id>
            <name>Bo</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('users counts:', len(lst))

for item in lst:
    print(item.find('name').text)
    print(item.find('id').text)
    # if you want to find tag content by using find('').text,
    # if you want to find attribute content by using get("")
    print(item.get("x"))
