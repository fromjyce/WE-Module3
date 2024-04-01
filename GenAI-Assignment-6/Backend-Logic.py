import random

def calculate_card_value(card: str) -> int:
    return {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card] if card in ['J', 'Q', 'K', 'A'] else int(card)

def final_game():
    human_score = 0
    computer_score = 0
    list_of_computer_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    list_of_human_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    human_score, computer_score = play_game(human_score, computer_score, list_of_computer_cards, list_of_human_cards)
    print(f"Your score: {human_score} \nComputer's Score: {computer_score}")
    print("YOU WON") if human_score > computer_score else print("COMPUTER WON") if human_score < computer_score else print("TIE")
    
def who_won_round(human_card: str, computer_card: str) -> int:
    return 1 if did_computer_win(human_card, computer_card) else 2 if is_tie(human_card, computer_card) else 3

def add_score(human_score : float, computer_score : float, human_card : str, computer_card : str, revealed_card : str):
    if did_computer_win(human_card, computer_card):
        computer_score += calculate_card_value(revealed_card)
    elif is_tie(human_card, computer_card):
        computer_score += calculate_card_value(revealed_card) / 2
        human_score += calculate_card_value(revealed_card) / 2
    else:
        human_score += calculate_card_value(revealed_card)
    #print(human_score,computer_score)
    return human_score, computer_score

def computer_card_choice(revealed_card: str,list_of_computer_cards: list[str]) -> str:
    n = calculate_card_value(revealed_card)
    min_range = n - 2 if n >= 3 else 2
    max_range = n + 2 if n < 14 else 14
    available_cards = [card for card in list_of_computer_cards if min_range <= calculate_card_value(card) <= max_range]
    if available_cards:
        computer_card = max(available_cards, key=lambda x: calculate_card_value(x))
    else:
        computer_card = random.choice(list_of_computer_cards)
    list_of_computer_cards.remove(computer_card)
    return computer_card

def human_card_choice(list_of_human_cards: list[str]) -> str:
    human_card = input("Enter your bid card (A, 2, 3, ..., J, Q, K): ")
    while human_card not in list_of_human_cards:
        print("Invalid card. Play again")
        human_card = input("Enter your bid card (A, 2, 3, ..., J, Q, K): ")
    list_of_human_cards.remove(human_card)
    return human_card

def diamond_cards_shuffle() -> list[str]:
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    random.shuffle(cards)
    return cards

def did_computer_win(human_card: str, computer_card: str) -> bool:
    return calculate_card_value(human_card) < calculate_card_value(computer_card)

def is_tie(human_card:str, computer_card:str) -> bool:
    return calculate_card_value(human_card) == calculate_card_value(computer_card)

def play_game(human_score : float, computer_score : float, list_of_computer_cards : list[str], list_of_human_cards: list[str]):
    diamond_cards = diamond_cards_shuffle()
    for revealed_card in diamond_cards:
        print("Revealed card: " + revealed_card)
        human_card = human_card_choice(list_of_human_cards)
        computer_card = computer_card_choice(revealed_card,list_of_computer_cards)
        #print("COM CARD:", computer_card)
        who_won = who_won_round(human_card, computer_card)
        print("YOU WON DIAMOND CARD") if who_won == 3 else print("COMPUTER WON DIAMOND CARD") if who_won == 1 else print("IT'S A TIE")
        human_score, computer_score = add_score(human_score, computer_score, human_card, computer_card, revealed_card)
    
    return human_score, computer_score

final_game()