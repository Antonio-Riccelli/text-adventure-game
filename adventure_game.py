import random
import time
import sys

# This is set as False by default, but it's set as True
# if player visits cathedral, prior to following the voices.
# If True, when player returns to starting point, new description
# is automatically triggered.
cathedral_visited = False


def print_scene(description):
    print(description)
    input()


def incipit(prev_event=cathedral_visited):
    """Begin first scene.

    Argument:
        (bool) prev_event -- by default, this will be 'cathedral_visited'.
        If set to True, a different description is printed
        when player returns to starting point.

    Return:
        (str) choice -- returns player choice first time script is run
    """

    if prev_event is False:
        print_scene("Welcome to this short text-based adventure, "
                    "'A field in mourning'.\n"
                    "This handful of scenes was conceived as good practice in "
                    "understanding functions with Python.\n"
                    "It will hopefully be expanded to become a full game.\n"
                    "In the meantime, take delight in these descriptions "
                    "of uncanny events.\n"
                    "\n\nNote, paragraphs will print "
                    "one at a time, to give you enough time to read.\n"
                    "Just press any key to continue to the next one.")
        print_scene("\nDead of night. \n"
                    "You awaken from a slumber so profound, "
                    "feeling as if you have been asleep for aeons. "
                    "\nYour senses still numb, your vision blurry.")
        print_scene("\nYou can make out voices in the distance. \n"
                    "Hard to tell whether they come from a crowd, "
                    "fading in one big roar, or from one individual, "
                    "whose echo causes it to sound like a legion.")
        print_scene("\nRising up, standing on your feet. \n"
                    "Your muscles aching, slowly coming alive, "
                    "back from a state of semi-atrophy.")
        print_scene("\nYou find yourself in a dimly lit field. \n"
                    "What's strange, "
                    "you cannot tell where the lighting is coming from. ")
        print_scene("\nYou look around you.\nAfter carefully assessing the "
                    "situation, "
                    "you realise you have two choices: ")
        print_scene("\nYou can head for where the voices "
                    "seem to be coming from. \n"
                    "Or...")
        print_scene("\nYou can head for the opposite direction where, "
                    "in the distance, you can make out the silhouette "
                    "of a cathedral spire.\n")
        print_scene("\nWhat do you choose, o lost one?\nEnter: \n"
                    "- 'a' to head for the voices\n- "
                    "'b' to head for the cathedral\n"
                    "Or if uncertainty paralyses you "
                    "and shakes your heart...\n"
                    "- 'c' to let fate decide.")
        choice = input().strip()
        while choice != "a" and choice != "b" and choice != 'c':
            choice = input("\nThat is not a valid choice."
                           "Please type and enter either 'a', 'b', or 'c'.\n")
        time.sleep(2)
        return choice
    elif prev_event is True:
        print_scene("\nYou trace your steps back to the spot where you first"
                    "awakened.\nAfter the strange event you just witnessed, "
                    "the only way now is towards the voices."
                    "And so you head off...")
        voices()


def cathedral():
    """Run cathedral scene.

    Return:
        (bool) cathedral_visited -- by default, it will be true
        once this script runs and if player survives encounter.

        (funct) incipit(cathedral_visited) -- reruns first script,
        passing the updated argument, which triggers a different
        description.
    """

    cathedral_events = ['cathedral_a', 'cathedral_b']
    print_scene("\nYou approach the cathedral. "
                "The spire silhouette you had spotted "
                "from the distance, "
                "now reveals itself to be completely golden.")
    # time.sleep(5)
    print_scene("\nIn fact, the whole cathedral is made of gold, "
                "and the strange dim "
                "light makes it shine so bright, it almost blinds you.")
    # time.sleep(5)
    print_scene("\nSuddenly, "
                "just as you were about to start enjoying that roaring "
                "silence, the ground starts shaking.")
    # time.sleep(5)
    print_scene("\nFor a moment, "
                "it feels as if the whole world should collapse on "
                "itself, and all that's left of it will be the wreckage of an "
                "ill-fated planet, forever doomed to orbit the universe.\n"
                "You lose balance and fall to the ground.")
    # time.sleep(7)
    event = random.choice(cathedral_events)
    if event == 'cathedral_a':
        print_scene("\nJust as you thought your existence was coming to an end"
                    ", the quake-like shaking stops, "
                    "as suddenly as it had started. "
                    "But something is different...")
        # time.sleep(5)
        print_scene("\nThe golden cathedral has disappeared. "
                    "A small golden object "
                    "lies on the ground where it once stood.")
        # time.sleep(5)
        print_scene("\nIt's the effigy of a golden platypus.")
        # time.sleep(5)
        print_scene("\nYou don't know what this means, but you pick it up, "
                    "hoping it will come in handy sooner or later.")
        cathedral_visited = True
        return cathedral_visited, incipit(cathedral_visited)
    elif event == 'cathedral_b':
        print_scene("\nThis is it.")
        # time.sleep(1)
        print_scene("\nWithout an explanation or a warning, "
                    "as absurd as it could ever be, your time has come.")
        # time.sleep(1)
        print_scene("\nAs you're lying on your back whilst the shaking worsens"
                    ", the ground starts opening up.")
        # time.sleep(5)
        print_scene("\nA deep, yawning chasm embraces you, engulfs you, "
                    "and ultimately swallows you. "
                    "\nAs you cling to the last instants "
                    "of this conscious existence, "
                    "the image of a golden platypus "
                    "becomes visible to your inner eye.")
        # time.sleep(10)
        print_scene("\nYou feel drawn to it, as if this was your last chance "
                    "for some semblance of salvation.")
        # time.sleep(5)
        print_scene("\nYou head towards it. It's so familiar, so warm, "
                    "so comfortable... You take a final leap for it...")
        # time.sleep(10)
        print("\n...Silence.")
        input("\nPress any key to continue")
        restart = input("\nThis timeline is over, but other outcomes "
                        "could still be possible.\nIf you'd like to challenge "
                        "fate again, type and enter 'r', else press any other "
                        "key and persist in the nothingness you have "
                        "embraced.\n")
        if restart == 'r':
            main()
        else:
            sys.exit("Godspeed.\n")


def voices():
    """Run voices scene."""

    print_scene("\nAs you journey through the dark, the strange silhouettes "
          "of several figures become increasingly distinguishable.")
    # time.sleep(5)
    print_scene("\nIt's weird. The contours are getting clearer and clearer, "
          "yet the figures still look essentially dark.\nYou'd think that, "
          "with less distance separating the observer from the observed, "
          "you should be able to make out some colors, clothes - "
          "instead, nothing.")
    # time.sleep(10)
    print_scene("\nYou're almost there, and by now the strange reality is clear: "
          "these figures are made of sheer darkness. Carbon-based lifeforms "
          "they are not. Yet, with no other visible options, "
          "you can only keep going.")
    # time.sleep(10)
    print_scene("\nTrembling, shivering, you approach the unreal crowd, "
          "and immediately wish you had made a different choice.")
    # time.sleep(7)
    print_scene("\nIt all happens so quickly, you barely even realise it until it's "
          "already too late: part of the crowd has "
          "moved around and circled you."
          "\nYou are effectively trapped.")
    # time.sleep(7)
    print_scene("\nSomebody, you're too terrorised to even turn around and look, "
          "starts pushing you forward. You are being taken somewhere, "
          "God knows where.")
    # time.sleep(7)
    print_scene("\nSurrounded by this surreal crowd, you walk for what feels like "
          "hours but it's probably only a few minutes, until you reach the "
          "middle of some hillside.")
    # time.sleep(5)
    print_scene("\nIn what is another impossible turn of events, "
          "the crowd disappears, almost dissipates - like fog. "
          "But you sense a new presence: something else has now "
          "appeared, just slightly higher up the hillside, "
          "and is now looking down at you.")
    # time.sleep(5)
    print_scene("\nYou wonder if the crowd ever existed in the first place, "
          "or it was just an illusion, "
          "a subterfuge to lead you where you are now. "
          "In any case, it's too late now.")
    # time.sleep(5)
    print_scene("\nThe dim light you had noticed at the time of your awakening "
          "is also present in this area... and it moves over to render "
          "the new presence visible. You understand now who or what "
          "has been controlling it from the start.")
    # time.sleep(5)
    encounter()


def encounter():
    """Run encounter scene."""

    monsters = ("Mourngolem", "Coffinmask")
    random_encounter = random.choice(monsters)
    if random_encounter == "Mourngolem":
        # time.sleep(5)
        print_scene("\nYou cannot believe your own eyes, "
              "as what stands a few feet away from you is something "
              "you had only previously seen in old mythology texts: "
              "a Mourngolem.")
        # time.sleep(5)
        print_scene("\nThis creature was said to embody the pain of all those who "
              "lost a loved one. Legend has it, it would appear once "
              "a decade to lay its vengeance on someone "
              "who had taken innocent lives, "
              "causing unspeakable pain to their families who survived them.")
        # time.sleep(8)
        print_scene("\nBut why you? You've never hurt anyone in your life, "
              "let alone killed someone. This must be a mistake. "
              "Some cosmic bureaucratic error for which you "
              "are the designated victim. "
              "The injustice fills you with anger.")
        # time.sleep(8)
        print_scene("\nYou shout your rage at the Mourngolem, who stands still "
              "and silent, staring at you with eyes so empty, "
              "yet so full of doom. It marches towards you. Its steps, "
              "the sound of the inevitable.")
        # time.sleep(8)
        if cathedral_visited is True:
            print_scene("\nAs the Mourngolem takes its final step, "
                  "it now stands only a few inches away from you. "
                  "Lifting its huge arms, it prepares to strike you "
                  "with a powerful, "
                  "life-ending, blow... but something is wrong. "
                  "You feel something shaking uncontrollably, "
                  "and a light shining out of your jacket's inner pocket: "
                  "it's the effigy of the platypus you "
                  "found at the cathedral.")
            # time.sleep(15)
            print_scene("\nAs the Mourngolem sees the effigy, it stops. "
                  "It talks to you, but you can't hear any voice: "
                  "it is speaking in your mind through "
                  "some kind of telepathy.")
            # time.sleep(3)
            print_scene("\nYour memory has been obliterated, "
                  "for what you did was too gruesome to be told. "
                  "Rest assured, you are guilty. For what you have done, "
                  "you shall pay. The pain you bestowed unto others, "
                  "shall now be bestowed unto you. However, "
                  "as you carry the sacred effigy, "
                  "you shall not meet your end. "
                  "Instead, you shall help relieve the pain of "
                  "those who are left. "
                  "There is no choice to be made, this is how it shall be.")
            epilogue()
        elif cathedral_visited is False:
            print_scene("\nAs the Mourngolem takes its final step, "
                  "it now stands only a few inches away from you. "
                  "Lifting its huge arms, it strikes you with a powerful, "
                  "life-ending, blow... You barely have time "
                  "to realise what's happening, "
                  "that you are already falling into a deep nothingness. "
                  "Is this the end, or does something else await? "
                  "You will find out very soon.")
            # time.sleep(10)
            epilogue()

    elif random_encounter == "Coffinmask":
        print_scene("\nYou cannot believe your own eyes, "
              "as what hovers a few feet away from you is something "
              "you had only previously seen in old mythology texts: "
              "the Coffinmask.")
        # time.sleep(5)
        print_scene("\nThis creature was said to embody the pain of all "
              "those who lost a loved one. Legend has it, "
              "it would appear once a decade to lay its vengeance on "
              "someone who had taken innocent lives, causing "
              "unspeakable pain to their families who survived them.")
        # time.sleep(8)
        print_scene("\nBut why you? You've never hurt anyone in your life, "
              "let alone killed someone. This must be a mistake. "
              "Some cosmic bureaucratic error for which you are the "
              "designated victim. The injustice fills you with anger.")
        # time.sleep(8)
        print_scene("\nYou shout your rage at the Coffinmask, who hovers "
              "and observes you silent, staring at you with eyes so empty, "
              "yet so full of doom. It floats towards you. Its whooshing, "
              "the sound of the inevitable.")
        # time.sleep(8)
        if cathedral_visited is True:
            print_scene("\nAs the Coffinmask approaches, it now hovers only "
                  "a few inches away from you. It generates an incredibly "
                  "bright sphere of energy, preparing to strike you with a "
                  "powerful, life-ending, attack... but something is wrong. "
                  "You feel something shaking uncontrollably, and a light "
                  "shining out of your jacket's inner pocket: it's the effigy "
                  "of the platypus you found at the cathedral.")
            # time.sleep(15)
            print_scene("\nAs the Coffinmask sees the effigy, it stops. It speaks "
                  "to you, but you can't hear any voice: it is speaking "
                  "in your mind through some kind of telepathy.")
            # time.sleep(3)
            print_scene("\nYour memory has been obliterated, for what you "
                  "did was too gruesome to be told. Rest assured, "
                  "you are guilty. "
                  "For what you have done, you shall pay. "
                  "The pain you bestowed "
                  "unto others, shall now be bestowed unto you. However, as "
                  "you carry the sacred effigy, you shall not meet your end. "
                  "Instead, you shall help relieve the pain of those who are "
                  "left. There is no choice to be made, "
                  "this is how it shall be.")
            epilogue()
        elif cathedral_visited is False:
            print_scene("\nAs the Coffinmask approaches, it now hovers only "
                  "a few inches away from you. Generating a incredibly "
                  "bright sphere of energy, it strikes you with a powerful, "
                  "life-ending, attack... You barely have time to realise "
                  "what's happening, that you find yourself falling into a "
                  "deep nothingness. Is this the end, or does something else "
                  "await? You will find out very soon.")
            # time.sleep(10)
            epilogue()


def epilogue():
    """Run epilogue scene."""

    print_scene("\nStripped of the possibility to remember the actions that "
          "led you to this fate, you can only take solace in the realisation "
          "that such entities answer to forces so beyond human understanding, "
          "such that they wouldn not fall prey to lying or scheming, "
          "and that anything uttered by such entities, should be taken "
          "as unadulterated truth.")
    # time.sleep(15)
    print_scene("\nSuch realisation will help you bear the burden of the "
          "endless coming years. You look around you. The entity "
          "stares at you with bewildered but strangely complicit "
          "eyes. It's going to be an interesting story, if only "
          "there was someone to tell it to. "
          "But you will think of something...")
    # time.sleep(15)
    input("\nPress enter to continue.")
    restart = input("\nThis timeline is over, but other outcomes could "
                    "still be possible.\nIf you'd like to challenge fate "
                    "again, type and enter 'r', else press any other key "
                    "and persist in the nothingness you have embraced.\n")
    if restart == 'r':
        main()
    else:
        sys.exit("Godspeed.\n")


def main():
    """Begin story."""
    choice = incipit(cathedral_visited)
    if choice == 'a':
        voices()
    elif choice == 'b':
        cathedral()
    elif choice == 'c':
        random_choice = random.choice([0, 1])
        if random_choice == 0:
            print_scene("Fate has decreed you shall head for the voices. "
                  "And so you head off...")
            # time.sleep(2)
            voices()
        elif random_choice == 1:
            print_scene("Fate has decreed you shall head for the cathedral. "
                  "And so you head off...")
            time.sleep(2)
            cathedral()


# Block used to trigger main() function
if __name__ == "__main__":
    main()
