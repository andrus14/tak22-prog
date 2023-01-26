me = {
    'first_name': 'Andrus',
    'last_name': 'Naulainen',
    'birth_year': 1980,
    'place_of_living': 'Kuressaare',
    'dessert': 'Pavlova'
}

print(me.get('place_of_living'))
print(me['place_of_living'])

me['dessert'] = 'Jäätis'

for k, v in me.items():
    print(k, v)

# me['personal_code'] = '1234567890'

if 'personal_code' in me:
    print('Isikukood on olemas')
else:
    print('Isikukoodi pole')