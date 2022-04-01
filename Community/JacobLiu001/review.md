# Code review for Nick's code on Farkle
Hi Nick! I am a huge fan of your work and when binging your videos I saw the Farkle video, and found that you set up a GitHub repository for us! I saw this as an opportunity to contribute to your community, so I wrote up a little code review on how the code can be improved.

Disclaimer: I am a computer science *student* and have been learning coding for only 8 years. This code review represent only my opinions. If you are not comfortable with or not interested in code reviews, don't bother to read it: I won't be upset as I would rather your time be used on something more productive.

I have written this code review in the style I have seen on [Code Review StackExchange](https://codereview.stackexchange.com/).

## Code Review Starts Here

### Code style:
The conventions that should be followed are those specified in [PEP8 - Style Guide for Python](https://peps.python.org/pep-0008/).

Variables and methods (functions) use `snake_case`, where each word is lowercase and words are separated using an underscore.

In a traditional code review I would have listed every infringement of the conventions. However, your naming style is consistent. I would guess that you came from another language, maybe Pascal? So I wouldn't be so harsh, but my code would follow traditional python rules.

Type annotation: https://www.python.org/dev/peps/pep-0484/, feel free to skip.
Type annotations are optional, but recommended, as they tell your code editor what to expect and provide better code completion, as well as improve the readability of the code.

### Overall Algorithm:
The code hard-codes the number of dice and uses multiply nested for-loops, which is not very ideal. Therefore a constant `NUM_DICE = 6` can be introduced.

The code also uses `numpy` instead of stock python, but `numpy`-specific features are not used. `numpy` is an extremely powerful library providing linear algebra capabilities.

The numpy features used here can be implemented in pure python quite easily. Typically, using such powerful packages is avoided as long as it's possible. To use one of your analogies: why use a sledgehammer to open a nut? (In the Lagrangian Mechanics video)

### Possible Rolls
Deeply-nested for loops are not very popular.

Python has a standard built-in module called `itertools`. This module provides a function `product(A, B, ..., [repeat=1])`. This function returns the cartesian product of the input arguments (see official documentation [here](https://docs.python.org/3/library/itertools.html#itertools.product)).

So rolls can be generated with: `ROLLS = product(SIDE_VALUES, repeat=NUM_DICES)`, where each roll is not sorted. However, I think that sorting each roll in `ROLLS` does not make sense, as the sorting process is there only to benefit the categorization -- why not sort there?

### Count Scoring Rolls
There are two problems in the code:
- the current code has many repetitions, which is bad in programming -- the computer does the repetition, not the human!
- the current code is fragile: if there were a new rule it would be quite hard to introduce it.

There is not really a *best* way of doing it. However, there can be tricks to simplify the process.

A trick I spotted is to match long scoring dice first: The program can first look for patterns of length 6: six of a kind, Straight, two triplets, four of a kind + pair, three pairs; then patterns of length 5, then patterns of length 4, and so on. More concretely, the program would:

1. Let `unmatched` be the entire roll
2. Let `length_to_match` be 6
3. Let `match_result` be an empty list. This will store which patterns are matched.
4. while `unmatched` is not empty and `length_to_match >= 1`:
   1. For each pattern with length `length_to_match`
      1. Try to match the pattern
      2. If success, discard the matched parts from `unmatched`, and append the matched pattern to `match_result`
   2. decrement `length_to_match` by one
5. `match_result` can then be used to update the counters.

There are small optimizations here and there, and they would be explained in the code.

A python trick here is to use another standard library `collections`. It provides a `Counter` class that counts the number of elements in any iterable `arr` for you. It is dictionary-like, so once created, one can access the number of occurences of some element `x` simply with the following code.
```python
from collections import Counter
counter = Counter(some_iterable)
occurences_x = counter[x]
```

### Print results / Count Farkles

The original code did not need to have to count Farkles separately. Instead, in the main loop where the scoring rolls are counted, if a roll reaches the bottom of the if-else-if chain, it is a Farkle.

The modified code is similar: if `match_result` is empty, it is a farkle.

But, subtracting the number of all scoring cases from the total number of cases is a nice trick for verifying that the result is self-consistent.

