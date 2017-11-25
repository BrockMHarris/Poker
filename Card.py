# I affirm that I have carried out my academic endeavors with full academic honesty -Brock Harris

class Card:
    def __init__(self, rank, suit):
        """
        creates a card with a rank and suit
        :param rank: (int) 1-14
        :param suit: (str) s,p,d,c
        """
        self.suit = suit
        self.rank = rank

    def get_card_elem(self, elem):
        """
        get a the suit or rank of the card
        :param elem: (str) 'rank' or 'suit'
        :return: the suit or rank of the card
        :rtype: str or int
        """
        if elem == 'rank':
            return self.rank
        elif elem == 'suit':
            return self.suit

    def __str__(self):
        """
        :return: the card into human readable form
        """
        readable_card = "("

        if (self.rank == 11):
            readable_card += ("Jack")
        elif (self.rank == 12):
            readable_card +=("Queen")
        elif (self.rank == 13):
            readable_card += ("King")
        elif (self.rank == 14):
            readable_card += ("Ace")
        else:
            readable_card += str(self.rank)

        readable_card += " of "

        if (self.suit == 'c'):
            readable_card += ("Clubs")
        elif (self.suit == 's'):
            readable_card += ("Spades")
        elif (self.suit == 'h'):
            readable_card += ("Hearts")
        elif (self.suit == 'd'):
            readable_card += ("Diamonds")
        else:
            readable_card += str(self.suit)

        readable_card += ")"

        return readable_card
