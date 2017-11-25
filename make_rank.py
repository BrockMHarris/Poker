# I affirm that I have carried out my academic endeavors with full academic honesty -Brock Harris

import Deck as deck
import FiveCardHand as check

HIGH_CARD = 0
PAIR = 1
TWO_PAIR = 2
FLUSH = 3

def get_ranks_in_hand(hand):
    """
    puts the ranks for each card in a hand and puts them into a new list
    :param hand: a list of tuples
    :return: list of 5 integers
    """
    rank_hand = list()
    for index, elem in enumerate(hand):
        rank_hand.append(hand[index].get_card_elem(hand,'rank'))
    #print(rank_hand)
    return rank_hand

def get_hand_ranking(hand):
    """
    checks if it has pairs a flush or none and creates a list of integers that represent how good the hand is
    first number is 0 if the hand has a highcard, 1 if 1 pair, 2 if 2 pair, and 3 if flush
    second and third(if there is a 2 pair) numbers reprent the rank of the pair or the highest card in the case of flush and highcard
    the rest of the list are integers that are te ranks of each of the cards in the hand
    :param hand: list of tuples that represent cards
    :return: a list with the format of {X,X,X(if first X is 2),{x,x,x,x,x}}
    """
    hand_ranking = list()
    pair = hand.is_pair()
    flush = hand.is_flush(hand)
    high_card = hand[0][0]
    if (flush != None):
        hand_ranking.append(FLUSH)
        hand_ranking.append(flush)
    elif (hand.is_twoPair() != None):
        two_pair = sorted(hand.is_twoPair(), reverse=True)
        hand_ranking.append(TWO_PAIR)
        hand_ranking.append(two_pair)
    elif (pair != None):
        hand_ranking.append(PAIR)
        hand_ranking.append(pair)
    else:
        hand_ranking.append(HIGH_CARD)
        hand_ranking.append(high_card)
    for elem in hand.get_ranks_in_hand():
        hand_ranking.append(elem)
    #print(hand_ranking)
    return hand_ranking

def get_ranking(rank_list):
    """
    get the value at the index in the provided list
    :param rank_list: list of integers that represent the ranking of a hand
    :param index: specific index of the integer bieng looked for
    :return: return that integer
    """
    new_rank_list = list()
    for elem in rank_list:
        if isinstance(elem,list):
            for part in elem:
                new_rank_list.append(part)
        else:
            new_rank_list.append(elem)
    return new_rank_list
