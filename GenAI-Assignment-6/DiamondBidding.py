import pygame
import sys
import time
import random

pygame.init()

#screen width
width = 800
height = 600


background_color = (13, 116, 47)  # green

#screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Diamond Bidding Game")

#images for splash screen
image1 = pygame.image.load(r'C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\Name.png')
image2 = pygame.image.load(r'C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\PyGame.png')

image1_width = 250
image1_height = 250
image2_width = 315
image2_height = 175

image1 = pygame.transform.scale(image1, (image1_width, image1_height))
image2 = pygame.transform.scale(image2, (image2_width, image2_height))


def splash_screen():
    screen.fill(background_color)

    screen.blit(image1, ((width - image1_width) // 2, (height - image1_height) // 4))
    
    font = pygame.font.SysFont(None, 35)
    text_surface = font.render("Developed using", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, (height // 2) + 30))  
    screen.blit(text_surface, text_rect)

    screen.blit(image2, ((width - image2_width) // 2, (height - image2_height) // 4 * 3))

    pygame.display.flip()
    time.sleep(5)

def calculate_card_value(card: str) -> int:
    return {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card] if card in ['J', 'Q', 'K', 'A'] else int(card)

def diamond_cards_shuffle() -> list[str]:
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    random.shuffle(cards)
    return cards

def did_computer_win(human_card: str, computer_card: str) -> bool:
    return calculate_card_value(human_card) < calculate_card_value(computer_card)

def is_tie(human_card:str, computer_card:str) -> bool:
    return calculate_card_value(human_card) == calculate_card_value(computer_card)

def who_won_round(human_card: str, computer_card: str) -> int:
    return 1 if did_computer_win(human_card, computer_card) else 2 if is_tie(human_card, computer_card) else 3

def computer_card_choice(revealed_card: str,list_of_computer_cards: list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']) -> str:
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

def winner_page():
    screen.fill(background_color)
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 42)
    text = font.render("Winner!!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 240))
    screen.blit(text, text_rect)

    pygame.display.flip()

def spades_page():
    current_card_index = 0
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 42)
    text = font.render("Choose a Card", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 240))
    screen.blit(text, text_rect)

    revealed_card_width = 125
    revealed_card_height = 175
    cards = diamond_cards_shuffle()
    
    #revealed_card = cards[current_card_index]
    diamond_card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\Joker.png")
    diamond_card_image = pygame.transform.scale(diamond_card_image, (revealed_card_width, revealed_card_height))
    diamond_card_button_rect = diamond_card_image.get_rect(center=(width // 2 - 260, height // 2 - 100))
    screen.blit(diamond_card_image, diamond_card_button_rect)
    #cards.remove(revealed_card)

    # Display next button
    next_button_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\NextButton.png")
    next_button_image = pygame.transform.scale(next_button_image, (200, 200))
    next_button_image_rect = next_button_image.get_rect(center=(width // 2 - 260, height // 2 + 200))
    screen.blit(next_button_image, next_button_image_rect)

    display_card_width = 90
    display_card_height = 140

    selected_card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\Joker.png")
    selected_card_image = pygame.transform.scale(selected_card_image, (display_card_width,display_card_height))

    card_positions = [((width // 2 - 90, height // 2 - 115), "A"), ((width // 2 + 15, height // 2 - 115), "2"), ((width // 2 + 120, height // 2 - 115), "3"), ((width // 2 + 225, height // 2 - 115), "4"), ((width // 2 + 330, height // 2 - 115), "5"),
                      ((width // 2 - 90, height // 2 + 40), "6"), ((width // 2 + 15, height // 2 + 40), "7"), ((width // 2 + 120, height // 2 + 40), "8"), ((width // 2 + 225, height // 2 + 40), "9"), ((width // 2 + 330, height // 2 + 40), "10"), 
                      ((width // 2 - 90, height // 2 + 195), "J"), ((width // 2 + 15, height // 2 + 195), "Q"), ((width // 2 + 120, height // 2 + 195), "K")]
    
    for position, card_value in card_positions:
        card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Spades\{}.png".format(card_value))
        card_image = pygame.transform.scale(card_image, (display_card_width, display_card_height))
        card_rect = card_image.get_rect(center=(position))
        screen.blit(card_image, card_rect)


    pygame.display.flip()

    a_button_range_x = range(266, 350)
    a_button_range_y = range(118, 244)

    two_button_range_x = range(378, 450)
    two_button_range_y = range(119, 247)


    three_button_range_x = range(478, 558)
    three_button_range_y = range(123, 247)

    four_button_range_x = range(582, 666)
    four_button_range_y = range(117, 251)

    five_button_range_x = range(688, 772)
    five_button_range_y = range(119, 246)

    six_button_range_x = range(267, 354)
    six_button_range_y = range(276, 404)

    seven_button_range_x = range(374, 457)
    seven_button_range_y = range(277, 402)

    eight_button_range_x = range(481, 560)
    eight_button_range_y = range(278, 404)

    nine_button_range_x = range(587, 665)
    nine_button_range_y = range(275, 404)

    ten_button_range_x = range(690, 771)
    ten_button_range_y = range(275, 402)

    jack_button_range_x = range(270, 352)
    jack_button_range_y = range(431, 560)

    queen_button_range_x = range(375, 458)
    queen_button_range_y = range(429, 560)

    king_button_range_x = range(482, 560)
    king_button_range_y = range(431, 564)

    next_button_range_x = range(81, 199)
    next_button_range_y = range(477, 520)

    human_card = 0
    revealed_score_card = 0
    computer_card = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print("Mouse Position:", mouse_x, mouse_y)


def hearts_page():
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 42)
    text = font.render("Choose a Card", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 250))
    screen.blit(text, text_rect)

    pygame.display.flip()

def clubs_page():
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 42)
    text = font.render("Choose a Card", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 250))
    screen.blit(text, text_rect)

    pygame.display.flip()

def choosing_suits_page():
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 48)
    text = font.render("Choose a Deck", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 175))
    screen.blit(text, text_rect)

    spade_deck_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Spades\A.png")
    heart_deck_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Hearts\A.png")
    club_deck_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Clubs\A.png")
    back_button_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\BackButton.png")

    card_width = 125
    card_height = 175
    button_width = 325
    button_height = 325

    spade_deck_image = pygame.transform.scale(spade_deck_image, (card_width, card_height))
    heart_deck_image = pygame.transform.scale(heart_deck_image, (card_width, card_height))
    club_deck_image = pygame.transform.scale(club_deck_image, (card_width, card_height))
    back_button_image = pygame.transform.scale(back_button_image, (button_width, button_height))

    spade_deck_button_rect = spade_deck_image.get_rect(center=(width // 2 - 200, height // 2 - 40))
    heart_deck_button_rect = heart_deck_image.get_rect(center=(width // 2 , height // 2 - 40))
    club_deck_button_rect = club_deck_image.get_rect(center=(width // 2 + 200, height // 2 - 40))    
    back_button_image_rect = back_button_image.get_rect(center=(width // 2, height // 2 + 130))

    screen.blit(spade_deck_image, spade_deck_button_rect)
    screen.blit(heart_deck_image, heart_deck_button_rect)
    screen.blit(club_deck_image, club_deck_button_rect)
    screen.blit(back_button_image, back_button_image_rect)

    pygame.display.flip()

    spade_deck_button_range_x = range(137, 261)
    spade_deck_button_range_y = range(174, 344)

    heart_deck_button_range_x = range(339, 458)
    heart_deck_button_range_y = range(178, 341)

    club_deck_button_range_x = range(544, 659)
    club_deck_button_range_y = range(177, 341)

    back_button_image_rect_range_x = range(303, 497)
    back_button_image_rect_range_y = range(388, 465)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #print("Mouse Position:", mouse_x, mouse_y)  # Debug information
                if mouse_x in spade_deck_button_range_x and mouse_y in spade_deck_button_range_y:
                    spades_page()
                elif mouse_x in heart_deck_button_range_x and mouse_y in heart_deck_button_range_y:
                    hearts_page()
                elif mouse_x in club_deck_button_range_x and mouse_y in club_deck_button_range_y:
                    clubs_page()
                elif mouse_x in back_button_image_rect_range_x and mouse_y in back_button_image_rect_range_y:
                    main_screen()

def helping_game_page():
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 48)
    text = font.render("How to Play this Game?", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 175))
    screen.blit(text, text_rect)

    pygame.display.flip()


def exit_button():
    pygame.quit()
    sys.exit()

def main_screen():
    screen.fill(background_color)

    font = pygame.font.SysFont(None, 48)
    text = font.render("Diamond Bidding Game", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 150))
    screen.blit(text, text_rect)

    play_button_image = pygame.image.load(r'C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\PlayButton.png')
    help_button_image = pygame.image.load(r'C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\HelpButton.png')
    exit_button_image = pygame.image.load(r'C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\ExitButton.png')

    button_width = 325
    button_height = 325
    play_button_image = pygame.transform.scale(play_button_image, (button_width, button_height))
    help_button_image = pygame.transform.scale(help_button_image, (button_width, button_height))
    exit_button_image = pygame.transform.scale(exit_button_image, (button_width, button_height))

    play_button_rect = play_button_image.get_rect(center=(width // 2, height // 2 - 50))
    help_button_rect = help_button_image.get_rect(center=(width // 2, height // 2 + 50))
    exit_button_rect = exit_button_image.get_rect(center=(width // 2, height // 2 + 150))

    screen.blit(play_button_image, play_button_rect)
    screen.blit(help_button_image, help_button_rect)
    screen.blit(exit_button_image, exit_button_rect)

    pygame.display.flip()

    # Define ranges for buttons
    play_button_range_x = range(303, 498)
    play_button_range_y = range(210, 290)

    help_button_range_x = range(304, 497)
    help_button_range_y = range(310, 388)

    exit_button_range_x = range(310, 488)
    exit_button_range_y = range(420, 482)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #print("Mouse Position:", mouse_x, mouse_y)  # Debug information
                if mouse_x in play_button_range_x and mouse_y in play_button_range_y:
                    choosing_suits_page()
                elif mouse_x in help_button_range_x and mouse_y in help_button_range_y:
                    helping_game_page()
                elif mouse_x in exit_button_range_x and mouse_y in exit_button_range_y:
                    exit_button()


splash_screen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_screen()
    #spades_page()


pygame.quit()
sys.exit()