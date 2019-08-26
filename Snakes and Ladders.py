from tkinter import * # Imports the tkinter pack
import random         # Imports random pack ( used to make diceRoll)

array =[]

def diceRoll(): # Dice roll function
    dice1= random.randint(1,6) # Creates a dice roll between 1 and 6
    dice2= random.randint(1,6)
    diceroll= dice1 + dice2
    if dice1 == dice2: # Checks to see if you've rolled doubles
        print("Move backwards",diceroll,"spaces!") # Prints backward move
        return -diceroll
    else:
        print("Move forwards",diceroll,"spaces!") # Prints forward move
        return diceroll
window=Tk()

button1= Button(window, text="Press the button to roll the dice!",command=diceRoll)
button1.grid(row=0,column=1,columnspan=5)
# This button is connected to the function "diceRoll" when pressed you are
# given your diceroll and how many spaces to move
# button1.grid ----- states where the button will be on the GUI

player1 = 1
player2 = 1
# Creates the player variables

while player1 < 49 and player2 < 49: # The game will play as long as both players are below 49

    player1 = player1 + diceRoll()
    player2 = player2 + diceRoll()
# This states how far the player will move across the grid.

    if player1 < 0:
        player1 = 0
    if player2 < 0:
        player2 = 0
# Error checking, means someone cant go into minus position

    if player1 >= 49:
        print("Player one has conquered the grid!")
        
    if player2 >= 49:
        print("Player two has destroyed the competition!")
# This is the win condition, if a player goes past 49 they win.

    print(player1)
    print(player2)

# This prints the players position everytime.

# Below is importing a bitmap that looks like a dice!
BMP = """
#define cursor_width 16
#define cursor_height 16
static char cursor_bits[] = {
0xff,0xff,
0x01,0x80,
0x1d,0xb8,
0x1d,0xb8,
0x1d,0xb8,
0x01,0x80,
0x01,0x80,
0x1d,0xb8,
0x1d,0xb8,
0x1d,0xb8,
0x01,0x80,
0x1d,0xb8,
0x1d,0xb8,
0x1d,0xb8,
0x01,0x80,
0xff,0xff};
"""

ImageOne = BitmapImage(data=BMP, foreground="purple")

# This states the BMP as a variable


labelimage=Label(window,image=ImageOne)

# This assigns the button to a label, allowing it to be displayed on the GUI

labelimage.grid(row=0,column=0)

# This places the image at row 0, colum 0 on the grid


BMP = """
#define cursor_width 16
#define cursor_height 16
static char cursor_bits[] = {
0xff,0xff,
0x01,0x80,
0x3d,0xbc,
0x3d,0xbc,
0x3d,0xbc,
0x3d,0xbc,
0xc1,0x83,
0xc1,0x83,
0xc1,0x83,
0xc1,0x83,
0x3d,0xbc,
0x3d,0xbc,
0x3d,0xbc,
0x3d,0xbc,
0x01,0x80,
0xff,0xff};;
"""

ImageTwo = BitmapImage(data=BMP, foreground="purple")


labelimage=Label(window,image=ImageTwo)

labelimage.grid(row=0,column=6)

window2=Tk()

col = 1
row = 2
num = 1
for num in range (1,50):
    box_num = Label(window2, text = num, font = ('impact', 40),borderwidth = 10, relief = 'groove', width = 2, bg = 'white')
    if (8 - row) % 2 == 0:
        box_num.grid(row = 8 - row, column = col)
    else:
        box_num.grid(row = 8 -row, column = 8 - col) 
    array.append(box_num)
    col += 1
    num += 1
    if col == 8:
        row += 1
        col = 1


    
