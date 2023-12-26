# zbiory (sets) są kolekcjami elementów, które są unikalne i nieuporządkowane
# Oznacza to, że w zbiorze nie mogą występować duplikaty, a także nie ma określonego porządku elementów, 
# co oznacza, że nie można odwoływać się do nich za pomocą indeksów.

# Add - Dodawanie kolejnego elementu 
subjects = {'mathematics', 'polish'}
subjects.add('english')

print(subjects)

print('---')

"""
Wykorzystując zmienną text wykonaj następujące kroki:
    Zamień wszystkie litery na małe.
    Usuń wszystkie spacje i kropkę.
    Utwórz zbiór składający się z pozostałych liter w tak przetworzonym tekście.
"""
text = 'Programming in python.'
lower_text = text.lower()
without_lower_text = text.split()
set_all = set(("").join(without_lower_text).lower()) - {'.'}
vowels = {'a', 'e', 'i', 'o', 'u'}
without_vowels = set_all - vowels

print(f"Number of consonants: {len(without_vowels)}")

print('---')

# wyznacz różnicę symetryczną zbiorów set_A i set_B
set_A = {2, 4, 6, 8}
set_B = {4, 10}

symmetricDifferent = set_A.symmetric_difference(set_B)

print(f"Symmetric difference: {symmetricDifferent}")

print('---')

# wuyznacz ID, które pojawiły się tylko raz pomiędzy zbiorem ad1_ids i ad2_ids

ad1_ids = {'001', '002', '003'}
ad2_ids = {'002', '003', '007'}
ad_all = []

for item in ad1_ids:
    if item in ad2_ids:
        print(f'Produkt występuje {item}')
    else:
        ad_all.append(item)

for item in ad2_ids:
    if item in ad1_ids:
        print(f'Produkt występuje {item}')
    else:
        ad_all.append(item)

print(f"Selected IDs: {set(ad_all)}")

print('---')

# Zwróć ID tych klientów, którzy kliknęli w reklamę i kupili produkt.
# intersection - część wspólna

clicked_ids = {'9001', '9002', '9005'}
bought_ids = {'9002', '9004', '9005'}

theSame = clicked_ids.intersection(bought_ids)

print(theSame)

print('---')

# tego które jeszcze zostały 
flights = {'AA100', 'UA200', 'DL300', 'WN400'}
booked_flights = {'AA100', 'WN400'}

available_flights = flights - booked_flights

print(available_flights)

print('---')

# część wspolna 
daily_menu = {
    'burger',
    'fries',
    'hot dog',
    'chicken sandwich',
    'pasta with seafood',
}
fixed_vegetarian_options = {
    'fries',
    'onion rings',
    'pasta with seafood',
    'feta salad',
}

vegetarian_menu = daily_menu.intersection(fixed_vegetarian_options)

print(vegetarian_menu)