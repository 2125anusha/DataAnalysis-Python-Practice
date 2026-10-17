print(r'''
                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input("Do you want to go 'Left' or 'Right'?").lower()
if direction=="left":
    to_swim=input("You\'re at a lake, Do you want to 'swim' or 'wait' for a ride ?").lower()
    if to_swim=="wait":
        print("Good thing you waited, or you would have been eaten!")
        door=input("I give you 3 doors to choose: Red, Blue,Yellow").lower()
        if door=="red":
            print("Fiery waves await you, You Lose!")
        elif door=="blue":
            print("Icy Spikes from all sides, You Lose!")
        elif door=="yellow":
            print("Good Choice, You Won!")
        else:
            print("Please pick one among the 3 colors only, Game Over!")
    else:
        print("Patience is everything, must have waited, you lose!")
else:
    print("Took a wrong turn, You Loose!")

