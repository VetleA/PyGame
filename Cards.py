import random

card_value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 14]

suit_list = ["Hjerter", "Ruter", "Kløver", "Spar"]


def random_card_value_number_generator():
    number = random.randrange(0, 10)
    return number


def random_suit_number_generator():
    number = random.randrange(1, 4)
    return number


def card_suit_dealer(random_number_suit):
    chosen_card_suite = suit_list[random_number_suit]
    return chosen_card_suite


def card_number_dealer(random_card_number_x):
    chosen_card_number = card_value_list[random_card_number_x]
    return chosen_card_number


suit_num = random_suit_number_generator()
card_num = random_card_value_number_generator()

