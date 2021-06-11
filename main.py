# function
def greetings(name, cities ):
    print('Bienvenue à vous', name)
    print("j'espere que vous allez bien à", cities[name])
    if cities[name] == 'Abidjan':
        print('Bonjour a vous le ivos ')


# data
names = ['Franck', 'Aimé', 'Désiré']
cities = {'Franck': 'Bordeaux', 'Aimé': 'Abidjan', 'Désiré': 'Gagnoa'}


# app
for name in names:
    greetings(name, cities)
