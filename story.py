def story1(player_name):
    print(player_name + ", you are playing story 1.")
    print("--------------------------------------------------------------------------------------------------")
    print("You are on your first day in middle school and all the school clubs are recruiting new members.\n"
          "You are very good at kendo. At the moment you are searching for the kendo club, to join.\n"
          "Out of noway a bunch of flyers flew into your face.\n"
          "You are grabbing them out off the air, while you hear someone shouting: \"I´m so sorry!\".\n"
          "You look around and see a small, very cute  girl gathering the flyers.\n"
          "You look at the flyers and see that they are from the shogi club.\n"
          "You are not that good at shogi. You just know the rules.\n"
          "You´r heart skips some beats when you see the cute girl.\n"
          "She says:\"Hi my name is Urushi Yatome. Are you interested in joining the shogi club?\"\n"
          "\"It´s not an official club yet because i´m the only member, but i can guarantee it will be fun.\"")
    print("--------------------------------------------------------------------------------------------------")
    player_input = input("Are you joining the shogi club with the cute Girl? (Y/N) ")
    print("--------------------------------------------------------------------------------------------------")

    if player_input == "Y":
        print("You say:""\"Yes i would like to join. But my shogi skills are not that good.\"\n"
              "She smiles at you and say:\"That's no problem, i´ll teach you.\"\n"
              "She asks:\"Whats your name?\"\n"
              "You respond with:\"My name is " + player_name + "\"! I hope can become good friends.\n"
                                                               "She says:\"I hope that too, " + player_name + ".\"\n"
                                                                                                              "You say bye to Urushi and walk to your class.")
        print("--------------------------------------------------------------------------------------------------")
        print("You have taken seat in class and you are waiting for the class to start,\n"
              "when you hear someone calling you from behind.\n"
              "The voice says:\"Did you join the kendo club? I haven't seen you there.\"\n"
              "You turn around and see your childhood friend Takeru. Both of you are very good kendo player.\n"
              "You say:\"No I joined an other club, how about you?\""
              "Takeru says:\"I didn't joined either, but I'm in the library committee, together with Sakura.\""
              "You smiles and know that Takeru really fallen for Sakura\n"
              "The classes starts but nothing really interesting happens.")
        print("--------------------------------------------------------------------------------------------------")
        print("After classes are over you head to the club rooms and search for the shogi clubroom.\n"
              "You cant find the room and thinking of leaving school for today, because you cant find the room.")
        player_input = input("Are you leaving school for today or do you continue searching? (leave/stay) ")
        print("--------------------------------------------------------------------------------------------------")

        if player_input == "leave":
            print("You leave school early for today because you didn't found the clubroom.\n"
                  "Story end")
        elif player_input == "stay":
            print("You decide to stay at school for a bid longer and continue your search.\n"
                  "Suddenly you remember that the shogi club isn't an official club.\n"
                  "That in mind you continue your search and after a bit you find a door with a note.\n"
                  "On the note stands:'Shogi club'\n"
                  "You are happy that you finally found the clubroom of the unofficial shogi club.\n"
                  "You knock on the door and enter.\n"
                  "\"Hello, is that the shogi clubroom?\"\n"
                  "You look around the room is very small and there is a lot of old things in shelf's.\n"
                  "\"Oh, I'm so sorry! I haven't told you where the clubroom is.I'm so sorry!\"\n"
                  "You look to where the voice was coming from and you see Urushi, your senpai, who invited you to "
                  "the shoghi club.\n"
                  "\"Ahh, Its ok i found the room, so it's ok.\n"
                  "She looks relieved."
                  "So that's really the clubroom?\", you ask."
                  "\"Yes it is. I know it's really small and full of old stuff.\n"
                  "But that's because it's the storage room.\n"
                  "Not so important how about a shogi match?\n")
            print("--------------------------------------------------------------------------------------------------")
            player_input = input("a) Yes gladly!\n"
                                 "b) Yes, by the way did someone called you cute before?\n"
                                 "   Because you really are.\n"
                                 "c) No, I think I'm going home the shogi club is nothing for me.\n"
                                 "   I can't even play shogi that good. Bye\n"
                                 "What do you say? (a/b/c) ")
            print("--------------------------------------------------------------------------------------------------")
            if player_input == "a":
                print("story ongoing")
            elif player_input == "b":
                print("story ongoing")
            elif player_input == "c":
                print("Her face turns sad and she says:\"Oh, ok then bye.\"\n"
                      "ARE YOU DUMP?")
                print("<<<<<<<<<<<<<<<<<<<<|GAME OVER|>>>>>>>>>>>>>>>>>>>>")

    elif player_input == "N":
        print("Her face turns sad and she says:\"That's ok. Then bye and sorry because of the trouble.\"")
        print("<<<<<<<<<<<<<<<<<<<<|GAME OVER|>>>>>>>>>>>>>>>>>>>>")


def story2(player_name):
    print(player_name + ", you are playing story 2.")
    print("Seems really empty here. How it looks no second story yet.")
