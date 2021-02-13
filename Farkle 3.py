#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Jan 2021 **********************************
#*******************************************************************************
import numpy as np
input("\n Press enter to continue.")

#---------------------------- Conditions ----------------------------
Num_Sides = 6
print("\n 3 SIX-SIDED DICE")

#-------------------------- Possible Rolls --------------------------
Rolls = []
SideValues = np.arange(1,Num_Sides+1,1)

print("\n List of Rolls:")
for Die_1 in SideValues:
    for Die_2 in SideValues:
        for Die_3 in SideValues:
            Roll = sorted([Die_1,Die_2,Die_3])
            Rolls.append(Roll)
            print("", Roll)

print("\n Number of Possible Rolls :", len(Rolls), "\n")

#------------------------ Count Scoring Rolls -----------------------
ScoringRolls = ["Triple One","Triple Two","Triple Three",
                "Triple Four","Triple Five","Triple Six",
                "One One Five","One Five Five",
                "One One","Five Five","One Five",
                "One","Five"]
ScoringCounts = np.zeros( len(ScoringRolls) )

for Roll in Rolls:
    if Roll == [1,1,1]:
        ScoringCounts[0] += 1
    elif Roll == [2,2,2]:
        ScoringCounts[1] += 1
    elif Roll == [3,3,3]:
        ScoringCounts[2] += 1
    elif Roll == [4,4,4]:
        ScoringCounts[3] += 1
    elif Roll == [5,5,5]:
        ScoringCounts[4] += 1
    elif Roll == [6,6,6]:
        ScoringCounts[5] += 1

    elif Roll == [1,1,5]:
        ScoringCounts[6] += 1
    elif Roll == [1,5,5]:
        ScoringCounts[7] += 1

    elif Roll[:2] == [1,1]:
        ScoringCounts[8] += 1
    elif Roll[:2] == [5,5] or Roll[1:] == [5,5]:
        ScoringCounts[9] += 1
    elif Roll[0] == 1 and ( Roll[1] == 5 or Roll[2] == 5 ):
        ScoringCounts[10] += 1

    elif Roll[0] == 1 or Roll[1] == 1 or Roll[2] == 1:
        ScoringCounts[11] += 1
    elif Roll[0] == 5 or Roll[1] == 5 or Roll[2] == 5:
        ScoringCounts[12] += 1

for ele in np.arange(0,len(ScoringRolls),1):
    print("", ScoringRolls[ele], ":", ScoringCounts[ele])

#-------------------------- Count Farkles ---------------------------
Farkles = len(Rolls)
for Roll in ScoringCounts:
    Farkles -= Roll

print(" Farkles :", Farkles)

input("\n Press enter to close. \n")
