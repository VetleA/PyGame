def check_if_user_has_blackjack(user_card_score):
    if user_card_score == 21:
        return 1
    elif user_card_score > 21:
        return 2
    elif user_card_score < 21:
        return 3
