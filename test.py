# I affirm that I have carried out my academic endeavors with full academic honesty -Brock Harris

import FiveCardHand as check
import StudHand
import table
import Card

num_pass = 0
num_fail = 0

def assert_equals(msg, expected, actual):
    """
    Check whether code being tested produces
    the correct result for a specific test
    case. Prints a message indicating whether
    it does.
    :param: msg is a message to print at the beginning.
    :param: expected is the correct result
    :param: actual is the result of the
    code under test.
    """
    print(msg)
    print("expected: " + str(expected))
    print("actual: " + str(actual))

    global num_pass, num_fail

    if expected == actual:
        print("PASS")
        num_pass += 1
    else:
        print("**** FAIL")
        num_fail += 1

    print("")

def start_tests(header):
    """
    Initializes summary statistics so we are ready to run tests using
    assert_equals.
    :param header: A header to print at the beginning
    of the tests.
    """
    print(header)
    print("========")
    print("")
    num_pass = 0
    num_fail = 0

def Create_seven_card_hand(list_of_table_cards, hand):
    """
    Creates a seven card hand with specific cards that can be tested
    :param list_of_table_cards: (list of cards) desired community cards
    :param hand: (list of cards) desired player hand
    :return:  StudHand object with desired cards
    :rtype: StudHand
    """
    community_cards = list()
    new_hand = list()
    for tups in list_of_table_cards:
        community_cards.append(Card.Card(tups[0], tups[1]))
    for tups in hand:
        new_hand.append(Card.Card(tups[0],tups[1]))

    community_table = table.table([], 5, community_cards)
    seven_card_hand = StudHand.StudHand([], community_table, 2, new_hand)
    return seven_card_hand

def Create_five_card_hand(hand):
    """
    Creates a 5 card hadn with specific cards
    :param hand: (list of cards) desired player hand
    :return: FiveCardHand
    """
    new_hand = list()
    for tups in hand:
        new_hand.append(Card.Card(tups[0],tups[1]))
    new_hand = check.FiveCardHand(new_hand)
    return new_hand

def finish_tests():
    """
    Prints summary statistics after the tests are complete.
    """
    print("Passed %d/%d" % (num_pass, num_pass + num_fail))
    print("Failed %d/%d" % (num_fail, num_pass + num_fail))


start_tests("Testing Game")
community_cards = [(10, 'c'), (6, 'c'), (5, 'c'), (4, 'c'), (2, 'c')]
seven_card_hand_a = Create_seven_card_hand(community_cards, [(13, 'd'), (3, 's')])
seven_card_hand_b = Create_seven_card_hand(community_cards, [(13, 's'), (3, 'd')])
assert_equals("if both the hands are completely equal",0,seven_card_hand_a.compare_to(seven_card_hand_b))

community_cards = [(10, 'c'), (6, 'h'), (12, 's'), (4, 'd'), (2, 'c')]
seven_card_hand_a = Create_seven_card_hand(community_cards, [(12, 'd'), (4, 's')])
seven_card_hand_b = Create_seven_card_hand(community_cards, [(13, 's'), (3, 'd')])
assert_equals("if one hand has a two pair",-1,seven_card_hand_a.compare_to(seven_card_hand_b))

community_cards = [(10, 'c'), (6, 'c'), (5, 'c'), (4, 'd'), (2, 's')]
seven_card_hand_a = Create_seven_card_hand(community_cards, [(12, 's'), (4, 's')])
seven_card_hand_b = Create_seven_card_hand(community_cards, [(13, 'c'), (3, 'c')])
#print (seven_card_hand_a._get_best_five_card_hand())
#print (seven_card_hand_b._get_best_five_card_hand())
assert_equals("if a flush wins over a pair",1,seven_card_hand_a.compare_to(seven_card_hand_b))

community_cards = [(10, 'c'), (9, 'h'), (5, 'd'), (4, 's'), (2, 'c')]
seven_card_hand_a = Create_seven_card_hand(community_cards, [(12, 'd'), (3, 's')])
seven_card_hand_b = Create_seven_card_hand(community_cards, [(13, 's'), (3, 'd')])
assert_equals("this test the highcard",1,seven_card_hand_a.compare_to(seven_card_hand_b))

community_cards = [(12, 'c'), (6, 'h'), (5, 'd'), (4, 's'), (2, 'c')]
seven_card_hand_a = Create_seven_card_hand(community_cards, [(12, 'd'), (6, 's')])
seven_card_hand_b = Create_seven_card_hand(community_cards, [(12, 's'), (5, 'd')])
assert_equals("this test 2 pair with highcard",-1,seven_card_hand_a.compare_to(seven_card_hand_b))



hand_a = Create_five_card_hand([(10, 'c'), (6, 'c'), (5, 's'), (4, 'd'), (2, 'c')])
hand_b = Create_five_card_hand([(10, 'd'), (6, 's'), (5, 'c'), (4, 'c'), (2, 'd')])
assert_equals("if both the hands are completely equal",0,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(10, 'c'), (6, 'c'), (5, 'c'), (4, 'c'), (2, 'c')])
hand_b = Create_five_card_hand([(10, 'd'), (6, 's'), (5, 'c'), (4, 'c'), (2, 'd')])
assert_equals("if there is a flush in hand a",-1,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(10, 'c'), (10, 'c'), (5, 's'), (4, 'd'), (4, 'c')])
hand_b = Create_five_card_hand([(10, 'd'), (6, 's'), (5, 'c'), (4, 'c'), (2, 'd')])
assert_equals("if there is a two pair in hand a",-1,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(10, 'c'), (10, 'c'), (5, 's'), (5, 'd'), (2, 'c')])
hand_b = Create_five_card_hand([(10, 'd'), (10, 's'), (5, 'c'), (4, 'c'), (4, 'd')])
assert_equals("if there is a two pair in both hands",-1,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(10, 'c'), (10, 'c'), (5, 's'), (4, 'd'), (2, 'c')])
hand_b = Create_five_card_hand([(10, 'd'), (6, 's'), (5, 'c'), (4, 'c'), (2, 'd')])
assert_equals("if there is a pair in hand a",-1,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(10, 'c'), (10, 'c'), (5, 'c'), (4, 'c'), (2, 'c')])
hand_b = Create_five_card_hand([(10, 's'), (6, 's'), (5, 's'), (4, 's'), (2, 's')])
#print(rank.get_hand_ranking(hand_a))
#print(rank.get_hand_ranking(hand_b))
assert_equals("if there is 2 flushes",-1,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(10, 'c'), (6, 'c'), (5, 's'), (3, 'd'), (2, 'c')])
hand_b = Create_five_card_hand([(10, 'd'), (6, 's'), (5, 'c'), (4, 'c'), (2, 'd')])
assert_equals("if the cards are almost all the same",1,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(12, 'c'), (10, 'c'), (5, 's'), (4, 'd'), (2, 'c')])
hand_b = Create_five_card_hand([(10, 'd'), (6, 's'), (5, 'c'), (4, 'c'), (2, 'd')])
assert_equals("if theres only a highcard",-1,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(10, 'c'), (10, 'c'), (5, 's'), (5, 'd'), (2, 'c')])
hand_b = Create_five_card_hand([(14, 'd'), (5, 's'), (5, 'c'), (4, 'c'), (2, 'd')])
assert_equals("2 pair verse 1 pair",-1,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(5, 'c'), (14, 'c'), (3, 's'), (7, 'd'), (2, 'c')])
hand_b = Create_five_card_hand([(10, 'd'), (6, 's'), (5, 'c'), (4, 'c'), (2, 'd')])
#print(rank.get_hand_ranking(hand_a))
#print(rank.get_hand_ranking(hand_b))
assert_equals("Out of order high card",-1,hand_a.compare_to(hand_b))

hand_a = Create_five_card_hand([(12, 'h'), (11, 'd'), (9, 'h'), (8, 's'), (4, 's')])
hand_b = Create_five_card_hand([(13, 'h'), (11, 'h'), (10, 'h'), (7, 'c'), (2, 'c')])
assert_equals("highcard",1,hand_a.compare_to(hand_b))

finish_tests()
