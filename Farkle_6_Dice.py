#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Jan 2021 **********************************
#*******************************************************************************
import numpy as np
input("\n Press enter to continue.")

#---------------------------- Conditions ----------------------------
Num_Sides = 6
print("\n 6 SIX-SIDED DICE")

#-------------------------- Possible Rolls --------------------------
Rolls = []
SideValues = np.arange(1,Num_Sides+1,1)

print("\n List of Rolls:")
for Die_1 in SideValues:
    for Die_2 in SideValues:
        for Die_3 in SideValues:
            for Die_4 in SideValues:
                for Die_5 in SideValues:
                    for Die_6 in SideValues:
                        Roll = sorted([Die_1,Die_2,Die_3,Die_4,Die_5,Die_6])
                        Rolls.append(Roll)
                        print("", Roll)

print("\n Number of Possible Rolls :", len(Rolls), "\n")

#------------------------ Count Scoring Rolls -----------------------
ScoringRolls = ["Six of a Kind","Straight",
                
                "Five of a Kind +One","Five of a Kind +Five",
                
                "Five of a Kind",
                
                "Four of a Kind +Pair","Four of a Kind +OneFive",
                
                "Four of a Kind +One","Four of a Kind +Five",
                
                "Four of a Kind",
                
                "Two Triplets",
                
                "Triple Two +OneOneFive","Triple Three +OneOneFive",
                "Triple Four +OneOneFive","Triple Six +OneOneFive",
                
                "Triple Two +OneFiveFive","Triple Three +OneFiveFive",
                "Triple Four +OneFiveFive","Triple Six +OneFiveFive",
                
                "Triple Two +OneOne","Triple Three +OneOne",
                "Triple Four +OneOne","Triple Five +OneOne",
                "Triple Six +OneOne",
                
                "Triple One +FiveFive","Triple Two +FiveFive",
                "Triple Three +FiveFive","Triple Four +FiveFive",
                "Triple Six +FiveFive",
                
                "Triple Two +OneFive","Triple Three +OneFive",
                "Triple Four +OneFive","Triple Six +OneFive",
                
                "Triple Two +One","Triple Three +One","Triple Four +One",
                "Triple Five +One","Triple Six +One",
                
                "Triple One +Five","Triple Two +Five","Triple Three +Five",
                "Triple Four +Five","Triple Six +Five",
                
                "Triple One","Triple Two","Triple Three",
                "Triple Four","Triple Five","Triple Six",
                
                "Three Pairs",
                
                "One One Five Five",
                
                "One One Five","One Five Five",
                
                "One One","Five Five","One Five",
                
                "One","Five"]
ScoringCounts = np.zeros( len(ScoringRolls) )

for Roll in Rolls:
    #Six of a Kind
    if Roll.count(Roll[0]) == len(Roll):
        ScoringCounts[0] += 1

    #1-6 Straight
    elif Roll == [1,2,3,4,5,6]:
        ScoringCounts[1] += 1

    #Five of a Kind +1,+5
    elif Roll[0] == 1 and Roll[1:].count(Roll[1]) == 5:
        ScoringCounts[2] += 1
    elif ( Roll[:5].count(Roll[0]) == 5 and Roll[5] == 5) or Roll == [5,6,6,6,6,6]:
        ScoringCounts[3] += 1

    #Five of a Kind
    elif Roll[:5].count(Roll[0]) == 5 or Roll[1:].count(Roll[1]) == 5:
        ScoringCounts[4] += 1

    #Four of a Kind +Pair
    elif ( Roll[:2].count(Roll[0]) == 2 and Roll[2:].count(Roll[2]) == 4 ) or ( Roll[:4].count(Roll[0]) == 4 and Roll[4:].count(Roll[4]) == 2 ):
        ScoringCounts[5] += 1

    #Four of a Kind +15
    elif ( Roll[0] == 1 and Roll[1:5].count(Roll[1]) == 4 and Roll[5] == 5 ) or Roll == [1,5,6,6,6,6]:
        ScoringCounts[6] += 1

    #Four of a Kind +1,+5
    elif Roll[0] == 1 and ( Roll[1:5].count(Roll[1]) == 4 or Roll[2:].count(Roll[2]) == 4 ):
        ScoringCounts[7] += 1
    elif Roll.count(5) == 1 and ( Roll[:4].count(Roll[0]) == 4 or Roll[1:5].count(Roll[1]) == 4 or Roll[2:].count(Roll[2]) == 4 ):
        ScoringCounts[8] += 1

    #Four of a Kind
    elif Roll[:4].count(Roll[0]) == 4 or Roll[1:5].count(Roll[1]) == 4 or Roll[2:].count(Roll[2]) == 4:
        ScoringCounts[9] += 1

    #Two Triplets
    elif Roll[:3].count(Roll[0]) == 3 and Roll[3:].count(Roll[3]) == 3:
        ScoringCounts[10] += 1

    #Triples +115
    elif Roll == [1,1,2,2,2,5]:
        ScoringCounts[11] += 1
    elif Roll == [1,1,3,3,3,5]:
        ScoringCounts[12] += 1
    elif Roll == [1,1,4,4,4,5]:
        ScoringCounts[13] += 1
    elif Roll == [1,1,5,6,6,6]:
        ScoringCounts[14] += 1

    #Triples +155
    elif Roll == [1,2,2,2,5,5]:
        ScoringCounts[15] += 1
    elif Roll == [1,3,3,3,5,5]:
        ScoringCounts[16] += 1
    elif Roll == [1,4,4,4,5,5]:
        ScoringCounts[17] += 1
    elif Roll == [1,5,5,6,6,6]:
        ScoringCounts[18] += 1

    #Triples +11
    elif Roll[:2] == [1,1] and Roll[2:].count(2) == 3:
        ScoringCounts[19] += 1
    elif Roll[:2] == [1,1] and Roll[2:].count(3) == 3:
        ScoringCounts[20] += 1
    elif Roll[:2] == [1,1] and Roll[2:].count(4) == 3:
        ScoringCounts[21] += 1
    elif Roll[:2] == [1,1] and Roll[2:].count(5) == 3:
        ScoringCounts[22] += 1
    elif Roll[:2] == [1,1] and Roll[2:].count(6) == 3:
        ScoringCounts[23] += 1

    #Triples +55
    elif Roll.count(5) == 2 and Roll.count(1) == 3:
        ScoringCounts[24] += 1
    elif Roll.count(5) == 2 and Roll.count(2) == 3:
        ScoringCounts[25] += 1
    elif Roll.count(5) == 2 and Roll.count(3) == 3:
        ScoringCounts[26] += 1
    elif Roll.count(5) == 2 and Roll.count(4) == 3:
        ScoringCounts[27] += 1
    elif Roll.count(5) == 2 and Roll.count(6) == 3:
        ScoringCounts[28] += 1

    #Triples +15
    elif Roll.count(1) == 1 and Roll.count(5) == 1 and Roll.count(2) == 3:
        ScoringCounts[29] += 1
    elif Roll.count(1) == 1 and Roll.count(5) == 1 and Roll.count(3) == 3:
        ScoringCounts[30] += 1
    elif Roll.count(1) == 1 and Roll.count(5) == 1 and Roll.count(4) == 3:
        ScoringCounts[31] += 1
    elif Roll.count(1) == 1 and Roll.count(5) == 1 and Roll.count(6) == 3:
        ScoringCounts[32] += 1

    #Triples +1
    elif Roll[0] == 1 and Roll.count(2) == 3:
        ScoringCounts[33] += 1
    elif Roll[0] == 1 and Roll.count(3) == 3:
        ScoringCounts[34] += 1
    elif Roll[0] == 1 and Roll.count(4) == 3:
        ScoringCounts[35] += 1
    elif Roll[0] == 1 and Roll.count(5) == 3:
        ScoringCounts[36] += 1
    elif Roll[0] == 1 and Roll.count(6) == 3:
        ScoringCounts[37] += 1

    #Triples +5
    elif Roll.count(5) == 1 and Roll.count(1) == 3:
        ScoringCounts[38] += 1
    elif Roll.count(5) == 1 and Roll.count(2) == 3:
        ScoringCounts[39] += 1
    elif Roll.count(5) == 1 and Roll.count(3) == 3:
        ScoringCounts[40] += 1
    elif Roll.count(5) == 1 and Roll.count(4) == 3:
        ScoringCounts[41] += 1
    elif Roll.count(5) == 1 and Roll.count(6) == 3:
        ScoringCounts[42] += 1

    #Triples
    elif Roll.count(1) == 3:
        ScoringCounts[43] += 1
    elif Roll.count(2) == 3:
        ScoringCounts[44] += 1
    elif Roll.count(3) == 3:
        ScoringCounts[45] += 1
    elif Roll.count(4) == 3:
        ScoringCounts[46] += 1
    elif Roll.count(5) == 3:
        ScoringCounts[47] += 1
    elif Roll.count(6) == 3:
        ScoringCounts[48] += 1

    #Triples
    elif Roll[0] == Roll[1] and Roll[2] == Roll[3] and Roll[4] == Roll[5]:
        ScoringCounts[49] += 1

    #1155
    elif Roll.count(1) == 2 and Roll.count(5) == 2:
        ScoringCounts[50] += 1

    #115,155
    elif Roll.count(1) == 2 and Roll.count(5) == 1:
        ScoringCounts[51] += 1
    elif Roll.count(1) == 1 and Roll.count(5) == 2:
        ScoringCounts[52] += 1

    #11,55,15
    elif Roll.count(1) == 2:
        ScoringCounts[53] += 1
    elif Roll.count(5) == 2:
        ScoringCounts[54] += 1
    elif Roll.count(1) == 1 and Roll.count(5) == 1:
        ScoringCounts[55] += 1

    #1,5
    elif Roll.count(1) == 1:
        ScoringCounts[56] += 1
    elif Roll.count(5) == 1:
        ScoringCounts[57] += 1

for ele in np.arange(0,len(ScoringRolls),1):
    print("", ScoringRolls[ele], ":", ScoringCounts[ele])

#-------------------------- Count Farkles ---------------------------
Farkles = len(Rolls)
for Roll in ScoringCounts:
    Farkles -= Roll

print(" Farkles :", Farkles)

input("\n Press enter to close. \n")
