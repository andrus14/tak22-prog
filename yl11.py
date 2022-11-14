import math

text = input('Sisend: ').strip()

print(len(text))

if len(text) >= 7 and len(text) % 2 == 1:
    print('Vastab tingimustele')
    i = math.floor(len(text) / 2)
    print(text[i-1:i+2])
else:
    print('Sisend ei vasta tingimustele')