a = float(input('Sisesta 1. küljepikkus: '))
b = float(input('Sisesta 2. küljepikkus: '))
c = float(input('Sisesta 3. küljepikkus: '))

if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print('Kolmnurk on võrdkülgne')
    elif a == b or b == c or c == a:
        print('Kolmnurk on võrdhaarne')
    else:
        print('Kolnurk on erikülgne')

else:
    print('Selliste küljepikkustega kolmnurk ei saa eksisteerida')