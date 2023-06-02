import random

card_dictionary = {1: {0:"Ess", 1:"To", 2:"Tre", 3:"Fire", 4:"Fem", 5:"Seks", 6:"Syv", 7:"Åtte", 8:"Ni", 9:"Ti",
                            10:"Knekt", 11:"Dame", 12:"Konge"}
    , 2:{0:"Ess", 1:"To", 2:"Tre", 3:"Fire", 4:"Fem", 5:"Seks", 6:"Syv", 7:"Åtte", 8:"Ni", 9:"Ti",
                            10:"Knekt", 11:"Dame", 12:"Konge"},
                   3: {0:"Ess", 1:"To", 2:"Tre", 3:"Fire", 4:"Fem", 5:"Seks", 6:"Syv", 7:"Åtte", 8:"Ni", 9:"Ti",
                            10:"Knekt", 11:"Dame", 12:"Konge"},
                   4: {0:"Ess", 1:"To", 2:"Tre", 3:"Fire", 4:"Fem", 5:"Seks", 6:"Syv", 7:"Åtte", 8:"Ni", 9:"Ti",
                            10:"Knekt", 11:"Dame", 12:"Konge"}}


my_list = list(card_dictionary.keys())


def random_card_value_number_generator():
    number = random.randrange(0, 13)
    return number


def random_suit_number_generator():
    number = random.randrange(1, 4)
    return number


def card_suit_dealer(random_number_suit):
    card_suite = random_number_suit
    chosen_card_suite = my_list[card_suite:card_suite+1]
    return chosen_card_suite


def card_number_dealer(random_number_card_value, random_card_number_x):
    random_card_number_y = random_card_number_x
    random_card_number = random_number_card_value
    chosen_card_number = card_dictionary[random_card_number_y].get(random_card_number)
    return chosen_card_number


def card_suite_name(suite_number):
    card_name_list = ["Ruter", "Hjerter", "Spar", "Kløver"]
    chosen_suite = my_list[suite_number:suite_number+1]
    # suite_return = card_name_list[chosen_suite]
    print(chosen_suite)

x = random_suit_number_generator()
y = random_card_value_number_generator()
z = random_suit_number_generator()

caaard = [int(x) for x in my_list]

print(caaard)

# print(card_dealer(x, y, z))



