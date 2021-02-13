#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Jan 2021 **********************************
#*******************************************************************************
import numpy as np
input("\n Press enter to continue.")

#---------------------------- Conditions ----------------------------
Num_Sides = 6
print("\n 5 SIX-SIDED DICE")

#-------------------------- Possible Rolls --------------------------
Rolls = []
SideValues = np.arange(1,Num_Sides+1,1)

print("\n List of Rolls:")
for Die_1 in SideValues:
    for Die_2 in SideValues:
        for Die_3 in SideValues:
            for Die_4 in SideValues:
                for Die_5 in SideValues:
                    Roll = sorted([Die_1,Die_2,Die_3,Die_4,Die_5])
                    Rolls.append(Roll)
                    print("", Roll)

print("\n Number of Possible Rolls :", len(Rolls), "\n")

#------------------------ Count Scoring Rolls -----------------------
ScoringRolls = ["Five of a Kind",
                
                "Four of a Kind +One","Four of a Kind +Five",
                
                "Four of a Kind",
                
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
                
                "One One Five Five",
                
                "One One Five","One Five Five",
                
                "One One","Five Five","One Five",
                
                "One","Five"]
ScoringCounts = np.zeros( len(ScoringRolls) )

for Roll in Rolls:
    #Five of a Kind
    if Roll.count(Roll[0]) == len(Roll):
        ScoringCounts[0] += 1

    #Four of a Kind +1,+5
    elif Roll[0] == 1 and Roll[1:].count(Roll[1]) == 4:
        ScoringCounts[1] += 1
    elif ( Roll[:4].count(Roll[0]) == 4 and Roll[4] == 5 ) or Roll == [5,6,6,6,6]:
        ScoringCounts[2] += 1

    #Four of a Kind
    elif Roll[:4].count(Roll[0]) == 4 or Roll[1:].count(Roll[1]) == 4:
        ScoringCounts[3] += 1

    #Triples +11
    elif Roll == [1,1,2,2,2]:
        ScoringCounts[4] += 1
    elif Roll == [1,1,3,3,3]:
        ScoringCounts[5] += 1
    elif Roll == [1,1,4,4,4]:
        ScoringCounts[6] += 1
    elif Roll == [1,1,5,5,5]:
        ScoringCounts[7] += 1
    elif Roll == [1,1,6,6,6]:
        ScoringCounts[8] += 1

    #Triples +55
    elif Roll == [1,1,1,5,5]:
        ScoringCounts[9] += 1
    elif Roll == [2,2,2,5,5]:
        ScoringCounts[10] += 1
    elif Roll == [3,3,3,5,5]:
        ScoringCounts[11] += 1
    elif Roll == [4,4,4,5,5]:
        ScoringCounts[12] += 1
    elif Roll == [5,5,6,6,6]:
        ScoringCounts[13] += 1

    #Triples +15
    elif Roll == [1,2,2,2,5]:
        ScoringCounts[14] += 1
    elif Roll == [1,3,3,3,5]:
        ScoringCounts[15] += 1
    elif Roll == [1,4,4,4,5]:
        ScoringCounts[16] += 1
    elif Roll == [1,5,6,6,6]:
        ScoringCounts[17] += 1

    #Triples +1
    elif Roll[0] == 1 and Roll.count(2) == 3:
        ScoringCounts[18] += 1
    elif Roll[0] == 1 and Roll.count(3) == 3:
        ScoringCounts[19] += 1
    elif Roll[0] == 1 and Roll.count(4) == 3:
        ScoringCounts[20] += 1
    elif Roll[0] == 1 and Roll.count(5) == 3:
        ScoringCounts[21] += 1
    elif Roll[0] == 1 and Roll.count(6) == 3:
        ScoringCounts[22] += 1

    #Triples +5
    elif Roll.count(5) == 1 and Roll.count(1) == 3:
        ScoringCounts[23] += 1
    elif Roll.count(5) == 1 and Roll.count(2) == 3:
        ScoringCounts[24] += 1
    elif Roll.count(5) == 1 and Roll.count(3) == 3:
        ScoringCounts[25] += 1
    elif Roll.count(5) == 1 and Roll.count(4) == 3:
        ScoringCounts[26] += 1
    elif Roll.count(5) == 1 and Roll.count(6) == 3:
        ScoringCounts[27] += 1

    #Triples
    elif Roll.count(1) == 3:
        ScoringCounts[28] += 1
    elif Roll.count(2) == 3:
        ScoringCounts[29] += 1
    elif Roll.count(3) == 3:
        ScoringCounts[30] += 1
    elif Roll.count(4) == 3:
        ScoringCounts[31] += 1
    elif Roll.count(5) == 3:
        ScoringCounts[32] += 1
    elif Roll.count(6) == 3:
        ScoringCounts[33] += 1

    #1155
    elif Roll.count(1) == 2 and Roll.count(5) == 2:
        ScoringCounts[34] += 1

    #115,155
    elif Roll.count(1) == 2 and Roll.count(5) == 1:
        ScoringCounts[35] += 1
    elif Roll.count(1) == 1 and Roll.count(5) == 2:
        ScoringCounts[36] += 1

    #11,55,15
    elif Roll.count(1) == 2:
        ScoringCounts[37] += 1
    elif Roll.count(5) == 2:
        ScoringCounts[38] += 1
    elif Roll.count(1) == 1 and Roll.count(5) == 1:
        ScoringCounts[39] += 1

    #1,5
    elif Roll.count(1) == 1:
        ScoringCounts[40] += 1
    elif Roll.count(5) == 1:
        ScoringCounts[41] += 1

for ele in np.arange(0,len(ScoringRolls),1):
    print("", ScoringRolls[ele], ":", ScoringCounts[ele])

#-------------------------- Count Farkles ---------------------------
Farkles = len(Rolls)
for Roll in ScoringCounts:
    Farkles -= Roll

print(" Farkles :", Farkles)

input("\n Press enter to close. \n")
