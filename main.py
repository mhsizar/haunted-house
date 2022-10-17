print('''

                     ___
                                   T T
                                   ===
                                   |.|
                                  .'.`.
                                .'.' `.`.
                  %%          .'.' ___ `.`.
                 %%%%       .'.'  |_|_|  `.`.
                %%%%%%    .'.'    |_|_|    `.`.
                %%%%%__.--`'| []  |_|_|  [] |`'---.
__              %%%%|------||               |||||||
 /\     =========%%%|    _&||      ___      ||===='
/  \   ///////////H/| j |  ||     |_|_|     ||    |
||||  ////////////H%|   |- ||     |_|_|     ||____|
|||| /////////////H/|   |  ||     |_|_|     ||  TT|       .   &
|||| @@@@@@@@@@@@@H@|======||               ||====|  "==='   (f
|\//|\/|/\//\||//|\|||/\//|//\||\//||//|\||\||\/|/\//\||////|//\/||

''')
print("The Mystery of the Haunted House\n")
#Story by Paul Channel (https://www.teachervision.com/creative-writing/choose-your-own-adventure-stories)

print(
    'On a rainy day during summer vacation, you were going to your uncle\'s house. You got off the bus, and started walking across the Main Street. When you reach in front of an old house with no other house to be seen nearby, it starts raining heavily and you ran to the house to take shelter.\n'
)

door = input(
    'Below the door, you found a broken numberplate with the number 880 written on it. You just remembered that this is the oldest house in the town and you have heared a lot of haunted story about this house, though you never beleived them. Would you rather get into the house or wait outside and get drenched by the heavy rain?\n \n[Reply with "Enter" or "Wait"] '
).lower()

if door == "enter":
    choice2 = input(
        '\nYou said to yourself, "I will go inside, as I don\'t want to soak at this rain. And I don\'t believe those haunted stories!" You opened the door and stepped inside. Suddenly the door shut down, and you ran back to the door but failed to open it. When you turned around after trying for a minute, a sharp arrow streaks across in front of you! But luckily it misses you. You found a dark staircase in front of you, and a swinging door on your right, through which a light was coming in.\n Do you want to go straight up to the staircase or ran through the door on your right?\n \n[Reply with "Stairs" or "Door"] '
    ).lower()
    if choice2 == "door":
        choice3 = input(
            '\nYou go through the swinging door and reached a big hallroom. You walk through the room and came before a passageway that goes under the house. Suddenly you heard someone walking to you through the swinging door. Do you you want to hide into the closet beside you or run into the passageway?\n \n[Reply with "Hide" or "Run"] '
        ).lower()
        if choice3 == "run":
            print(
                "\nYou go into the pasaageway under the house. After running a while, you found a way that leads you to an exit door. You open the door and run out of the haunted house!\n \nCongratulations!\n \nYou are lucky enough to get out of the house. Don't ever go in there again!"
            )
        elif choice3 == "hide":
            print(
                "\nYou go into the closet. But alas! That was a trapdoor, and you fall down to a hole through it and break your leg. The walls are too smooth to climb. You started shouting, but the only reply you could hear is your echo! There is no other way up. You have been trapped there for eternity!\n \nTHE END"
            )
        else:
            print(
                "Too late! You made the wrong choice to stay still inside the room. In the twinkling of an eye, a paranormal creature enters the room, and kill you.\n \nTHE END"
            )
    elif choice2 == "stairs":
        print(
            "\nYou go up the stairs. It's so dark that you can't even see your feet! You lean against the railing to look below and it breaks. You keep faling an falling deep down a hole and that's the end of you. RIP\n  \nTHE END"
        )
    else:
        print(
            "\nWrong Command! Never be too late to make decisions when your life is at stake! Another arrow hit you from behind, and blow your head up. That's the end of you! RIP\n  \nTHE END"
        )

elif door == "wait":
    print(
        "\nYou have been waiting for an hour outside, but the thunderstorm is never stopping.\n"
    )
    rethink = input(
        '\nWould you change your mind and enter the house to warm yourself?\n \n[Reply with "Yes" or "No"] '
    ).lower()
    if rethink == "yes":
        choice2 = input(
            '\nYou said to yourself, "I will go inside, as I don\'t want to soak at this rain. And I don\'t believe those haunted stories!" You opened the door and stepped inside. Suddenly the door shut down, and you ran back to the door but failed to open it. When you turned around after trying for a minute, a sharp arrow streaks across in front of you! But luckily it misses you. You found a dark staircase in front of you, and a swinging door on your right, through which a light was coming in.\n Do you want to go straight up to the staircase or ran through the door on your right?\n \n[Reply with "Stairs" or "Door"] '
        ).lower()
        if choice2 == "door":
            choice3 = input(
                '\nYou go through the swinging door and reached a big hallroom. You walk through the room and came before a passageway that goes under the house. Suddenly you heard someone walking to you through the swinging door. Do you you want to hide into the closet beside you or run into the passageway?\n \n[Reply with "Hide" or "Run"] '
            ).lower()
            if choice3 == "run":
                print(
                    "\nYou go into the pasaageway under the house. After running a while, you found a way that leads you to an exit door. You open the door and run out of the haunted house!\n \nCongratulations!\n \nYou are lucky enough to get out of the house. Don't ever go in there again!"
                )
            elif choice3 == "hide":
                print(
                    "\nYou go into the closet. But alas! That was a trapdoor, and you fall down to a hole through it and break your leg. The walls are too smooth to climb. You started shouting, but the only reply you could hear is your echo! There is no other way up. You have been trapped there for eternity!\n \nTHE END"
                )
            else:
                print(
                    "Too late! You made the wrong choice to stay still inside the room. In the twinkling of an eye, a paranormal creature enters the room, and kill you.\n \nTHE END"
                )
        elif choice2 == "stairs":
            print(
                "\nYou go up the stairs. It's so dark that you can't even see your feet! You lean against the railing to look below and it breaks. You keep faling an falling deep down a hole and that's the end of you. RIP\n  \nTHE END"
            )
        else:
            print(
                "\nWrong Command! Never be too late to make decisions when your life is at stake! Another arrow hit you from behind, and blow your head up. That's the end of you! RIP\n  \nTHE END"
            )
    else:
        print(
            "\nYou waited there another hour and finally the rain stops! You come out from the door front and run to your uncle's house. Finally!"
        )
else:
    print('\nWrong command! Please restart the game! ')
