# I affirm that I have carried out my academic endeavors with full academic honesty -Brock Harris

import Card as card
import random

class Deck:


    def __init__(self):
        """
        creates a deck of 52 cards
        :return: a list of 2 charactor tuples. The first element of every tuple is the rankin from 2-14 the second is the suit 'h','d','c','s'
        """
        self.new_deck = list()
        rank_list = (10,2,3,4,5,6,7,8,9,11,12,13,14)
        suit_list = "h","d","c","s"

        for ranks in rank_list:
            for suits in suit_list:
                self.new_deck.append(card.Card(ranks, suits))
        self.deck = self.new_deck
        #print(len(deck))

    def deal_hand(self, size):
        """
        takes 5 random cards from the deck and puts them into a new list called hand
        :param deck: this is a list of 52 unique tuples. The first element of every tuple is the rankin from 2-14 the second is the suit 'h','d','c','s' these represent cards
        :return: returns a card object
        """
        hand = list()
        used_cards = list()
        for cards in range(size):
            rand = self.deck[random.randint(0, len(self.deck) - 1)]
            hand.append(rand)
            self.deck.pop(self.deck.index(rand))
        #print(len(hand))
        return hand

    def size(self):
        return(len(self.deck))
