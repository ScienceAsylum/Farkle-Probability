#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#**************************** Reviewed by Jacob Liu ****************************
#*********************************** Apr 2022 **********************************
#*******************************************************************************

from itertools import product
from collections import Counter

# Constant declarations

NUMBER_TO_TEXT = ("Zero", "One", "Two", "Three", "Four", "Five", "Six")

NUM_DICES = 6
NUM_SIDES = 6
SIDE_VALUES = tuple(range(1, NUM_SIDES + 1)) # Tuple is an immutable list

ROLLS = product(SIDE_VALUES, repeat=NUM_DICES)

# f-strings are very cool: https://www.python.org/dev/peps/pep-0498/
# basically it automatically treats content inside curly brackets as code,
# evaluates the code, and replace the content with the result
print(f"{NUM_DICES} {NUMBER_TO_TEXT[NUM_SIDES]}-SIDED Dice")

# -------------- Generate each scoring pattern ----------------
# Generate each pattern in decreasing order of pattern length

all_patterns = [list() for _ in range(NUM_DICES+1)]
# all_patterns[i] is the list of pattern matchers of length i

# Each element in all_patterns[i] is a function.
# The function takes as input the list of dice values
# and returns a tuple with elements
#  - int: the score of the matched pattern, or 0 if not matched
#  - str: string_representation_of_the_pattern
# If the pattern is matched, the Counter for dice are updated.
# Counter objects are mutable, so they are passed by reference.
# Modifying them inside the function will modify the Counter object outside.

# all_patterns is a list of list of functions

# Feel free to collapse the code of each function. This makes the code clearer.

# ------------ LENGTH 6 -------------

def six_of_a_kind(dice_values: Counter):
    # Counter.most_common(n) returns a list of
    # tuples (element, count) of the most common n elements
    most_common_element, most_common_count = dice_values.most_common(1)[0]
    if most_common_count == 6:
        del dice_values[most_common_element]
        return (3000, "Six of a kind")
    return (0, "")

def straight(dice_values: Counter):
    # See if the dice values cover all side values
    # set(iterable) can be used to see what
    if set(dice_values.elements()) == (SIDE_VALUES):
        dice_values.clear()
        return (1500, "Straight")
    return (0, "")

def four_of_a_kind_plus_a_pair(dice_values: Counter):
    # A list interpretation is
    two_most_common = dice_values.most_common(2)
    if len(two_most_common) < 2:
        # There are no two distinct elements
        return (0, "")
    if two_most_common[0][1] == 4 and two_most_common[1][1] == 2:
        dice_values.clear()
        return (1500, "Four of a kind + a pair")
    return (0, "")

def two_triplets(dice_values: Counter):
    two_most_common = dice_values.most_common(2)
    if len(two_most_common) < 2:
        # There are no two distinct elements
        return (0, "")
    if two_most_common[0][1] == 3 and two_most_common[1][1] == 3:
        dice_values.clear()
        return (1500, "Two triplets")
    return (0, "")

def three_pairs(dice_values: Counter):
    three_most_common = dice_values.most_common(3)
    if len(three_most_common) < 3:
        # There are no two distinct elements
        return (0, "")
    for element, count in three_most_common:
        if count != 2:
            return (0, "")
    dice_values.clear()
    return (1500, "Three pairs")

all_patterns[6] = [six_of_a_kind, straight, four_of_a_kind_plus_a_pair, two_triplets, three_pairs]

# ------------ LENGTH 5 -------------

def five_of_a_kind(dice_values: Counter):
    most_common_element, most_common_count = dice_values.most_common(1)[0]
    if most_common_count == 5:
        del dice_values[most_common_element]
        return (2000, "Five of a kind")
    return (0, "")

all_patterns[5] = [five_of_a_kind]

# ------------ LENGTH 4 -------------

def four_of_a_kind(dice_values: Counter):
    most_common_element, most_common_count = dice_values.most_common(1)[0]
    if most_common_count == 4:
        del dice_values[most_common_element]
        return (1000, "Four of a kind")
    return (0, "")

all_patterns[4] = [four_of_a_kind]

# ------------ LENGTH 3 -------------

def triplet(dice_values: Counter):
    most_common_element, most_common_count = dice_values.most_common(1)[0]
    if most_common_count == 3:
        del dice_values[most_common_element]
        if most_common_element == 1:
            score = 300
        else:
            score = 100 * most_common_element
        return (score, f"Triple {NUMBER_TO_TEXT[most_common_element]}")
    return (0, "")

all_patterns[3] = [triplet]

# ------------ LENGTH 2 -------------
# There are no patterns of length 2

# ------------ LENGTH 1 -------------
def one(dice_values: Counter):
    number_of_ones = dice_values[1]
    if number_of_ones == 0:
        return (0, "")
    if number_of_ones == 1:
        del dice_values[1]
        return (100, "One")
    if number_of_ones == 2:
        del dice_values[1]
        return (200, "One + One")
    # If the code reaches here, a triplet of ones is not detected
    # so something has gone wrong, raise an exception
    raise Exception("Triplet detected while checking for ones")

def five(dice_values: Counter):
    number_of_ones = dice_values[5]
    if number_of_ones == 0:
        return (0, "")
    if number_of_ones == 1:
        del dice_values[1]
        return (50, "Five")
    if number_of_ones == 2:
        del dice_values[1]
        return (100, "Five + Five")
    # If the code reaches here, a triplet of ones is not detected
    # so something has gone wrong, raise an exception
    raise Exception("Triplet detected while checking for fives")

all_patterns[1] = [one, five]

# ---------- Count each type of scoring roll ------------------

# A Counter is a dictionary-like object that counts hashable objects.

# The counter can be treated as a dictionary
# that maps strings to integers with default 0.

# The keys are the rolls, and the values are the counts.
roll_counter = Counter()
number_of_rolls = 0
for roll in ROLLS:
    number_of_rolls += 1
    # Counter (from module collections) is a dictionary-like class
    # that counts the number of occurences of each element.
    counter = Counter(roll)
    unmatched = counter
    length_to_match = 6
    match_result = []
    match_score = 0

    # Match the roll with the patterns in decreasing order of length
    while length_to_match > 0:
        if len(list(counter.elements())) < length_to_match:
            length_to_match -= 1
            continue
        for pattern_matcher in all_patterns[length_to_match]:
            score, new_string = pattern_matcher(unmatched)
            if score:
                match_result.append(new_string)
                match_score += score
        length_to_match -= 1

    matched_pattern = ""
    if len(match_result) == 0: # If nothing matched
        matched_pattern = "Farkle (0)"
    else:
        matched_pattern = " + ".join(match_result)
        matched_pattern += f" ({match_score})"
    roll_counter[matched_pattern] += 1

# Print the results in decreasing order of frequency
total_counts = 0
for pattern, count in roll_counter.most_common():
    print(f"{pattern}: {count}")
    total_counts += count

# If they don't equal, this will throw an error
assert total_counts == number_of_rolls
