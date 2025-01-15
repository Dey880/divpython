import os
import random
import time
from Card_Art import cards_art, hidden

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

INITIAL_CASH = 5000

deck = [
    "ace of hearts", "two of hearts", "three of hearts", "four of hearts", "five of hearts", "six of hearts", "seven of hearts", "eight of hearts", "nine of hearts", "ten of hearts", 
    "jack of hearts", "queen of hearts", "king of hearts",
    "ace of spades", "two of spades", "three of spades", "four of spades", "five of spades", "six of spades", "seven of spades", "eight of spades", "nine of spades", "ten of spades", 
    "jack of spades", "queen of spades", "king of spades",
    "ace of diamonds", "two of diamonds", "three of diamonds", "four of diamonds", "five of diamonds", "six of diamonds", "seven of diamonds", "eight of diamonds", "nine of diamonds", "ten of diamonds", 
    "jack of diamonds", "queen of diamonds", "king of diamonds",
    "ace of clubs", "two of clubs", "three of clubs", "four of clubs", "five of clubs", "six of clubs", "seven of clubs", "eight of clubs", "nine of clubs", "ten of clubs", 
    "jack of clubs", "queen of clubs", "king of clubs"
]

cash = INITIAL_CASH
max_cash = cash
total_won = 0

def shuffle_deck():
    print("\nShuffling the deck...")
    time.sleep(1)
    random.shuffle(deck)

def deal_cards():
    current_deck = deck.copy()
    dealer_open = random.choice(current_deck)
    current_deck.remove(dealer_open)
    player1 = random.choice(current_deck)
    current_deck.remove(player1)
    dealer_closed = random.choice(current_deck)
    current_deck.remove(dealer_closed)
    player2 = random.choice(current_deck)
    current_deck.remove(player2)
    return dealer_open, dealer_closed, player1, player2, current_deck

def print_cards(*cards):
    card_lines = [card.strip().split('\n') for card in cards]
    card_height = len(card_lines[0])
    for i in range(card_height):
        print("  ".join(card[i] for card in card_lines))

def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        card_name = card.split()[0]
        if card_name == 'ace':
            ace_count += 1
            value += 11
        elif card_name in ('jack', 'queen', 'king'):
            value += 10
        else:
            value += int({
                'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
            }[card_name])

    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

def play():
    global cash, max_cash, total_won
    while cash > 0:
        clear()
        print(f"Your current cash: ${cash}")
        print("-" * 40)

        while True:
            try:
                bet = int(input(f"Place your bet (1-{cash}): $"))
                if 1 <= bet <= cash:
                    break
                print("Invalid bet amount. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

        cash -= bet

        shuffle_deck()
        dealer_open, dealer_closed, player1, player2, current_deck = deal_cards()
        print("-"*40)
        print("\nDealer's Hand:")
        print_cards(cards_art[dealer_open], hidden)

        player_hand = [player1, player2]
        split_hands = [player_hand]

        if player_hand[0].split()[0] == player_hand[1].split()[0]:
            split_choice = input("Do you want to split your hand? (y/n): ").lower()
            if split_choice == 'y':
                split_hands = [[player_hand[0]], [player_hand[1]]]
                print("You chose to split!")

        for hand in split_hands:
            play_hand(hand, bet, current_deck, dealer_open, dealer_closed)

        if cash == 0:
            print("You're out of cash. Game over!")
            break

        if input("Play another round? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break

def play_hand(player_hand, bet, current_deck, dealer_open, dealer_closed, das=False):
    global cash, total_won
    doubled = False
    split_hands = [player_hand]

    for hand in split_hands:
        while True:
            print("\nYour Hand:")
            print_cards(*[cards_art[card] for card in hand])
            hand_value = calculate_hand_value(hand)
            print(f"Your hand value: {hand_value}")

            if len(player_hand) == 2 and hand_value not in [10, 11]:
                card1_value = player_hand[0].split()[0]
                card2_value = player_hand[1].split()[0]
                if card1_value == card2_value:
                    split_choice = input("Do you want to split your hand? (y/n): ").lower()
                    if split_choice == 'y':
                        split_hands = [[player_hand[0]], [player_hand[1]]]
                        print("You chose to split!")

            if len(hand) == 2 and not doubled and hand_value in [9, 10, 11] and bet <= cash:
                action = input("(1) Hit  (2) Stand  (3) Double Down: ").strip()
            else:
                action = input("(1) Hit  (2) Stand: ").strip()

            if action == '2':
                break
            elif action == '1':
                new_card = random.choice(current_deck)
                current_deck.remove(new_card)
                hand.append(new_card)
                print("-"*40)
                print("\nYou drew:")
                print_cards(cards_art[new_card])
                hand_value = calculate_hand_value(hand)
                if hand_value > 21:
                    print("-"*40)
                    print("You busted!")
                    print_final_hands(player_hand, hand, dealer_open, dealer_closed)
                    return
            elif action == '3' and not doubled and len(hand) == 2 and hand_value in [9, 10, 11] and bet <= cash:
                double_bet = min(bet, cash)
                cash -= double_bet
                bet += double_bet
                doubled = True
                print(f"You doubled down! New bet: ${bet}")
                new_card = random.choice(current_deck)
                current_deck.remove(new_card)
                hand.append(new_card)
                break

    dealer_hand = [dealer_open, dealer_closed]


    while calculate_hand_value(dealer_hand) < 17:
        new_card = random.choice(current_deck)
        current_deck.remove(new_card)
        dealer_hand.append(new_card)

    print("-"*40)
    print("\nDealer's Hand:")
    print_cards(*[cards_art[card] for card in dealer_hand])
    
    dealer_value = calculate_hand_value(dealer_hand)
    player_value = calculate_hand_value(hand)
    clear()
    print("\nFinal Results:")
    print_final_hands(player_hand, hand, dealer_open, dealer_closed)
    print(f"Dealer's total: {dealer_value}")
    print(f"Your total: {player_value}")

    if player_value > 21:
        print("You busted! Dealer wins.")
    elif dealer_value > 21 or player_value > dealer_value:
        print("You win!")
        cash += bet * 2
        total_won += bet
    elif player_value == dealer_value:
        print("Push")
        cash += bet
    else:
        print("Dealer wins.")


def print_final_hands(player_hand, hand, dealer_open, dealer_closed):
    dealer_cards = [dealer_open, dealer_closed]
    player_cards = hand
    

    for card in dealer_cards + player_cards:
        if card not in cards_art:
            print(f"Invalid card: {card}")
        else:
            pass

    print("\nDealer's Hand:")
    print_cards(*[cards_art[card] for card in dealer_cards])
    
    print("\nYour Hand:")
    print_cards(*[cards_art[card] for card in player_cards])

play()