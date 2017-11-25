# I affirm that I have carried out my academic endeavors with full academic honesty -Brock Harris

# :author: Brock Harris

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def _list_with_one_list_inside(input_list):
    """
    Wraps the given list inside another list, and returns the new list.
    :param input_list: The list to wrap
    :return: A new list with a single element, which is the input_list.
    """
    new_list = list()
    new_list.append(input_list)
    return new_list


def _prepend_to_all_lists(prefix, list_of_lists_to_prepend):
    """
    Adds a prefix to each element of a list, returns a list of the new lists.
    :param prefix: A single element to prepend onto each list.
    :param list_of_lists_to_prepend: The list of the lists to prepend.
    :return: A list of lists, containing each of the lists from list_of_lists_to_prepend with the prefix prepended.
    """

    for l in list_of_lists_to_prepend:
        l.insert(0, prefix)

    return list_of_lists_to_prepend


# -----------------------------------------------------------------------------

def get_combinations(choose_from, target_len):
    """
    Gets all combinations of a given length chosen from a given list, returns a list of those combinations.

    :param choose_from: A list of elements to choose from.
    :param target_len: The target length of the combinations to find.
    :return: A list of lists, where each list is a combination of elements from choose_from of length target_len.
             Returns the empty list if choose_from is empty.
    """
    #total_lists = list()
    if len(choose_from) == target_len:
        return _list_with_one_list_inside(choose_from)
    elif len(choose_from) == 0:
        return []
    first = choose_from[0]
    rest = choose_from[1:]
    append_to_list_of_list = _prepend_to_all_lists(first, get_combinations(rest,target_len-1))
    list_of_list = get_combinations(rest, target_len)
    return list_of_list + append_to_list_of_list

def _test_combos(input_list, target_length):
    combos = get_combinations(input_list, target_length)
    print ("For list %s, %d combination(s) of length %d:\n     %s" % (str(input_list),
                                                                len(combos),
                                                                target_length,
                                                                str(combos)))
def _test_get_combinations():
    _test_combos(['a', 'b', 'c', 'd'], 4)
    _test_combos([], 4)
    print str(_prepend_to_all_lists('a', [['b'],['c'],['d','e']]))
    _test_combos(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 5)
    _test_combos(['a', 'b', 'c'], 2)



if __name__ == "__main__":
    _test_get_combinations()