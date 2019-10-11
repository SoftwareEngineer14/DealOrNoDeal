from tkinter import *
from tkinter import messagebox
from enum import Enum
import random
import collections

top = Tk()
top.geometry("{0}x{1}+0+0".format(top.winfo_screenwidth(), top.winfo_screenheight()))

class Level(Enum):
    LEVEL1 = 1
    LEVEL2 = 2
    LEVEL3 = 3
    LEVEL4 = 4
    LEVEL5 = 5
    LEVEL6 = 6
    LEVEL7 = 7
    LEVEL8 = 8
    LEVEL9 = 9
    LEVEL10 = 10

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
        
def PrintCases():
    for k, v in orderedCases.items(): print(k, v)

def CalcBankersOffer():
    total = 0
    for val in orderedCases.values():
        total += val
    return (int)(total/len(orderedCases.values()))
    
def CalcFinalBankersOffer():
    total = 0
    for val in orderedCases.values():
        total += val
    return total/2
    
def CheckForEndOfRound():
    global remainingTurns
    global level
    global finalRoundEntered
    global playersCaseSelection
    global playersCaseAmount
    remainingTurns -= 1
    messagebox.showinfo("Remaining Turns", f"Remaining turns: {remainingTurns}")
    if remainingTurns == 0:
        if len(orderedCases) == 1:
            bankersOffer = CalcFinalBankersOffer()
        elif len(orderedCases) == 0:
            messagebox.showinfo("Game outcome", f"Players case {playersCaseSelection} contained {playersCaseAmount}")
            exit()
        else:
            bankersOffer = CalcBankersOffer()
        choice = messagebox.askyesno("Bankers Offer", f"Bankers offer: {bankersOffer}\n\nDeal or No Deal?")
        messagebox.showinfo("Players choice", f"Players choice {choice}")
        #DisplayOfferUsingMessageBoxAndHandlePlayerSelection()
        # Handle user selection and continue playing game or end game when player has accepted offer
        if Level.LEVEL1 == level:
            remainingTurns = 5
            level = Level.LEVEL2
            messagebox.showinfo("End of round 1", f"Cases to open next round: 5")
        elif Level.LEVEL2 == level:
            remainingTurns = 4
            level = Level.LEVEL3
            messagebox.showinfo("End of round 2", f"Cases to open next round: 4")
        elif Level.LEVEL3 == level:
            remainingTurns = 3
            level = Level.LEVEL4
            messagebox.showinfo("End of round 3", f"Cases to open next round: 3")
        elif Level.LEVEL4 == level:
            remainingTurns = 2
            level = Level.LEVEL5
            messagebox.showinfo("End of round 4", f"Cases to open next round: 2")
        elif Level.LEVEL5 == level:
            remainingTurns = 1
            level = Level.LEVEL6
            messagebox.showinfo("End of round 5", f"Cases to open next round: 1")
        elif Level.LEVEL6 == level:
            remainingTurns = 1
            if not finalRoundEntered:
                messagebox.showinfo("End of round 6", f"Cases to open next round: 1")
                finalRoundEntered = True
            else:
                messagebox.showinfo("End of round", f"Cases to open next round: 1")
            #if len(orderedCases) == 1:
            #    OfferPlayerToSwitch()
            #if remainingCases == 1:
            #    OfferPlayerToSwitch()

def c1CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 1
        playersCaseAmount = orderedCases.get(1)
        playersCase[1] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 1.\n\nRound 1: Select 6 cases")
        c1.config(bg = "Red", state = DISABLED)
        orderedCases.pop(1)
        cases.pop(1)
    else:
        caseValue = orderedCases.get(1)
        messagebox.showinfo("Case 1 selected", f"Case 1 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c1.config(state = DISABLED)
        orderedCases.pop(1)
        cases.pop(1)
        CheckForEndOfRound()

def c2CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 2
        playersCaseAmount = orderedCases.get(2)
        playersCase[2] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 1.\n\nRound 1: Select 6 cases")
        c2.config(bg = "Red", state = DISABLED)
        orderedCases.pop(2)
        cases.pop(2)
    else:
        caseValue = orderedCases.get(2)
        messagebox.showinfo("Case 2 selected", f"Case 2 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c2.config(state = DISABLED)
        orderedCases.pop(2)
        cases.pop(2)
        CheckForEndOfRound()

def c3CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 3
        playersCaseAmount = orderedCases.get(3)
        playersCase[3] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 3.\n\nRound 1: Select 6 cases")
        c3.config(bg = "Red", state = DISABLED)
        orderedCases.pop(3)
        cases.pop(3)
    else:
        caseValue = orderedCases.get(3)
        messagebox.showinfo("Case 3 selected", f"Case 3 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c3.config(state = DISABLED)
        orderedCases.pop(3)
        cases.pop(3)
        CheckForEndOfRound()

def c4CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 4
        playersCaseAmount = orderedCases.get(4)
        playersCase[4] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 4.\n\nRound 1: Select 6 cases")
        c4.config(bg = "Red", state = DISABLED)
        orderedCases.pop(4)
        cases.pop(4)
    else:
        caseValue = orderedCases.get(4)
        messagebox.showinfo("Case 4 selected", f"Case 4 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c4.config(state = DISABLED)
        orderedCases.pop(4)
        cases.pop(4)
        CheckForEndOfRound()

def c5CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 5
        playersCaseAmount = orderedCases.get(5)
        playersCase[5] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 5.\n\nRound 1: Select 6 cases")
        c5.config(bg = "Red", state = DISABLED)
        orderedCases.pop(5)
        cases.pop(5)
    else:
        caseValue = orderedCases.get(5)
        messagebox.showinfo("Case 5 selected", f"Case 5 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c5.config(state = DISABLED)
        orderedCases.pop(5)
        cases.pop(5)
        CheckForEndOfRound()

def c6CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 6
        playersCaseAmount = orderedCases.get(6)
        playersCase[6] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 6.\n\nRound 1: Select 6 cases")
        c6.config(bg = "Red", state = DISABLED)
        orderedCases.pop(6)
        cases.pop(6)
    else:
        caseValue = orderedCases.get(6)
        messagebox.showinfo("Case 6 selected", f"Case 6 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c6.config(state = DISABLED)
        orderedCases.pop(6)
        cases.pop(6)
        CheckForEndOfRound()

def c7CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 7
        playersCaseAmount = orderedCases.get(7)
        playersCase[7] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 7.\n\nRound 1: Select 6 cases")
        c7.config(bg = "Red", state = DISABLED)
        orderedCases.pop(7)
        cases.pop(7)
    else:
        caseValue = orderedCases.get(7)
        messagebox.showinfo("Case 7 selected", f"Case 7 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c7.config(state = DISABLED)
        orderedCases.pop(7)
        cases.pop(7)
        CheckForEndOfRound()

def c8CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 8
        playersCaseAmount = orderedCases.get(8)
        playersCase[8] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 8.\n\nRound 1: Select 6 cases")
        c8.config(bg = "Red", state = DISABLED)
        orderedCases.pop(8)
        cases.pop(8)
    else:
        caseValue = orderedCases.get(8)
        messagebox.showinfo("Case 8 selected", f"Case 8 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c8.config(state = DISABLED)
        orderedCases.pop(8)
        cases.pop(8)
        CheckForEndOfRound()

def c9CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 9
        playersCaseAmount = orderedCases.get(9)
        playersCase[9] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 9.\n\nRound 1: Select 6 cases")
        c9.config(bg = "Red", state = DISABLED)
        orderedCases.pop(9)
        cases.pop(9)
    else:
        caseValue = orderedCases.get(9)
        messagebox.showinfo("Case 9 selected", f"Case 9 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c9.config(state = DISABLED)
        orderedCases.pop(9)
        cases.pop(9)
        CheckForEndOfRound()

def c10CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 10
        playersCaseAmount = orderedCases.get(10)
        playersCase[10] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 10.\n\nRound 1: Select 6 cases")
        c10.config(bg = "Red", state = DISABLED)
        orderedCases.pop(10)
        cases.pop(10)
    else:
        caseValue = orderedCases.get(10)
        messagebox.showinfo("Case 10 selected", f"Case 10 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c10.config(state = DISABLED)
        orderedCases.pop(10)
        cases.pop(10)
        CheckForEndOfRound()

def c11CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 11
        playersCaseAmount = orderedCases.get(11)
        playersCase[11] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 11.\n\nRound 1: Select 6 cases")
        c11.config(bg = "Red", state = DISABLED)
        orderedCases.pop(11)
        cases.pop(11)
    else:
        caseValue = orderedCases.get(11)
        messagebox.showinfo("Case 11 selected", f"Case 11 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c11.config(state = DISABLED)
        orderedCases.pop(11)
        cases.pop(11)
        CheckForEndOfRound()

def c12CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 12
        playersCaseAmount = orderedCases.get(12)
        playersCase[12] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 12.\n\nRound 1: Select 6 cases")
        c12.config(bg = "Red", state = DISABLED)
        orderedCases.pop(12)
        cases.pop(12)
    else:
        caseValue = orderedCases.get(12)
        messagebox.showinfo("Case 12 selected", f"Case 12 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c12.config(state = DISABLED)
        orderedCases.pop(12)
        cases.pop(12)
        CheckForEndOfRound()

def c13CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 13
        playersCaseAmount = orderedCases.get(13)
        playersCase[13] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 13.\n\nRound 1: Select 6 cases")
        c13.config(bg = "Red", state = DISABLED)
        orderedCases.pop(13)
        cases.pop(13)
    else:
        caseValue = orderedCases.get(13)
        messagebox.showinfo("Case 13 selected", f"Case 13 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c13.config(state = DISABLED)
        orderedCases.pop(13)
        cases.pop(13)
        CheckForEndOfRound()

def c14CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 14
        playersCaseAmount = orderedCases.get(14)
        playersCase[14] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 14.\n\nRound 1: Select 6 cases")
        c14.config(bg = "Red", state = DISABLED)
        orderedCases.pop(14)
        cases.pop(14)
    else:
        caseValue = orderedCases.get(14)
        messagebox.showinfo("Case 14 selected", f"Case 14 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c14.config(state = DISABLED)
        orderedCases.pop(14)
        cases.pop(14)
        CheckForEndOfRound()

def c15CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 15
        playersCaseAmount = orderedCases.get(15)
        playersCase[15] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 15.\n\nRound 1: Select 6 cases")
        c15.config(bg = "Red", state = DISABLED)
        orderedCases.pop(15)
        cases.pop(15)
    else:
        caseValue = orderedCases.get(15)
        messagebox.showinfo("Case 15 selected", f"Case 15 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c15.config(state = DISABLED)
        orderedCases.pop(15)
        cases.pop(15)
        CheckForEndOfRound()

def c16CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 16
        playersCaseAmount = orderedCases.get(16)
        playersCase[16] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 16.\n\nRound 1: Select 6 cases")
        c16.config(bg = "Red", state = DISABLED)
        orderedCases.pop(16)
        cases.pop(16)
    else:
        caseValue = orderedCases.get(16)
        messagebox.showinfo("Case 16 selected", f"Case 16 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c16.config(state = DISABLED)
        orderedCases.pop(16)
        cases.pop(16)
        CheckForEndOfRound()

def c17CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 17
        playersCaseAmount = orderedCases.get(17)
        playersCase[17] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 17.\n\nRound 1: Select 6 cases")
        c17.config(bg = "Red", state = DISABLED)
        orderedCases.pop(17)
        cases.pop(17)
    else:
        caseValue = orderedCases.get(17)
        messagebox.showinfo("Case 17 selected", f"Case 17 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c17.config(state = DISABLED)
        orderedCases.pop(17)
        cases.pop(17)
        CheckForEndOfRound()

def c18CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 18
        playersCaseAmount = orderedCases.get(18)
        playersCase[18] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 18.\n\nRound 1: Select 6 cases")
        c18.config(bg = "Red", state = DISABLED)
        orderedCases.pop(18)
        cases.pop(18)
    else:
        caseValue = orderedCases.get(18)
        messagebox.showinfo("Case 18 selected", f"Case 18 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c18.config(state = DISABLED)
        orderedCases.pop(18)
        cases.pop(18)
        CheckForEndOfRound()

def c19CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 19
        playersCaseAmount = orderedCases.get(19)
        playersCase[19] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 19.\n\nRound 1: Select 6 cases")
        c19.config(bg = "Red", state = DISABLED)
        orderedCases.pop(19)
        cases.pop(19)
    else:
        caseValue = orderedCases.get(19)
        messagebox.showinfo("Case 19 selected", f"Case 19 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c19.config(state = DISABLED)
        orderedCases.pop(19)
        cases.pop(19)
        CheckForEndOfRound()

def c20CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 20
        playersCaseAmount = orderedCases.get(20)
        playersCase[20] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 20.\n\nRound 1: Select 6 cases")
        c20.config(bg = "Red", state = DISABLED)
        orderedCases.pop(20)
        cases.pop(20)
    else:
        caseValue = orderedCases.get(20)
        messagebox.showinfo("Case 20 selected", f"Case 20 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c20.config(state = DISABLED)
        orderedCases.pop(20)
        cases.pop(20)
        CheckForEndOfRound()

def c21CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 21
        playersCaseAmount = orderedCases.get(21)
        playersCase[21] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 21.\n\nRound 1: Select 6 cases")
        c21.config(bg = "Red", state = DISABLED)
        orderedCases.pop(21)
        cases.pop(21)
    else:
        caseValue = orderedCases.get(21)
        messagebox.showinfo("Case 21 selected", f"Case 21 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c21.config(state = DISABLED)
        orderedCases.pop(21)
        cases.pop(21)
        CheckForEndOfRound()

def c22CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 22
        playersCaseAmount = orderedCases.get(22)
        playersCase[22] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 22.\n\nRound 1: Select 6 cases")
        c22.config(bg = "Red", state = DISABLED)
        orderedCases.pop(22)
        cases.pop(22)
    else:
        caseValue = orderedCases.get(22)
        messagebox.showinfo("Case 22 selected", f"Case 22 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c22.config(state = DISABLED)
        orderedCases.pop(22)
        cases.pop(22)
        CheckForEndOfRound()

def c23CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 23
        playersCaseAmount = orderedCases.get(23)
        playersCase[23] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 23.\n\nRound 1: Select 6 cases")
        c23.config(bg = "Red", state = DISABLED)
        orderedCases.pop(23)
        cases.pop(23)
    else:
        caseValue = orderedCases.get(23)
        messagebox.showinfo("Case 23 selected", f"Case 23 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c23.config(state = DISABLED)
        orderedCases.pop(23)
        cases.pop(23)
        CheckForEndOfRound()

def c24CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 24
        playersCaseAmount = orderedCases.get(24)
        playersCase[24] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 24.\n\nRound 1: Select 6 cases")
        c24.config(bg = "Red", state = DISABLED)
        orderedCases.pop(24)
        cases.pop(24)
    else:
        caseValue = orderedCases.get(24)
        messagebox.showinfo("Case 24 selected", f"Case 24 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c24.config(state = DISABLED)
        orderedCases.pop(24)
        cases.pop(24)
        CheckForEndOfRound()

def c25CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 25
        playersCaseAmount = orderedCases.get(25)
        playersCase[25] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 25.\n\nRound 1: Select 6 cases")
        c25.config(bg = "Red", state = DISABLED)
        orderedCases.pop(25)
        cases.pop(25)
    else:
        caseValue = orderedCases.get(25)
        messagebox.showinfo("Case 25 selected", f"Case 25 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c25.config(state = DISABLED)
        orderedCases.pop(25)
        cases.pop(25)
        CheckForEndOfRound()

def c26CallBack():
    global playersCaseSelected
    global playersCaseSelection
    global playersCaseAmount
    if not playersCaseSelected:
        playersCaseSelection = 26
        playersCaseAmount = orderedCases.get(26)
        playersCase[26] = playersCaseAmount
        playersCaseSelected = True
        messagebox.showinfo("Players Case Selected", "You selected case 26.\n\nRound 1: Select 6 cases")
        c26.config(bg = "Red", state = DISABLED)
        orderedCases.pop(26)
        cases.pop(26)
    else:
        caseValue = orderedCases.get(26)
        messagebox.showinfo("Case 26 selected", f"Case 26 contains {caseValue}")
        if caseValue == 0.01:
            v1.config(state = DISABLED, bg = "Green")
        elif caseValue == 1:
            v2.config(state = DISABLED, bg = "Green")
        elif caseValue == 5:
            v3.config(state = DISABLED, bg = "Green")
        elif caseValue == 10:
            v4.config(state = DISABLED, bg = "Green")
        elif caseValue == 25:
            v5.config(state = DISABLED, bg = "Green")
        elif caseValue == 50:
            v6.config(state = DISABLED, bg = "Green")
        elif caseValue == 75:
            v7.config(state = DISABLED, bg = "Green")
        elif caseValue == 100:
            v8.config(state = DISABLED, bg = "Green")
        elif caseValue == 200:
            v9.config(state = DISABLED, bg = "Green")
        elif caseValue == 300:
            v10.config(state = DISABLED, bg = "Green")
        elif caseValue == 400:
            v11.config(state = DISABLED, bg = "Green")
        elif caseValue == 500:
            v12.config(state = DISABLED, bg = "Green")
        elif caseValue == 750:
            v13.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000:
            v14.config(state = DISABLED, bg = "Green")
        elif caseValue == 5000:
            v15.config(state = DISABLED, bg = "Green")
        elif caseValue == 10000:
            v16.config(state = DISABLED, bg = "Green")
        elif caseValue == 25000:
            v17.config(state = DISABLED, bg = "Green")
        elif caseValue == 50000:
            v18.config(state = DISABLED, bg = "Green")
        elif caseValue == 75000:
            v19.config(state = DISABLED, bg = "Green")
        elif caseValue == 100000:
            v20.config(state = DISABLED, bg = "Green")
        elif caseValue == 200000:
            v21.config(state = DISABLED, bg = "Green")
        elif caseValue == 300000:
            v22.config(state = DISABLED, bg = "Green")
        elif caseValue == 400000:
            v23.config(state = DISABLED, bg = "Green")
        elif caseValue == 500000:
            v24.config(state = DISABLED, bg = "Green")
        elif caseValue == 750000:
            v25.config(state = DISABLED, bg = "Green")
        elif caseValue == 1000000:
            v26.config(state = DISABLED, bg = "Green")
        c26.config(state = DISABLED)
        orderedCases.pop(26)
        cases.pop(26)
        CheckForEndOfRound()

cases = {}
orderedCases = {}
playersCase = {}
caseValues = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000,
75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
FillCases()
remainingTurns = 6
playersCaseSelection = 0
playersCaseAmount = 0
orderedCases = collections.OrderedDict(sorted(cases.items()))
level = Level.LEVEL1
playersCaseSelected = False
finalRoundEntered = False
PrintCases()

v1 = Button(top, text = "$0.01", bg = "Yellow", state = DISABLED)
v1.place(x = 50,y = 50)
v2 = Button(top, text = "$1", bg = "Yellow", state = DISABLED)
v2.place(x = 50,y = 100)
v3 = Button(top, text = "$5", bg = "Yellow", state = DISABLED)
v3.place(x = 50,y = 150)
v4 = Button(top, text = "$10", bg = "Yellow", state = DISABLED)
v4.place(x = 50,y = 200)
v5 = Button(top, text = "$25", bg = "Yellow", state = DISABLED)
v5.place(x = 50,y = 250)
v6 = Button(top, text = "$50", bg = "Yellow", state = DISABLED)
v6.place(x = 50,y = 300)
v7 = Button(top, text = "$75", bg = "Yellow", state = DISABLED)
v7.place(x = 50,y = 350)
v8 = Button(top, text = "$100", bg = "Yellow", state = DISABLED)
v8.place(x = 50,y = 400)
v9 = Button(top, text = "$200", bg = "Yellow", state = DISABLED)
v9.place(x = 50,y = 450)
v10 = Button(top, text = "$300", bg = "Yellow", state = DISABLED)
v10.place(x = 50,y = 500)
v11 = Button(top, text = "$400", bg = "Yellow", state = DISABLED)
v11.place(x = 50,y = 550)
v12 = Button(top, text = "$500", bg = "Yellow", state = DISABLED)
v12.place(x = 50,y = 600)
v13 = Button(top, text = "$750", bg = "Yellow", state = DISABLED)
v13.place(x = 50,y = 650)
v14 = Button(top, text = "$1000", bg = "Yellow", state = DISABLED)
v14.place(x = 600,y = 50)
v15 = Button(top, text = "$5000", bg = "Yellow", state = DISABLED)
v15.place(x = 600,y = 100)
v16 = Button(top, text = "$10000", bg = "Yellow", state = DISABLED)
v16.place(x = 600,y = 150)
v17 = Button(top, text = "$25000", bg = "Yellow", state = DISABLED)
v17.place(x = 600,y = 200)
v18 = Button(top, text = "$50000", bg = "Yellow", state = DISABLED)
v18.place(x = 600,y = 250)
v19 = Button(top, text = "$75000", bg = "Yellow", state = DISABLED)
v19.place(x = 600,y = 300)
v20 = Button(top, text = "$100000", bg = "Yellow", state = DISABLED)
v20.place(x = 600,y = 350)
v21 = Button(top, text = "$200000", bg = "Yellow", state = DISABLED)
v21.place(x = 600,y = 400)
v22 = Button(top, text = "$300000", bg = "Yellow", state = DISABLED)
v22.place(x = 600,y = 450)
v23 = Button(top, text = "$400000", bg = "Yellow", state = DISABLED)
v23.place(x = 600,y = 500)
v24 = Button(top, text = "$500000", bg = "Yellow", state = DISABLED)
v24.place(x = 600,y = 550)
v25 = Button(top, text = "$750000", bg = "Yellow", state = DISABLED)
v25.place(x = 600,y = 600)
v26 = Button(top, text = "$1000000", bg = "Yellow", state = DISABLED)
v26.place(x = 600,y = 650)

c1 = Button(top, text = "1", height = 2, width = 2, command = c1CallBack)
c1.place(x = 150,y = 50)
c2 = Button(top, text = "2", height = 2, width = 2, command = c2CallBack)
c2.place(x = 210,y = 50)
c3 = Button(top, text = "3", height = 2, width = 2, command = c3CallBack)
c3.place(x = 270,y = 50)
c4 = Button(top, text = "4", height = 2, width = 2, command = c4CallBack)
c4.place(x = 330,y = 50)
c5 = Button(top, text = "5", height = 2, width = 2, command = c5CallBack)
c5.place(x = 390,y = 50)
c6 = Button(top, text = "6", height = 2, width = 2, command = c6CallBack)
c6.place(x = 450,y = 50)
c7 = Button(top, text = "7", height = 2, width = 2, command = c7CallBack)
c7.place(x = 510,y = 50)
c8 = Button(top, text = "8", height = 2, width = 2, command = c8CallBack)
c8.place(x = 170,y = 200)
c9 = Button(top, text = "9", height = 2, width = 2, command = c9CallBack)
c9.place(x = 230,y = 200)
c10 = Button(top, text = "10", height = 2, width = 2, command = c10CallBack)
c10.place(x = 290,y = 200)
c11 = Button(top, text = "11", height = 2, width = 2, command = c11CallBack)
c11.place(x = 350,y = 200)
c12 = Button(top, text = "12", height = 2, width = 2, command = c12CallBack)
c12.place(x = 410,y = 200)
c13 = Button(top, text = "13", height = 2, width = 2, command = c13CallBack)
c13.place(x = 470,y = 200)
c14 = Button(top, text = "14", height = 2, width = 2, command = c14CallBack)
c14.place(x = 170,y = 350)
c15 = Button(top, text = "15", height = 2, width = 2, command = c15CallBack)
c15.place(x = 230,y = 350)
c16 = Button(top, text = "16", height = 2, width = 2, command = c16CallBack)
c16.place(x = 290,y = 350)
c17 = Button(top, text = "17", height = 2, width = 2, command = c17CallBack)
c17.place(x = 350,y = 350)
c18 = Button(top, text = "18", height = 2, width = 2, command = c18CallBack)
c18.place(x = 410,y = 350)
c19 = Button(top, text = "19", height = 2, width = 2, command = c19CallBack)
c19.place(x = 470,y = 350)
c20 = Button(top, text = "20", height = 2, width = 2, command = c20CallBack)
c20.place(x = 150,y = 500)
c21 = Button(top, text = "21", height = 2, width = 2, command = c21CallBack)
c21.place(x = 210,y = 500)
c22 = Button(top, text = "22", height = 2, width = 2, command = c22CallBack)
c22.place(x = 270,y = 500)
c23 = Button(top, text = "23", height = 2, width = 2, command = c23CallBack)
c23.place(x = 330,y = 500)
c24 = Button(top, text = "24", height = 2, width = 2, command = c24CallBack)
c24.place(x = 390,y = 500)
c25 = Button(top, text = "25", height = 2, width = 2, command = c25CallBack)
c25.place(x = 450,y = 500)
c26 = Button(top, text = "26", height = 2, width = 2, command = c26CallBack)
c26.place(x = 510,y = 500)

messagebox.showinfo("Select Your Case", "Select Your Case To Start")

top.mainloop()
