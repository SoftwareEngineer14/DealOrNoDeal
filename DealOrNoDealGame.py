import random
import collections

def FillCases():
    index = 0
    while len(cases) < 26:
        caseNumber = random.randint(1, 26)
        if caseNumber in cases:
            continue
        cases[caseNumber] = caseValues[index]
        index += 1

def SortCases():
    orderedCases = collections.OrderedDict(sorted(cases.items()))
    for k, v in orderedCases.items(): print(k, v)
    for i in range(1, 27):
        print("{0} in cases: {1}".format(i, i in orderedCases))

def CalcBankersOffer():
    total = 0
    for val in orderedCases.values():
        total += val
    return (int)(total/len(orderedCases.values()))
    
def PrintRemainingCaseNumbers():
    print("Remaining case numbers: ")
    for k in orderedCases.keys(): print(k)
#    for k, v in orderedCases.items(): print(k, v)
#    print("Remaining case numbers: ")
#    for caseNum in cases:
#        print("{0}, ".format(caseNum), end = '')

def PrintRemainingCaseValues():
    print("Remaining case values: ")
    for v in cases.values(): print(v)
#    for k, v in orderedCases.items(): print(k, v)
#    print("Remaining case values: ")
#    for value in cases.values():
#        print("{0}, ".format(value), end = '')

def PrintRemainingCases():
    print("Remaining cases: ")
    for k, v in orderedCases.items(): print(k, v)

'''
caseValues = {
    1 : 0.01
    2 : 1
    3 : 5
    4 : 10
    5 : 25
    6 : 50
    7 : 75
    8 : 100
    9 : 200
    10 : 300
    11 : 400
    12 : 500
    13 : 750
    14 : 1000
    15 : 5000
    16 : 10000
    17 : 25000
    18 : 50000
    19 : 75000
    20 : 100000
    21 : 200000
    22 : 300000
    23 : 400000
    24 : 500000
    25 : 750000
    26 : 1000000
}
'''
cases = {}
orderedCases = {}
playersCase = {}
caseValues = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000,
75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
selections = 0
FillCases()
orderedCases = collections.OrderedDict(sorted(cases.items()))
PrintRemainingCaseNumbers()
playersCaseSelection = int(input("Select your case> "))
playersCaseAmount = orderedCases.get(playersCaseSelection)
playersCase[playersCaseSelection] = playersCaseAmount
if playersCaseSelection in orderedCases:
    print("Your selected case is {0}.".format(playersCaseSelection))
else:
    print("Case must be valid. Select another case.")
orderedCases.pop(playersCaseSelection)
cases.pop(playersCaseSelection)

caseSelection = int(input("Select 6 cases to open> "))
while caseSelection not in orderedCases:
    print("Case {0} no longer exists, please select an available case".format(caseSelection))
    print()
    #PrintRemainingCases()
    PrintRemainingCaseNumbers()
    print()
    PrintRemainingCaseValues()
    print()
    caseSelection = int(input("Select 6 cases to open> "))
print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
orderedCases.pop(caseSelection)
cases.pop(caseSelection)
print()
#PrintRemainingCases()
PrintRemainingCaseNumbers()
print()
PrintRemainingCaseValues()
print()
selections += 1

while selections < 6:
    caseSelection = int(input("Next case> "))
    while caseSelection not in orderedCases:
        print("Case {0} no longer exists, please select an available case".format(caseSelection))
        print()
        #PrintRemainingCases()
        PrintRemainingCaseNumbers()
        print()
        PrintRemainingCaseValues()
        print()
        caseSelection = int(input("Next case> "))
    print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
    orderedCases.pop(caseSelection)
    cases.pop(caseSelection)
    print()
    #PrintRemainingCases()
    PrintRemainingCaseNumbers()
    print()
    PrintRemainingCaseValues()
    print()
    selections += 1
selections = 0

#bankersOffer = CalcBankersOffer()
bankersOffer = random.randint(10000, 30000)
print("Bankers offer: {0}".format(bankersOffer))
playersDecision = input("Deal (D) or no deal (N)? ")
if playersDecision.upper() == 'D':
    print("You accepted the bankers offer of {0}".format(bankersOffer))
    print("Your case {0} contained {1}".format(playersCaseSelection, playersCaseAmount))
    if playersCaseAmount > bankersOffer:
        print("Your made a poor deal")
    else:
        print("You made a great deal")
    print()
    exit()
else:
    print("No deal! Good luck")

caseSelection = int(input("Select 5 cases to open> "))
while caseSelection not in orderedCases:
    print("Case {0} no longer exists, please select an available case".format(caseSelection))
    print()
    PrintRemainingCaseNumbers()
    print()
    PrintRemainingCaseValues()
    print()
    caseSelection = int(input("Select 5 cases to open> "))
print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
orderedCases.pop(caseSelection)
cases.pop(caseSelection)
print()
PrintRemainingCaseNumbers()
print()
PrintRemainingCaseValues()
print()
selections += 1

while selections < 5:
    caseSelection = int(input("Next case> "))
    while caseSelection not in orderedCases:
        print("Case {0} no longer exists, please select an available case".format(caseSelection))
        print()
        PrintRemainingCaseNumbers()
        print()
        PrintRemainingCaseValues()
        print()
        caseSelection = int(input("Next case> "))
    print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
    orderedCases.pop(caseSelection)
    cases.pop(caseSelection)
    print()
    PrintRemainingCaseNumbers()
    print()
    PrintRemainingCaseValues()
    print()
    selections += 1
selections = 0

#bankersOffer = CalcBankersOffer()
bankersOffer = random.randint(30000, 60000)
print("Bankers offer: {0}".format(bankersOffer))
playersDecision = input("Deal (D) or no deal (N)? ")
if playersDecision.upper() == 'D':
    print("You accepted the bankers offer of {0}".format(bankersOffer))
    print("Your case {0} contained {1}".format(playersCaseSelection, playersCaseAmount))
    if playersCaseAmount > bankersOffer:
        print("Your made a poor deal")
    else:
        print("You made a great deal")
    print()
    exit()
else:
    print("No deal! Good luck")

caseSelection = int(input("Select 4 cases to open> "))
while caseSelection not in orderedCases:
    print("Case {0} no longer exists, please select an available case".format(caseSelection))
    print()
    PrintRemainingCaseNumbers()
    print()
    PrintRemainingCaseValues()
    print()
    caseSelection = int(input("Select 4 cases to open> "))
print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
orderedCases.pop(caseSelection)
cases.pop(caseSelection)
print()
PrintRemainingCaseNumbers()
print()
PrintRemainingCaseValues()
print()
selections += 1

while selections < 4:
    caseSelection = int(input("Next case> "))
    while caseSelection not in orderedCases:
        print("Case {0} no longer exists, please select an available case".format(caseSelection))
        print()
        PrintRemainingCaseNumbers()
        print()
        PrintRemainingCaseValues()
        print()
        caseSelection = int(input("Next case> "))
    print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
    orderedCases.pop(caseSelection)
    cases.pop(caseSelection)
    print()
    PrintRemainingCaseNumbers()
    print()
    PrintRemainingCaseValues()
    print()
    selections += 1
selections = 0

bankersOffer = CalcBankersOffer()
print("Bankers offer: {0}".format(bankersOffer))
playersDecision = input("Deal (D) or no deal (N)? ")
if playersDecision.upper() == 'D':
    print("You accepted the bankers offer of {0}".format(bankersOffer))
    print("Your case {0} contained {1}".format(playersCaseSelection, playersCaseAmount))
    if playersCaseAmount > bankersOffer:
        print("Your made a poor deal")
    else:
        print("You made a great deal")
    print()
    exit()
else:
    print("No deal! Good luck")
    
caseSelection = int(input("Select 3 cases to open> "))
while caseSelection not in orderedCases:
        print("Case {0} no longer exists, please select an available case".format(caseSelection))
        Pprint()
        PrintRemainingCaseNumbers()
        print()
        PrintRemainingCaseValues()
        print()
        caseSelection = int(input("Next case> "))
print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
orderedCases.pop(caseSelection)
cases.pop(caseSelection)
print()
PrintRemainingCaseNumbers()
print()
PrintRemainingCaseValues()
print()
selections += 1

while selections < 3:
    caseSelection = int(input("Next case> "))
    while caseSelection not in orderedCases:
        print("Case {0} no longer exists, please select an available case".format(caseSelection))
        print()
        PrintRemainingCaseNumbers()
        print()
        PrintRemainingCaseValues()
        print()
        caseSelection = int(input("Next case> "))
    print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
    orderedCases.pop(caseSelection)
    cases.pop(caseSelection)
    print()
    PrintRemainingCaseNumbers()
    print()
    PrintRemainingCaseValues()
    print()
    selections += 1
selections = 0

bankersOffer = CalcBankersOffer()
print("Bankers offer: {0}".format(bankersOffer))
playersDecision = input("Deal (D) or no deal (N)? ")
if playersDecision.upper() == 'D':
    print("You accepted the bankers offer of {0}".format(bankersOffer))
    print("Your case {0} contained {1}".format(playersCaseSelection, playersCaseAmount))
    if playersCaseAmount > bankersOffer:
        print("Your made a poor deal")
    else:
        print("You made a great deal")
    print()
    exit()
else:
    print("No deal! Good luck")

caseSelection = int(input("Select 2 cases to open> "))
while caseSelection not in orderedCases:
        print("Case {0} no longer exists, please select an available case".format(caseSelection))
        print()
        PrintRemainingCaseNumbers()
        print()
        PrintRemainingCaseValues()
        print()
        caseSelection = int(input("Next case> "))
print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
orderedCases.pop(caseSelection)
cases.pop(caseSelection)
print()
PrintRemainingCaseNumbers()
print()
PrintRemainingCaseValues()
print()
selections += 1

while selections < 2:
    caseSelection = int(input("Next case> "))
    while caseSelection not in orderedCases:
        print("Case {0} no longer exists, please select an available case".format(caseSelection))
        print()
        PrintRemainingCaseNumbers()
        print()
        PrintRemainingCaseValues()
        print()
        caseSelection = int(input("Next case> "))
    print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
    orderedCases.pop(caseSelection)
    cases.pop(caseSelection)
    print()
    PrintRemainingCaseNumbers()
    print()
    PrintRemainingCaseValues()
    print()
    selections += 1
selections = 0

bankersOffer = CalcBankersOffer()
print("Bankers offer: {0}".format(bankersOffer))
playersDecision = input("Deal (D) or no deal (N)? ")
if playersDecision.upper() == 'D':
    print("You accepted the bankers offer of {0}".format(bankersOffer))
    print("Your case {0} contained {1}".format(playersCaseSelection, playersCaseAmount))
    if playersCaseAmount > bankersOffer:
        print("Your made a poor deal")
    else:
        print("You made a great deal")
    print()
    exit()
else:
    print("No deal! Good luck")

while len(orderedCases) >= 2:
    if len(orderedCases) == 1:
        playersDecision = input("One case remaining. Would you like to keep your case (K) or \
            switch cases (S)> ")
        if playersDecision.upper() == 'S':
            playersCaseSelection = orderedCases.keys[0]
            playersCaseAmount = orderedCases.values[0]
            playersCase = {orderedCases.keys[0], orderedCases.values[0]}
        print("Your case {0} contained {1}".format(playersCaseSelection, playersCaseAmount))
        print()
        exit()
    caseSelection = int(input("Next case> "))
    while caseSelection not in orderedCases:
        print("Case {0} no longer exists, please select an available case".format(caseSelection))
        print()
        PrintRemainingCaseNumbers()
        print()
        PrintRemainingCaseValues()
        print()
        caseSelection = int(input("Next case> "))
    print("Case {0} contains {1}".format(caseSelection, orderedCases.get(caseSelection)))
    orderedCases.pop(caseSelection)
    cases.pop(caseSelection)
    print()
    PrintRemainingCaseNumbers()
    print()
    PrintRemainingCaseValues()
    print()
    bankersOffer = CalcBankersOffer()
    print("Bankers offer: {0}".format(bankersOffer))
    playersDecision = input("Deal (D) or no deal (N)? ")
    if playersDecision.upper() == 'D':
        print("You accepted the bankers offer of {0}".format(bankersOffer))
        print("Your case {0} contained {1}".format(playersCaseSelection, playersCaseAmount))
        if playersCaseAmount > bankersOffer:
            print("Your made a poor deal")
        else:
            print("You made a great deal")
        print()
        exit()
    else:
        print("No deal! Good luck")
