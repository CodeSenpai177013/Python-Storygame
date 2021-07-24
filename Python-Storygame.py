from story import *

print("--------------------------The best game!--------------------------")

player_name = input("Enter your name: ")
story = int(input("What story you want to play: "))

if story == 1:
    story1(player_name)
elif story == 2:
    story2(player_name)
