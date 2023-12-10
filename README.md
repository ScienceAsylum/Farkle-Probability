# Calculating Roll Probabilties in Farkle (Game)
<a href="https://en.wikipedia.org/wiki/Farkle">Farkle</a> is a dice game involving 6 dice. Only certain dice combinations will score you points. On consecutive rolls, you can roll fewer dice to try increase your score before your turn is over. The programs in this project find all possible rolls for a given number of dice, then count how many of times each possible type of roll appears in the list. A &quot;Farkle&quot; is a roll with no scoring dice.

## Necessary Software
They're coded in Python 3.8, so make sure you have Python 3.8 or later installed.

## How to Use
Simply run the program and press enter to start. You'll get a list that looks like this:

```
 2 SIX-SIDED DICE

 List of Rolls:
 [1, 1]
 [1, 2]
 [1, 3]
 [1, 4]
 [1, 5]
 [1, 6]
 [2, 1]
 [2, 2]
 [2, 3]
 [2, 4]
 [2, 5]
 [2, 6]
 [3, 1]
 [3, 2]
 [3, 3]
 [3, 4]
 [3, 5]
 [3, 6]
 [4, 1]
 [4, 2]
 [4, 3]
 [4, 4]
 [4, 5]
 [4, 6]
 [5, 1]
 [5, 2]
 [5, 3]
 [5, 4]
 [5, 5]
 [5, 6]
 [6, 1]
 [6, 2]
 [6, 3]
 [6, 4]
 [6, 5]
 [6, 6]

 Number of Possible Rolls : 36

 One One : 1.0
 Five Five : 1.0
 One Five : 2.0
 One : 8.0
 Five : 8.0
 Farkles : 16.0
```

## Room for Improvement
I'd like to consolidate the programs into one single program that asks the user for a number of dice. Also, the code runs noticibly slower as the number of dice increases. It was certainly good enough for what I needed. Farkle only goes up to six dice, after all. The code doesn't scale well though, so I couldn't transform this into code that listed the number of possible rolls of, say, 20 dice. It would take far too long.

## Motivation for the Project
My wife and I play Farkle all the time. One day, we got several high-score rolls in the same game that we expected to be rare and it got us wondering: How rare are each of the scoring rolls? It took me down a rabbit of dice combinatorics, which culminated in this video:

<a href="https://youtu.be/zBa5TWXfDEo">
    <b>Dice Combinatorics, Explained Through Game Design</b></br>
    <img src="https://img.youtube.com/vi/zBa5TWXfDEo/mqdefault.jpg">
</a>

## License
This code is under the <a href="https://github.com/ScienceAsylum/Farkle-Probability/blob/main/LICENSE">GNU General Public License v3.0</a>.
