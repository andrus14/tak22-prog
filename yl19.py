vowels = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
text = 'Kuressaare Ametikool' #10
i = 0

for c in text:
    if c.lower() in vowels:
        i += 1

print('Täishäälikute arv tekstis:', i)

