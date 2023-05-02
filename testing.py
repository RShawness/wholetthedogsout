import random

# Initialize the deck of cards
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

# Function to deal a card
def deal_card():
    card = random.choice(deck)
    deck.remove(card)
    return card

# Function to calculate the value of a hand
def calculate_hand(hand):
    value = 0
    ace_count = 0
    for card in hand:
        if card == 'A':
            ace_count += 1
            value += 11
        elif card in ['K', 'Q', 'J']:
            value += 10
        else:
            value += int(card)
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1
    return value

# Function to display the cards in the console
def show_cards(hand):
    for card in hand:
        print(card, end=' ')
    print()

# Function to check if the player wants to play again
def play_again():
    while True:
        choice = input('Do you want to play again? (Y/N) ')
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid choice. Please enter Y or N.')

# Start the game
play_game = True
while play_game:
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Show the cards
    print('Your cards:')
    show_cards(player_hand)
    print('Dealer cards:')
    print(dealer_hand[0], end=' ')
    print('X')

    # Player's turn
    while True:
        choice = input('Do you want to hit or stand? ')
        if choice.lower() == 'hit':
            player_hand.append(deal_card())
            show_cards(player_hand)
            if calculate_hand(player_hand) > 21:
                print('You bust!')
                break
        elif choice.lower() == 'stand':
            break

    # Dealer's turn
    if calculate_hand(player_hand) <= 21:
        print('Dealer cards:')
        show_cards(dealer_hand)
        while calculate_hand(dealer_hand) < 17:
            dealer_hand.append(deal_card())
            show_cards(dealer_hand)
        if calculate_hand(dealer_hand) > 21:
            print('Dealer busts! You win!')
        elif calculate_hand(dealer_hand) > calculate_hand(player_hand):
            print('Dealer wins!')
        elif calculate_hand(dealer_hand) == calculate_hand(player_hand):
            print('It\'s a tie!')
        else:
            print('You win!')

    # Ask if the player wants to play again
    play_game = play_again()