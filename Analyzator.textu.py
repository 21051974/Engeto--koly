print('=' * 50)
print('Zadejte své přihlašovací údaje do Analyzátoru textu:')
print()

data = {
	'uzivatel1': 'heslo',
	'bob': '123',
	'ann': 'pass123',
    'mike': 'password123',
    'liz' : 'pass123',
			}

jmeno = input("Jméno : ")
password = input('Heslo : ')

if  data.get(jmeno) != password:
    print('Heslo, nebo uživatelské jméno je špatně ')

elif data.get (jmeno) == password:
    print('V pořádku - pokračujte :) ')

print('-' * 50)

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

poradi = 0                  #zde uvádím příkaz k očíslování článků 1-3
for jmeno in TEXTS:
  poradi +=1
  print("Článek č.:", poradi, jmeno)

for i in TEXTS:
    print(i)
print('=' * 45)
text = int(input("Vyber si, který text odstavce požaduješ zpracovat ?"))
if text > 3:
    print("Máme jen 3 odstavce !! ")
    exit()
ODST = TEXTS[text-1]
rozdeleni = ODST.split()
cisty_list = [i.strip(",.") for i in rozdeleni]
print('=' * 45)
print(f"Počet slov v textu je: {len(cisty_list)}")
count = 0
male = 0
cis = 0
for i in cisty_list:
    if i.istitle():
        count = count + 1
    if i.islower():
        male = male + 1
    if i.isnumeric():
        cis = cis + 1
print('=' * 45)
print(f"Počet slov začínajících velkým písmenem je: {count}.")
print('=' * 45)
print(f"Počet slov psaných malými pismeny je: {male}.")
print('=' * 45)
print(f"Počet čísel v textu je: {cis}.")
print('=' * 45)
delka_slova = {}
for i in cisty_list:
    delka_slova[len(i)] = delka_slova.setdefault(len(i), 0) + 1
sort = sorted(delka_slova, key=delka_slova.get, reverse=True)
print("Nejčastějsí počet písmen ve slově.")
for i in sort:
    print(i, delka_slova.get(i) * "*", delka_slova.get(i), "x")
soucet = []
for i in cisty_list:
    if i.isnumeric():
        soucet.append(int(i))
konec = sum(soucet)
print('-' * 45)
print(f"Součet všech čísel v textu je {float(konec)}.")
print('=' * 45)
print("Program 'Analyzátor textu' ukončen.")