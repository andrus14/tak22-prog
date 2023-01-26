user = input('Nimi: ')
print('Tere,', user + '!')

living_place = input('Elukoht: ')
if living_place.lower() == 'saaremaa':
    print('Ööööö, lahe!')

age = int(input('Vanus: '))
if age < 18:
    print('Liiga noor, et autot juhtida')
elif age == 18:
    print('Palju õnne!')
else:
    print('Võid autot juhtida')