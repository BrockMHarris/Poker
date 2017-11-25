# I affirm that I have carried out my academic endeavors with full academic honesty -Brock Harris


class FiveCardHand:

    def  __init__(self, cards):
        """
        Takes a list of card objects and puts them into a hand

        :param cards: list of tuples that represent a hand
        """

        sorted_cards = sorted(cards, key=lambda x: x.get_card_elem('rank'),reverse=True)
        #print sorted_cards[0].__str__()
        #print sorted_cards[1].__str__()
        #print sorted_cards[2].__str__()
        self.hand = sorted_cards
        self.HIGH_CARD = 0
        self.PAIR = 1
        self.TWO_PAIR = 2
        self.FLUSH = 3

    def is_pair(self):
        """
        This checks for a pair of cards in the hand it is passed

        :return: returns the rank if there is a pair and the None if not
        """
        count = 0
        len_hand = len(self.hand)
        while count < len_hand:
            forCount = count + 1
            while forCount < len_hand:
                if self.hand[count].get_card_elem('rank') == self.hand[forCount].get_card_elem('rank'):
                    #print(hand[count][0])
                    return self.hand[count].get_card_elem('rank')
                forCount+=1
            count+=1
        return None

    def is_flush(self):
        """
        this function check the hand to determin if all the suits are the same

        :return: it return the high card if there is a flush otherwise returns None
        """
        first = self.hand[0].get_card_elem('suit')
        suitNum = 0

        for index in range(len(self.hand)):
            if self.hand[index].get_card_elem('suit') == first:
                suitNum +=1
        if suitNum == 5:
            return self.hand[0].get_card_elem('rank')
        else:
            return None

    def is_twoPair(self):
        """
        This checks if there are two pairs in the hand

        :return: returns a list of the ranks of the two pairs or None if there is none
        """
        count = 0
        num_pairs = 0
        first_match = 0
        len_hand = len(self.hand)
        high_card = list()
        while count < len_hand:
            forCount = count + 1
            while forCount < len_hand:
                if self.hand[count].get_card_elem('rank') == self.hand[forCount].get_card_elem('rank') and self.hand[count].get_card_elem('rank') != first_match:
                    first_match = self.hand[count].get_card_elem('rank')
                    high_card.append(self.hand[count].get_card_elem('rank'))
                    #print(count)
                    num_pairs += 1
                    if num_pairs == 2:
                        return high_card
                forCount+=1
            count+=2
        return None


    def is_highCard(self):
        """
        This check that the the hand has no pairs 2 pairs or flushes
        :return: returns True if the hand has no pairs of flushes, returns false otherwise
        """
        return self.is_pair() == None and self.is_twoPair() == None and self.is_flush() == None


    def compare_to(self, hand_b):
        """
        This function determins the winner of the 2 hands passed to it

        :param hand_b: it is passed a list of 5 tuples that represent a hand with rank bieng 2-14 and suit bieng s,d,c,h
        :return: returns 0 if hand a is the winner 1 if hand be is the winner and 2 if there is no winner
        """
        HAND_A_WINS = -1
        HAND_B_WINS = 1
        NO_WINNERS = 0

        #print("working")

        hand_a_ranking = self.get_hand_ranking()
        hand_b_ranking = hand_b.get_hand_ranking()
        #print(hand_a_ranking)
        #print(hand_b_ranking)

        #print("working")

        for index in range(len(hand_a_ranking)):
            #print("working")
            #print(index)
            #print(len(hand_b))
            if hand_a_ranking[index] > hand_b_ranking[index]:
                return HAND_A_WINS
            elif hand_a_ranking[index] < hand_b_ranking[index]:
                return HAND_B_WINS
        return NO_WINNERS


    def get_ranks_in_hand(self):
        """
        puts the ranks for each card in a hand and puts them into a new list
        :param hand: a list of tuples
        :return: list of 5 integers
        """
        rank_hand = list()
        for index, elem in enumerate(self.hand):
            rank_hand.append(self.hand[index].get_card_elem(self.hand,'rank'))
        #print(rank_hand)
        return rank_hand

    def get_hand_ranking(self):
        """
        checks if it has pairs a flush or none and creates a list of integers that represent how good the hand is
        first number is 0 if the hand has a highcard, 1 if 1 pair, 2 if 2 pair, and 3 if flush
        second and third(if there is a 2 pair) numbers represent the rank of the pair or the highest card in the case of flush and highcard
        the rest of the list are integers that are the ranks of each of the cards in the hand
        :param hand: list of tuples that represent cards
        :return: a list with the format of {X,X,X(if first X is 2),x,x,x,x,x}
        """

        HIGH_CARD = 0
        PAIR = 1
        FLUSH = 3
        #print("working.")
        TWO_PAIR = 2
        #print("working..")
        hand_ranking = list()
        #print("working...")
        pair = self.is_pair()
        #print("working....")
        flush = self.is_flush()
        high_card = self.hand[0].get_card_elem('rank')
        #print("working.....")
        if (flush != None):
            hand_ranking.append(FLUSH)
            hand_ranking.append(flush)
        elif (self.is_twoPair() != None):
            two_pair = sorted(self.is_twoPair(), reverse=True)
            hand_ranking.append(TWO_PAIR)
            hand_ranking.append(two_pair)
        elif (pair != None):
            hand_ranking.append(PAIR)
            hand_ranking.append(pair)
        else:
            hand_ranking.append(HIGH_CARD)
            hand_ranking.append(high_card)
        for elem in self.hand:
            hand_ranking.append(elem.get_card_elem('rank'))
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



    def __str__(self):
        """
        turns the list of cards into human readable list

        :param hand: a list of tuple cards
        :return: a string represntation of the hand in human readable form
            """
        return_string = ''
        for card in self.hand:
            return_string += card.__str__()

        return return_string