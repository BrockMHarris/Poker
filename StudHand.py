# I affirm that I have carried out my academic endeavors with full academic honesty -Brock Harris

import combo_finder
import FiveCardHand

class StudHand:
    def __init__(self, deck, table, hand_size, hand_a = None):
        """
        This creates a seven card by putting the cards in the table object in a list with 2 randomly generated cards
        :param deck: list of 52 cards
        :param table: list of cards that both player have acces to
        :param hand_size: the size of the desired player hand
        :param hand_a: this is optional, pass in a list that is the players hand (for testing)
        """
        if hand_a == None:
            self.player_hand = deck.deal_hand(hand_size)
        else:
            self.player_hand = hand_a

        self.community_cards = table
        self.seven_card_hand = table.get_list() + self.player_hand

    def _get_all_five_card_hands(self):
        return combo_finder.get_combinations(self.seven_card_hand ,5)

    def _convert_lists_to_cards(self):
        all_hand_objects = list()
        for hand in self._get_all_five_card_hands():
            all_hand_objects.append(FiveCardHand.FiveCardHand(hand))
        return all_hand_objects

    def _get_best_five_card_hand(self):
        hands = self._convert_lists_to_cards()
        #print len(hands)
        best_so_far = hands[0]

        for i in range(1, len(hands)):
            if hands[i].compare_to(best_so_far) < 0:
                best_so_far = hands[i]

        return best_so_far

    def compare_to(self, seven_card_hand):
        """
        Compares the best 5 card hand of the seven card hand to the best 5 card hand of a given seven card hand
        :param seven_card_hand: 5 community cards plus 2 player cards
        :return: -1 if the calling hand wins, 1 if parameter hand wins, and 0 if nobody wins
        """
        best_hand_a = self._get_best_five_card_hand()
        best_hand_b = seven_card_hand._get_best_five_card_hand()
        return best_hand_a.compare_to(best_hand_b)

    def is_pair(self):
        """
        determines if there is a pair in the hand
        :return: if there is returns the value, if not returns None
        """
        return self._get_best_five_card_hand().is_pair()
    def is_two_pair(self):
        """
        determines if there is a 2 pair in the hand
        :return: returns a list of the ranks of the two pairs or None if there is none
        """
        return self._get_best_five_card_hand().is_twoPair()
    def is_flush(self):
        """
        this function check the hand to determin if all the suits are the same

        :return: it return the high card if there is a flush otherwise returns None
        """
        return self._get_best_five_card_hand().is_flush()
    def is_high_card(self):
        """
        This check that the the hand has no pairs, 2 pairs, or flushes
        :return: returns True if the hand has no pairs or flushes, returns false otherwise
        """
        return self._get_best_five_card_hand().is_highCard()



    def __str__(self):
        """
        turns the list of cards into human readable list
        :return: a string representation of the hand in human readable form
        """
        return_string = ''
        for card in self.player_hand:
            return_string += card.__str__()

        return return_string

