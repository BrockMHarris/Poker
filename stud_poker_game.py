# I affirm that I have carried out my academic endeavors with full academic honesty -Brock Harris
import StudHand as hand
import table
import Deck as deck

def print_cards(community_hand, hand_a, hand_b):
    print("-------------------------")

    print community_hand
    print
    print("hand A: " + str(hand_a))
    print("hand B: " + str(hand_b))

    print("\n")

def print_input():
    print ("What to type \n   if Hand A: A \n   if Hand B: B \n   if Nobody: None \n")

    predicted_winner = raw_input("Who is the winner: ")
    while predicted_winner != "A" and predicted_winner != "B" and predicted_winner != "None":
        predicted_winner = raw_input("choose A,B, or None: ")
    return predicted_winner

def is_not_correct(actual_winner, predicted_winner):
    if actual_winner == -1:
        actual_winner_readable = 'A'
    elif actual_winner == 0:
        actual_winner_readable = 'None'
    else:
        actual_winner_readable = 'B'

    return predicted_winner != actual_winner_readable

def print_loser(score):
    print("\n=========================")
    print("YOU LOSE!!")
    print("Score: " + str(score))

def start_game():
    """
    this runs the game
    :return: nothing
    """
    print("Welcome to the game of life(Semi-Poker)")
    game_state = 0
    YOU_LOSE = 1
    new_deck = deck.Deck()
    new_deck_size = new_deck.size()

    while game_state != YOU_LOSE:
        score = 0
        for num in range(int(new_deck_size/9)):

            community_hand = table.table(new_deck, 5)
            hand_a = hand.StudHand(new_deck, community_hand, 2)
            hand_b = hand.StudHand(new_deck, community_hand, 2)

            print_cards(community_hand,hand_a,hand_b)

            actual_winner = hand_a.compare_to(hand_b)

            predicted_winner = print_input()

            if is_not_correct(actual_winner,predicted_winner):
                game_state = YOU_LOSE
                print_loser(score)
                return
            score += 1
        print("You win!")
        return
start_game()
