# textovy_analyzator.py: prvni projekt, zjistovani informaci o libovolne dlouhem textu
# author: Petr Běla
# email: petr.bela@seznam.cz
# discord: Petr B. Gibon420#2267

# libovolný text
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

# ulozene udaje
users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]
dict_users = dict(zip(users, passwords))

# proměnné
oddelovac = "=" * 40
pocet_slov = 0
title_pismeno = 0
velka_pismena = 0
mala_pismena = 0
cisla = 0
soucet = []
delky_slov = dict()

# získaní vstupu od uzivatele
user = input("username: ")
password = input("password: ")
print(oddelovac)

# zjisteni jestli uzivatel existuje a zadane heslo je správné
if user in dict_users:
    # zjisteni jestli zadal spravne heslo
    if password == dict_users.get(user):
        print(f"Welcome to the app, {user}")
        print(f"We have {len(TEXTS)} texts to be analyzed.")
        print(oddelovac)
    else:
        print(f"Wrong Password! Exiting ...")
        exit()

    # ověření zda je zadaný vstup číslo, pokud ne ukončí program
    try:
        vyber = int(input(f"Enter a number btw. 1 and 3 to select: "))
        print(oddelovac)
    except ValueError:
        print(f"Must be a number, Exiting ...")
        exit()

    # ověření že zadané číslo odpovídá nějakému ze zadaných těxtů
    if 1 <= vyber <= len(TEXTS):
        slova = TEXTS[vyber - 1].split() # tímto vyberu text na danem indexu a rovnou to rozdelim na slova do list()
        for slovo in slova:
            ocistene_slovo = slovo.strip(".,!?") # očistí slovo od interpunkčních znamének
            delka = len(ocistene_slovo)
            if ocistene_slovo: # kontroluje zda slovo není prázdné po odstranění znamének
                pocet_slov += 1
            if ocistene_slovo.istitle(): # vrací True pokud string začíná velkým písmenem a následují malá písmena
                title_pismeno += 1
            if ocistene_slovo.isupper() and ocistene_slovo.isalpha(): # vrací True pokud string obsahuje jen velká písmena
                velka_pismena += 1
            if ocistene_slovo.islower(): # vrací True pokud obsahuje jen malá písmena
                mala_pismena += 1
            if ocistene_slovo.isdigit(): # vrací True pokud obsahuje pouze číslice
                cisla += 1
                soucet.append(int(slovo))
            if delka not in delky_slov:
                delky_slov[delka] = 1
            else:
                delky_slov[delka] += 1

        # výpis statistik
        print(f"There are {pocet_slov} words in selected text.")
        print(f"There are {title_pismeno} titlecase words.")
        print(f"There are {velka_pismena} uppercase words.")
        print(f"There are {mala_pismena} lower words.")
        print(f"There are {cisla} numeric string.")
        print(f"The sum of all the numbers {sum(soucet)}")
        print(oddelovac)

        # sloupcovy graf
        max_length = max(delky_slov.values())
        print("LEN|".rjust(3), "OCCURENCES".center(max_length) + "|NR.")
        print(oddelovac)

        for key, value in sorted(delky_slov.items()):
            print(str(key).rjust(3) + "|" + ("#" * value).ljust(max_length), ("|" + str(value)))
    else:
        print(f"Invalid text selection, Exiting ...")
        exit()
else:
    print(f"unregistered user, terminating the program ...")
    exit()