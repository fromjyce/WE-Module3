#Play Diamond Bidding Game using Graphical User Interface

import pygame
import sys
import time
import pyautogui
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

def display_winners(human_score, computer_score):
    screen.fill(background_color)
    if human_score > computer_score:
        winner = "You"
    elif human_score < computer_score:
        winner = "Computer"
    else:
        winner = "It's a tie"
    
    message = f"The winner is: {winner}!\n\nYour Score: {human_score}\nComputer Score: {computer_score}"
    
    pyautogui.alert(message, "Winner")

def spades_page():
    current_card_index = 0
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 42)
    text = font.render("Choose a Card", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 240))
    screen.blit(text, text_rect)

    cards = diamond_cards_shuffle()

    def display_current_card():
        revealed_card_width = 125
        revealed_card_height = 175
        if current_card_index < len(cards):
            revealed_card = cards[current_card_index]
            diamond_card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Diamonds\{}.png".format(revealed_card))
            diamond_card_image = pygame.transform.scale(diamond_card_image, (revealed_card_width, revealed_card_height))
            diamond_card_button_rect = diamond_card_image.get_rect(center=(width // 2 - 260, height // 2 - 100))
            screen.blit(diamond_card_image, diamond_card_button_rect)
            pygame.display.flip()
        else:
            pass

    display_current_card()

    # Display next button
    home_button_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\HomeButton.png")
    home_button_image = pygame.transform.scale(home_button_image, (200, 200))
    home_button_image_rect = home_button_image.get_rect(center=(width // 2 - 260, height // 2 + 200))
    screen.blit(home_button_image, home_button_image_rect)

    display_card_width = 90
    display_card_height = 140

    selected_card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\Joker.png")
    selected_card_image = pygame.transform.scale(selected_card_image, (display_card_width,display_card_height))

    card_rects = {}

    card_positions = [((width // 2 - 90, height // 2 - 115), "A"), ((width // 2 + 15, height // 2 - 115), "2"), ((width // 2 + 120, height // 2 - 115), "3"), ((width // 2 + 225, height // 2 - 115), "4"), ((width // 2 + 330, height // 2 - 115), "5"),
                      ((width // 2 - 90, height // 2 + 40), "6"), ((width // 2 + 15, height // 2 + 40), "7"), ((width // 2 + 120, height // 2 + 40), "8"), ((width // 2 + 225, height // 2 + 40), "9"), ((width // 2 + 330, height // 2 + 40), "10"), 
                      ((width // 2 - 90, height // 2 + 195), "J"), ((width // 2 + 15, height // 2 + 195), "Q"), ((width // 2 + 120, height // 2 + 195), "K")]
    
    for position, card_value in card_positions:
        card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Spades\{}.png".format(card_value))
        card_image = pygame.transform.scale(card_image, (display_card_width, display_card_height))
        card_rect = card_image.get_rect(center=(position))
        card_rects[card_value] = card_rect
        screen.blit(card_image, card_rect)

    pygame.display.flip()

    button_ranges = {
        (range(266, 350), range(118, 244)) : "A",
        (range(378, 450), range(119, 247)) : 2, 
        (range(478, 558), range(123, 247)) : 3,
        (range(582, 666), range(117, 251)) : 4,
        (range(688, 772), range(119, 246)) : 5,
        (range(267, 354), range(276, 404)) : 6,
        (range(374, 457), range(277, 402)) : 7,
        (range(481, 560), range(278, 404)) : 8,
        (range(587, 665), range(275, 404)) : 9,
        (range(690, 771), range(275, 402)) : 10,
        (range(270, 352), range(431, 560)) : "J",
        (range(375, 458), range(429, 560)) : "Q",
        (range(482, 560), range(431, 564)) : "K"
    }

    home_button_range_x = range(81, 199)
    home_button_range_y = range(477, 520)

    human_card = 0
    revealed_score_card = 0
    computer_card = 0

    click_count = 0

    human_score = 0
    computer_score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #print("Mouse Position:", mouse_x, mouse_y)
                for button_range, card_value in button_ranges.items():
                    if mouse_x in button_range[0] and mouse_y in button_range[1]:
                        human_card = card_value
                        if current_card_index < len(cards):
                            current_card_index += 1
                            computer_card = computer_card_choice(cards[current_card_index - 1])
                            revealed_score_card = cards[current_card_index - 1]
                            display_current_card()
                            screen.blit(selected_card_image, card_rects[str(human_card)])
                            pygame.display.flip()
                            click_count += 1
                            human_score, computer_score = add_score(human_score, computer_score, human_card, computer_card, revealed_score_card)
                            if click_count == 13:
                                display_winners(human_score, computer_score)
                        #print("HUMAN: {h}; COMPUTER: {c}; Revealed: {r}".format(h=human_card, c=computer_card, r=revealed_score_card))
                        break
                if mouse_x in home_button_range_x and mouse_y in home_button_range_y:
                    main_screen()


def hearts_page():
    current_card_index = 0
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 42)
    text = font.render("Choose a Card", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 240))
    screen.blit(text, text_rect)

    cards = diamond_cards_shuffle()

    def display_current_card():
        revealed_card_width = 125
        revealed_card_height = 175
        if current_card_index < len(cards):
            revealed_card = cards[current_card_index]
            diamond_card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Diamonds\{}.png".format(revealed_card))
            diamond_card_image = pygame.transform.scale(diamond_card_image, (revealed_card_width, revealed_card_height))
            diamond_card_button_rect = diamond_card_image.get_rect(center=(width // 2 - 260, height // 2 - 100))
            screen.blit(diamond_card_image, diamond_card_button_rect)
            pygame.display.flip()
        else:
            pass

    display_current_card()

    # Display next button
    home_button_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\HomeButton.png")
    home_button_image = pygame.transform.scale(home_button_image, (200, 200))
    home_button_image_rect = home_button_image.get_rect(center=(width // 2 - 260, height // 2 + 200))
    screen.blit(home_button_image, home_button_image_rect)

    display_card_width = 90
    display_card_height = 140

    selected_card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\Joker.png")
    selected_card_image = pygame.transform.scale(selected_card_image, (display_card_width,display_card_height))

    card_rects = {}

    card_positions = [((width // 2 - 90, height // 2 - 115), "A"), ((width // 2 + 15, height // 2 - 115), "2"), ((width // 2 + 120, height // 2 - 115), "3"), ((width // 2 + 225, height // 2 - 115), "4"), ((width // 2 + 330, height // 2 - 115), "5"),
                      ((width // 2 - 90, height // 2 + 40), "6"), ((width // 2 + 15, height // 2 + 40), "7"), ((width // 2 + 120, height // 2 + 40), "8"), ((width // 2 + 225, height // 2 + 40), "9"), ((width // 2 + 330, height // 2 + 40), "10"), 
                      ((width // 2 - 90, height // 2 + 195), "J"), ((width // 2 + 15, height // 2 + 195), "Q"), ((width // 2 + 120, height // 2 + 195), "K")]
    
    for position, card_value in card_positions:
        card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Hearts\{}.png".format(card_value))
        card_image = pygame.transform.scale(card_image, (display_card_width, display_card_height))
        card_rect = card_image.get_rect(center=(position))
        card_rects[card_value] = card_rect
        screen.blit(card_image, card_rect)

    pygame.display.flip()

    button_ranges = {
        (range(266, 350), range(118, 244)) : "A",
        (range(378, 450), range(119, 247)) : 2, 
        (range(478, 558), range(123, 247)) : 3,
        (range(582, 666), range(117, 251)) : 4,
        (range(688, 772), range(119, 246)) : 5,
        (range(267, 354), range(276, 404)) : 6,
        (range(374, 457), range(277, 402)) : 7,
        (range(481, 560), range(278, 404)) : 8,
        (range(587, 665), range(275, 404)) : 9,
        (range(690, 771), range(275, 402)) : 10,
        (range(270, 352), range(431, 560)) : "J",
        (range(375, 458), range(429, 560)) : "Q",
        (range(482, 560), range(431, 564)) : "K"
    }

    home_button_range_x = range(81, 199)
    home_button_range_y = range(477, 520)

    human_card = 0
    revealed_score_card = 0
    computer_card = 0

    click_count = 0

    human_score = 0
    computer_score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #print("Mouse Position:", mouse_x, mouse_y)
                for button_range, card_value in button_ranges.items():
                    if mouse_x in button_range[0] and mouse_y in button_range[1]:
                        human_card = card_value
                        if current_card_index < len(cards):
                            current_card_index += 1
                            computer_card = computer_card_choice(cards[current_card_index - 1])
                            revealed_score_card = cards[current_card_index - 1]
                            display_current_card()
                            screen.blit(selected_card_image, card_rects[str(human_card)])
                            pygame.display.flip()
                            click_count += 1
                            human_score, computer_score = add_score(human_score, computer_score, human_card, computer_card, revealed_score_card)
                            if click_count == 13:
                                display_winners(human_score, computer_score)
                        #print("HUMAN: {h}; COMPUTER: {c}; Revealed: {r}".format(h=human_card, c=computer_card, r=revealed_score_card))
                        break
                if mouse_x in home_button_range_x and mouse_y in home_button_range_y:
                    main_screen()

def clubs_page():
    current_card_index = 0
    screen.fill(background_color)
    font = pygame.font.SysFont(None, 42)
    text = font.render("Choose a Card", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 240))
    screen.blit(text, text_rect)

    cards = diamond_cards_shuffle()

    def display_current_card():
        revealed_card_width = 125
        revealed_card_height = 175
        if current_card_index < len(cards):
            revealed_card = cards[current_card_index]
            diamond_card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Diamonds\{}.png".format(revealed_card))
            diamond_card_image = pygame.transform.scale(diamond_card_image, (revealed_card_width, revealed_card_height))
            diamond_card_button_rect = diamond_card_image.get_rect(center=(width // 2 - 260, height // 2 - 100))
            screen.blit(diamond_card_image, diamond_card_button_rect)
            pygame.display.flip()
        else:
            pass

    display_current_card()

    # Display next button
    home_button_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\HomeButton.png")
    home_button_image = pygame.transform.scale(home_button_image, (200, 200))
    home_button_image_rect = home_button_image.get_rect(center=(width // 2 - 260, height // 2 + 200))
    screen.blit(home_button_image, home_button_image_rect)

    display_card_width = 90
    display_card_height = 140

    selected_card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\Joker.png")
    selected_card_image = pygame.transform.scale(selected_card_image, (display_card_width,display_card_height))

    card_rects = {}

    card_positions = [((width // 2 - 90, height // 2 - 115), "A"), ((width // 2 + 15, height // 2 - 115), "2"), ((width // 2 + 120, height // 2 - 115), "3"), ((width // 2 + 225, height // 2 - 115), "4"), ((width // 2 + 330, height // 2 - 115), "5"),
                      ((width // 2 - 90, height // 2 + 40), "6"), ((width // 2 + 15, height // 2 + 40), "7"), ((width // 2 + 120, height // 2 + 40), "8"), ((width // 2 + 225, height // 2 + 40), "9"), ((width // 2 + 330, height // 2 + 40), "10"), 
                      ((width // 2 - 90, height // 2 + 195), "J"), ((width // 2 + 15, height // 2 + 195), "Q"), ((width // 2 + 120, height // 2 + 195), "K")]
    
    for position, card_value in card_positions:
        card_image = pygame.image.load(r"C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Cards\Clubs\{}.png".format(card_value))
        card_image = pygame.transform.scale(card_image, (display_card_width, display_card_height))
        card_rect = card_image.get_rect(center=(position))
        card_rects[card_value] = card_rect
        screen.blit(card_image, card_rect)

    pygame.display.flip()

    button_ranges = {
        (range(266, 350), range(118, 244)) : "A",
        (range(378, 450), range(119, 247)) : 2, 
        (range(478, 558), range(123, 247)) : 3,
        (range(582, 666), range(117, 251)) : 4,
        (range(688, 772), range(119, 246)) : 5,
        (range(267, 354), range(276, 404)) : 6,
        (range(374, 457), range(277, 402)) : 7,
        (range(481, 560), range(278, 404)) : 8,
        (range(587, 665), range(275, 404)) : 9,
        (range(690, 771), range(275, 402)) : 10,
        (range(270, 352), range(431, 560)) : "J",
        (range(375, 458), range(429, 560)) : "Q",
        (range(482, 560), range(431, 564)) : "K"
    }

    home_button_range_x = range(81, 199)
    home_button_range_y = range(477, 520)

    human_card = 0
    revealed_score_card = 0
    computer_card = 0

    click_count = 0

    human_score = 0
    computer_score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #print("Mouse Position:", mouse_x, mouse_y)
                for button_range, card_value in button_ranges.items():
                    if mouse_x in button_range[0] and mouse_y in button_range[1]:
                        human_card = card_value
                        if current_card_index < len(cards):
                            current_card_index += 1
                            computer_card = computer_card_choice(cards[current_card_index - 1])
                            revealed_score_card = cards[current_card_index - 1]
                            display_current_card()
                            screen.blit(selected_card_image, card_rects[str(human_card)])
                            pygame.display.flip()
                            click_count += 1
                            human_score, computer_score = add_score(human_score, computer_score, human_card, computer_card, revealed_score_card)
                            if click_count == 13:
                                display_winners(human_score, computer_score)
                        #print("HUMAN: {h}; COMPUTER: {c}; Revealed: {r}".format(h=human_card, c=computer_card, r=revealed_score_card))
                        break
                if mouse_x in home_button_range_x and mouse_y in home_button_range_y:
                    main_screen()

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
    font_title = pygame.font.SysFont(None, 48)
    font_text = pygame.font.SysFont(None, 24)

    # Title
    title_text = font_title.render("How to Play this Game?", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(width // 2, height // 2 - 175))
    screen.blit(title_text, title_rect)

    instructions = [
        "1. Choose a Suit",
        "2. From the given set of cards, choose a card to use to bid the displayed diamond card.",
        "3. Remember that a computer with a strategy to play this game is competing with you.",
        "4. For each displayed diamond card, the score on the diamond",
        "card will go to the player that bids the highest.",
        "5. At the end of the game, the total scores of the players are calculated and the winner is displayed."
    ]
    y_offset = 50
    for instruction in instructions:
        instruction_text = font_text.render(instruction, True, (0, 0, 0))
        instruction_rect = instruction_text.get_rect(center=(width // 2, height // 2 - 150 + y_offset))
        screen.blit(instruction_text, instruction_rect)
        y_offset += 30

    font_tag = pygame.font.SysFont(None, 35)
    tag_text = font_tag.render("Outbid, Outsmart, Outplay: Dominate the Diamond Dash!", True, (255, 255, 255))
    tag_rect = tag_text.get_rect(center=(width // 2, height // 2 + 125))
    screen.blit(tag_text, tag_rect)

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


pygame.quit()
sys.exit()
