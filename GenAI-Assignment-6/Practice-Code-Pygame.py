import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CARD_WIDTH = 100
CARD_HEIGHT = 150
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 30

# Function to display text
def draw_text(surface, text, x, y, color=BLACK, font_size=FONT_SIZE):
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

# Function to display cards
def display_cards(surface, cards, y):
    x = 50
    for card in cards:
        draw_text(surface, str(card), x, y)
        x += CARD_WIDTH + 20

# Function to shuffle diamond cards
def diamond_cards_shuffle():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    random.shuffle(cards)
    return cards

# Function to calculate card value
def calculate_card_value(card):
    if card in ['J', 'Q', 'K']:
        return {'J': 11, 'Q': 12, 'K': 13}[card]
    elif card == 'A':
        return 14
    else:
        return int(card)

# Function to determine winner of a round
def who_won_round(human_card, computer_card):
    if calculate_card_value(human_card) < calculate_card_value(computer_card):
        return 1
    elif calculate_card_value(human_card) > calculate_card_value(computer_card):
        return 2
    else:
        return 3

# Function to add scores
def add_score(human_score, computer_score, human_card, computer_card, revealed_card):
    if calculate_card_value(human_card) < calculate_card_value(computer_card):
        computer_score += calculate_card_value(revealed_card)
    elif calculate_card_value(human_card) > calculate_card_value(computer_card):
        human_score += calculate_card_value(revealed_card)
    else:
        human_score += calculate_card_value(revealed_card) / 2
        computer_score += calculate_card_value(revealed_card) / 2
    return human_score, computer_score

# Function for computer to choose card
def computer_card_choice(revealed_card, list_of_computer_cards):
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

# Function for human to choose card
def human_card_choice(list_of_human_cards):
    human_card = input("Enter your bid card (A, 2, 3, ..., J, Q, K): ")
    while human_card not in list_of_human_cards:
        print("Invalid card. Play again")
        human_card = input("Enter your bid card (A, 2, 3, ..., J, Q, K): ")
    list_of_human_cards.remove(human_card)
    return human_card

# Function to play the game
def play_game():
    human_score = 0
    computer_score = 0
    list_of_computer_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    list_of_human_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    diamond_cards = diamond_cards_shuffle()
    
    # Initialize Pygame window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Diamond Bidding Game")
    
    # Game loop
    for revealed_card in diamond_cards:
        screen.fill(WHITE)
        draw_text(screen, f"Revealed card: {revealed_card}", 50, SCREEN_HEIGHT // 2 - 50)
        pygame.display.flip()
        pygame.time.delay(2000)
        
        human_card = human_card_choice(list_of_human_cards)
        computer_card = computer_card_choice(revealed_card, list_of_computer_cards)
        who_won = who_won_round(human_card, computer_card)
        
        screen.fill(WHITE)
        draw_text(screen, f"You chose: {human_card}", 50, SCREEN_HEIGHT // 2 - 50)
        draw_text(screen, f"Computer chose: {computer_card}", 50, SCREEN_HEIGHT // 2 + 50)
        pygame.display.flip()
        pygame.time.delay(2000)
        
        human_score, computer_score = add_score(human_score, computer_score, human_card, computer_card, revealed_card)
    
    # Print final scores
    screen.fill(WHITE)
    draw_text(screen, f"Your score: {human_score}", 50, SCREEN_HEIGHT // 2 - 50)
    draw_text(screen, f"Computer's score: {computer_score}", 50, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()
    pygame.time.delay(3000)
    
    if human_score > computer_score:
        print("YOU WON!")
    elif human_score < computer_score:
        print("COMPUTER WON!")
    else:
        print("IT'S A TIE!")

# Main function
def main():
    play_game()

if __name__ == "__main__":
    main()
