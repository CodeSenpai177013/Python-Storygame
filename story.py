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
          "\"It´s not an official club yet because i´m the only member, but i can guarantee it will be fun.\"\n")
    print("--------------------------------------------------------------------------------------------------")
    player_input = input("Are you joining the shogi club with the cute Girl? (Y/N) ")
    print("--------------------------------------------------------------------------------------------------")

    if player_input == "Y":
        print("You say:""\"Yes i would like to join. But my shogi skills are not that good.\"\n"
              "She smiles at you and say:\"That's no problem, i´ll teach you.\"\n"
              "She asks:\"Whats your name?\"\n"
              "You respond with:\"My name is " + player_name + "\"! I hope can become good friends.\n"
              "She says:\"I hope that too, " + player_name + ".\"\n"
              "You say bye to Urushi and walk to your class.\n")
        print("--------------------------------------------------------------------------------------------------")
        print("You have taken seat in class and you are waiting for the class to start,\n"
              "when you hear someone calling you from behind.\n"
              "The voice says:\"Did you join the kendo club? I haven't seen you there.\"\n"
              "You turn around and see your childhood friend Takeru.\n"

              )



    elif player_input == "N":
        print("Her face turns sad and she says:\"That's ok. Then bye and sorry because of the flyers.\"")
        print("YOU LOST")


def story2(player_name):
    print(player_name + ", you are playing story 2.")
