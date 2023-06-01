import BlackJackFunksjoner


# check_if_user_has_blackjack returnerer 1 dersom spiller har 21
def test_check_if_user_has_blackjack():
    user_has_blackjack = BlackJackFunksjoner.check_if_user_has_blackjack(21)
    user_does_not_have_blackjack = BlackJackFunksjoner.check_if_user_has_blackjack(20)
    assert user_has_blackjack == 1
    assert not user_does_not_have_blackjack == 1


# check_if_user_has_blackjack returnerer 2 dersom spiller har over 21
def test_check_if_user_is_over_21():
    user_has_over_21 = BlackJackFunksjoner.check_if_user_has_blackjack(22)
    user_has_over_21_25 = BlackJackFunksjoner.check_if_user_has_blackjack(25)
    assert user_has_over_21 == 2
    assert user_has_over_21_25 == 2


# check_if_user_has_blackjack returnerer 3 dersom spiller har under 21
def test_check_if_user_is_under_21():
    user_has_20 = BlackJackFunksjoner.check_if_user_has_blackjack(20)
    user_has_1 = BlackJackFunksjoner.check_if_user_has_blackjack(1)
    assert user_has_20 == 3
    assert user_has_1 == 3

