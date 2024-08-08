from random import shuffle, choice

colors = ["R", "B", "Y", "G"]
cards = ["+2R", "+2B", "+2G", "+2Y", "SR", "SG", "SB", "SY", "RY", "RB", "RG", "RR"]
cards.extend(["+4"] * 4)
cards.extend(["CC"] * 4)
for color in colors:
    for number in range(0, 10):
        cards.append(f"{number}{color}")
shuffle(cards)

n = int(input("Enter the number of players: "))
c = int(input("Enter the number of cards per player: "))
players = []
for _ in range(n):
    curr_hand = []
    for _ in range(c):
        card = choice(cards)
        curr_hand.append(card)
        cards.remove(card)
    players.append(curr_hand)

game_pile = []
current_card = choice(cards)
game_pile.append(current_card)
cards.remove(current_card)
print("Starting card:", game_pile[-1])

current_player = 0
direction = 1

def draw_cards(num, player_index):
    for _ in range(num):
        if not cards:
            recycle_pile()
        card = choice(cards)
        players[player_index].append(card)
        cards.remove(card)

def recycle_pile():
    if len(game_pile) > 1:
        top_card = game_pile.pop()
        shuffle(game_pile)
        cards.extend(game_pile)
        shuffle(cards)
        game_pile.clear()
        game_pile.append(top_card)
        print("Recycled the game pile back into the deck.")

while True:
    print(f"\nPlayer {current_player + 1}'s turn. Your hand: {players[current_player]}")
    print("Top card on the pile:", game_pile[-1])
    
    valid_move = False
    while not valid_move:
        turn = input("Enter your card to play (or type 'draw' to draw a card): ").upper()
        if turn == "DRAW":
            draw_cards(1, current_player)
            print(f"You drew a card. Your new hand: {players[current_player]}")
            valid_move = True
            break
        if turn not in players[current_player]:
            print("You don't have this card! Try again.")
            continue
        if turn == "CC":
            chosen_color = input("Choose a color (R, B, Y, G): ").upper()
            if chosen_color in colors:
                game_pile.append(chosen_color)
                players[current_player].remove(turn)
                valid_move = True
            else:
                print("Invalid color. Please choose from R, B, Y, G.")
                while chosen_color not in colors:
                    chosen_color = input("Choose a color (R, B, Y, G): ").upper()
                    if chosen_color in colors:
                        game_pile.append(chosen_color)
                        players[current_player].remove(turn)
                        valid_move = True
        elif turn == "+4":
            draw_cards(4, (current_player + direction) % n)
            print(f"Player {(current_player + direction) % n + 1} drew 4 cards.")
            chosen_color = input("Choose a color (R, B, Y, G): ").upper()
            if chosen_color in colors:
                game_pile.append(chosen_color)
                players[current_player].remove(turn)
                valid_move = True
            else:
                print("Invalid color. Please choose from R, B, Y, G.")
                while chosen_color not in colors:
                    chosen_color = input("Choose a color (R, B, Y, G): ").upper()
                    if chosen_color in colors:
                        game_pile.append(chosen_color)
                        players[current_player].remove(turn)
                        valid_move = True
        elif turn.startswith("+2") and turn[-1] == game_pile[-1][-1]:
            draw_cards(2, (current_player + direction) % n)
            print(f"Player {(current_player + direction) % n + 1} drew 2 cards.")
            game_pile.append(turn)
            players[current_player].remove(turn)
            valid_move = True
        elif turn.startswith("S") and turn[-1] == game_pile[-1][-1]:
            game_pile.append(turn)
            players[current_player].remove(turn)
            current_player = (current_player + direction) % n
            valid_move = True
        elif turn[-1] == game_pile[-1][-1] or turn[:-1] == game_pile[-1][:-1]:
            game_pile.append(turn)
            players[current_player].remove(turn)
            valid_move = True
        else:
            print("Invalid card! Try again.")
    
    if not players[current_player]:
        print(f"Player {current_player + 1} wins!")
        break
    
    current_player = (current_player + direction) % n
    
    if len(cards) < 5:
        recycle_pile()
