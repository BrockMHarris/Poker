
class table:
    def __init__(self,deck, size, community_cards = None):
        """
        creates a hand of cards that can be used by all players

        :param deck: (list of card objects) deck to draw from
        :param size: (int) how many cards to put in the hand
        :param community_cards: (optional)(list of card objects) desired community cards (for testing)
        """
        if community_cards == None:
            self.community_hand = deck.deal_hand(size)
        else:
            self.community_hand = community_cards

    def get_card(self, card_number):
        """
        returns the cards int that place in the table usually 0-5
        :param card_number: (int) the place in the list of the desired card
        :return: returns desired card
        :rtype: (card object)
        """
        return self.community_hand[card_number]

    def get_size(self):
        """
        :return: size of the hand
        :rtype: int
        """
        return len(self.community_hand)

    def get_list(self):
        """
        :return: list of cards contained in the table
        :rtype: [card, card, card, card, card]
        """
        return self.community_hand

    def __str__(self):
        return_string = 'Community Cards: '
        for card in self.community_hand:
            return_string += card.__str__()
            return_string += "; "
        return return_string

    def __repr__(self):
        return self.__str__()