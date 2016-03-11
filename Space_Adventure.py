print ("Welcome to my space adventure!\n\n")
name = raw_input("What is your name cadet?!").title

print ("welcome %s" ) % name 
print ("Your vision is fuzzy as you wake up from your extremely long cryochamber slumber.")
print ("You hear a fuzzy sound of the alarm wailing in your ears as you cough up the cryo fluid")
print ("you flash back to a memory of the onboard doctor explaining why the fluid is in your lungs as you remember it is to not give you freezer burn")
print ("your vision returns and you see two doors, you barely make out the words, Engineering and Bridge")
ans = raw_input('Go to Engineering or the Bridge\n (Enter Engineering or Bridge)')

if ans == "Engineering" or "engineering":
    print ("There is an old creak as the door slides open barely for you and you have to push it the rest of the way. You walk down a vaguely lit hallway and you get to the engineering room where there is this strange creature hunched in a corner, looks at you and runs You are stunned by fear and you see the door controls to your left:")
    ans = raw_input('Lock the blast door or enter cautiously')
    if ans == "Lock":
        print ("You run to the panel and slam the close button and enter your 7 digit hexadecimal passcode followed by a \ retinal scan")
    else:
        print ("You cautiously walk into the room fully alert incase that 'Thing' wanders back in")
        print ("The monster runs back in as if it heard your movements and kills you just as quick as it left.")

else:
    print ("You start down the dark, dimly lit hallway")
    print ("You see faint movement in the darkness and you freeze in fear as you hear a huge, guttural growl")

ans = raw_input('Continue through the dark hallway despite the ever present "Thing" in the hallway with you, or search for a different\n way into the bridge?\n (Enter Continue or Search)')

if ans == "Continue" or "continue":

    print ("You cautiously move forward through the hallway towards where the creature was just growling")
    print ("The creature stands up in front of you through the darkness and you feel the heat of its foul breath against your\n face. The creature begins to tear into you as you are held still by its cold arms. You feel the life drain out of \n you and you fade out.")

else:
    print ("You turn and run back through the corridor as you get the feeling of the monster at your heels.")
    print ("There is a close sound of metal hitting metal like as if a panel was thrown at you to stop you.")

print ("You see the light of the locking system as soon as you leave the hallway. There is a shadow of a gun next to it but you are unclear if it is a real weapon or if it is your imagination.")
