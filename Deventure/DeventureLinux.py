#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep
from random import randint
from os import system

#########GLOBAL VARIABLES###################

name = ''
goblinhp = 60
werewolfhp = 100
dragonhp = 200
playerdamdagger = [2, 3, 4, 5]
playerdamsword = [5, 6, 7, 8, 9, 10,]
playerdamrapier = [2, 4, 6, 8]
difficulty = ''
goblindam = [2, 4, 6, 8, 10]
werewolfdam = [5, 10, 15, 20]
dragondam = [10, 15, 20, 25]
hp = 50
mana = 100
manathresh = 100
bag = {
    'gold': 300,
    'health potion': 1,
    'mana potion': 1,
    'dagger': 1,
    }
hpthresh = 100
choice = None
talked = False
bossdead = False
given = False



############################################

# Clear screen function (Linux)

def clear():
  print("c")


# Resets variables if you play again

def resetvars():
    global goblinhp
    global hp
    global bag
    global werewolfhp
    global dragonhp
    global mana
    global hpthresh
    global given
    global bossdead
    global talked
    global choice
    given = False
    bossdead = False
    talked = False
    choice = None
    goblinhp = 60
    werewolfhp = 100
    dragonhp = 200
    hp = 50
    hpthresh = 100
    mana = 100
    bag = {
        'gold': 300,
        'health potion': 1,
        'dagger': 1,
        'mana potion': 1,
        }


# Balances your HP, if you try to heal more than your total hp, cap it at the total

def hpbal():
    global hp
    if hp > hpthresh:
        hp = hpthresh


# Balances your mana

def manabal():
    global mana
    if mana > manathresh:
        mana = manathresh


# Choose difficulty

def choosediff():
    global difficulty
    print('\nWelcome to Deventure. This is a text based turn style role playing\
 game. Just follow the on screen instructions and enter the number of your\
 choice. Keep in mind that if your terminal is too small, you may need to scroll up to be able to read everything.')
    choice = \
        input("""
Choose a difficulty.\
    
1. Easy\
    
2. Medium\
    
3. Impossible\
    
> """)
    if choice == '1':
        print ('\nEasy difficulty selected...you baby.')
    elif choice == '2':
        print ('\nMedium difficulty selected. Have fun.')
    elif choice == '3':
        print ("\nImpossible difficulty selected. Good luck, you'll\
        need it.")
    else:
        print ('\nPlease select a valid difficulty.')
        choosediff()
    difficulty = choice


# First area function

def area1():
    global name
    name = \
        input("""
Welcome to the Land of Devonia young traveller, my name is Jacob and i'll be\
 your guide. His Majesty King Devon has decree that all travellers must be\
 treated with utmost respect and kindness.
 May I have your name please?\n> """)
    clear()
    print ('\nGreetings, ' + name \
        + ". Follow me to the nearest village where you can rest and stock\
 up on supplies. You seem injured, you're only at half hp! I would\
 go to the inn and have a rest to restore your health.")
    input('\nPress enter to continue.')
    print ("\nWelcome to Dev-ville. This is my home village, i've lived here\
 all my life! Why don't you have a look around? I highly recommend talking\
 to the locals for jobs.")
    intown1()

# Second area function

def wizardencounter():
    global bossdead
    bossdead = False
    clear()
    input("You head out of town as the villagers say their last goodbyes. Feeling content and ready to leave, you head out into the wilderness towards the next town...\n\nPress enter to continue")
    clear()
    input("You hear a commotion up ahead and run to see what it is. An old man is being attack by a cyclops in a small clearing. 'PLEASE, THROW ME A MANA POTION FROM MY BAG!' You look around for his bag, find the glowing blue vial and toss it to him. He downs it in one gulp and his eyes glow blue with vigor. He turns to the cyclops and in one swift motion, launches a flaming projectile at it. It explodes and splashes all over the creature like napalm. The cyclops desperately tries to get the flames off but to no avail. Eventually it is reduced to a pile of melted flesh and bones.\n\nPress enter to continue")
    clear()
    input("The man walks up to you, relieved. 'Am I glad that you arrived, traveller. I am truly grateful for your assistance. How unlucky to be caught out of mana by a cyclops. I'm not as young as a I used to be.' He strokes his beard while examining you closely. 'Are you attuned to the fine arts, by any chance? I can sense magical potential inside you.' He thinks for a moment, then rummages though his bag and hands you a book. 'It's getting dark, I better get going. Here have a book as a token of my thanks. You can just read it on your spare time. May our paths cross again!' He had a sly grin on his face as he handed it to you and walked into the trees...\n\nPress enter to continue")
    clear()
    input("You look at the book. It's bound by leather and has intricate markings and shapes on the front. The pages inside are all blank. 'Crazy old man...' you think to yourself. Suddenly, ancient inscriptions appear on the pages with a purple glow. You can't read them but for some reason they have meaning. Your heart starts beating hard and your blood feels hot like fire in your veins. Your fingertips burn as if they are close to burning coals. Your head rushes as if a strong wind is blowing inside of it. A loud thunderclap ends the process and book turns into ash in your hands.\n\nYou have learned Fireball.\n\nPress enter to continue")


# End game screen

def gameend():
    print ('\nThanks for playing. If you have any feedback just email me at\
 dev@udel.edu. Keep up with further updates at www.udel.edu/~dev/. Please\
 send money.')
    input('\nPress enter to play again.')
    clear()
    resetvars()
    gamestart()


# Displays the player's inventory and stats

def displayinv(inv):
    print ('\nInventory:')
    for (k, v) in inv.items():
        if v > 1:
            if k == 'gold':
                print (v, k)
            else:
                print (v, k + 's')
        else:
            print (v, k)
    print("\nStats:\n" + str(hp) + " HP\n" + str(mana) +" Mana")
# Checks to see if the goblin is dead

def isdead1():
    return bool(goblinhp <= 0)


# Checks to see if the werewolf is dead

def isdead2():
    return bool(werewolfhp <= 0)


# Checks to see if the dragon is dead

def isdead3():
    return bool(dragonhp <= 0)


# Goblin's attack turn, checks if you're dead after every attack

def goblinturn():
    global hp
    if difficulty == '1':
        attackdmg = goblindam[randint(0, 4)] * 1
    elif difficulty == '2':
        attackdmg = goblindam[randint(0, 4)] * 2
    elif difficulty == '3':
        attackdmg = goblindam[randint(0, 4)] * 3
    print ('\nThe goblin attacks you for ' + str(attackdmg) + ' damage.')
    hp -= attackdmg
    if hp <= 0:
        clear()
        print ('\nYou have died.')
        gameend()
    else:
        combat1()

# Werewolf attack turn

def werewolfturn():
    global hp
    if difficulty == '1':
        attackdmg = werewolfdam[randint(0, 3)] * 1
    elif difficulty == '2':
        attackdmg = werewolfdam[randint(0, 3)] * 2
    elif difficulty == '3':
        attackdmg = werewolfdam[randint(0, 3)] * 3
    print ('\nThe werewolf slashes you for ' + str(attackdmg) \
        + ' damage.')
    hp -= attackdmg
    if hp <= 0:
        clear()
        print ('\nYou have died.')
        gameend()
    else:
        combat2()


# Dragon attack turn

def dragonturn():
    global hp
    if difficulty == '1':
        attackdmg = dragondam[randint(0, 3)] * 1
    elif difficulty == '2':
        attackdmg = dragondam[randint(0, 3)] * 2
    elif difficulty == '3':
        attackdmg = dragondam[randint(0, 3)] * 3
    print ('\nThe dragon bites you for ' + str(attackdmg) + ' damage.')
    hp -= attackdmg
    if hp <= 0:
        clear()
        print ('\nYou have died.')
        gameend()
    else:
        combat3()


# Main combat function for the first area

def combat1():
    global bossdead
    global hp
    global goblinhp
    global gold
    print ('\nYou have ' + str(hp) + ' health.')
    fight = \
        input("""
1. Attack
2. Use health potion
> """)
    if fight == '1':
        try:
            if bag['sword'] > 0:
                print ('\nYou strike the goblin with your sword for ' \
                    + str(playerdamsword[randint(0, 5)]) + ' damage.')
                goblinhp -= playerdamsword[randint(0, 5)]
                sleep(1)
        except KeyError:
            try:
                if bag['rapier'] > 0:
                    print ('\nYou stab the goblin with your rapier for ' \
                        + str(playerdamrapier[randint(0, 3)]) \
                        + ' damage.')
                goblinhp -= playerdamrapier[randint(0, 3)]
                sleep(1)
            except KeyError:
                print ('\nYou strike the goblin with your dagger for ' \
                    + str(playerdamdagger[randint(0, 3)]) + ' damage.')
                goblinhp -= playerdamdagger[randint(0, 3)]
                sleep(1)
        if isdead1() is False:
            sleep(1)
            clear()
            goblinturn()
        else:
            clear()
            print ("\nThe goblin finally dies and falls to the ground as blood\
 pours from its wounds. You deliver a final blow and decapitate him.\
 Inside the cave you set the kidnapped women free and return to the\
 village with the goblin's head as a trophy.")
            sleep(2)
            bossdead = True
            input('\nPress enter to continue.')
            clear()
            print ("""
When you return to town, the villagers welcome you with fanfare. You are \
showered with flower petals and people shout praises from windows. Feasts and\
 drinking have started all over the village as the celebrations begin. 'Traveler\
 you are nothing but a blessing for us this day. Please, take this gold as a\
 token of our gratitude. Before you go, please feast and celebrate with us, it\
 is only tradition.

\nYou obtain 1000 gold.

The old lady from earlier beckons you over to speak with her again.
""")
            bag['gold'] += 1000
            intown1()
    elif fight == '2':
        if bag['health potion'] > 0:
            print ('\n40 health restored with health potion.')
            bag['health potion'] -= 1
            hp += 40
            hpbal()
            sleep(1)
            clear()
            combat1()
        else:
            print ('\nYou have no more health potions!')
            sleep(1)
            clear()
            combat1()
    else:
        print ('\nPlease choose an option.')
        combat1()

# Second area combat function

def combat2():
    global isdead2
    global hp
    global werewolfhp
    global gold
    global mana
    print ('\nYou have ' + str(hp) + ' health and ' + str(mana) + ' mana.')
    fight = \
        input("""
1. Attack
2. Fireball (20mp)
3. Use health potion
4. Use mana potion
> """)
    if fight == '1':
        try:
            if bag['sword'] > 0:
                print ('\nYou strike the werewolf with your sword for ' \
                    + str(playerdamsword[randint(0, 5)]) + ' damage.')
                werewolfhp -= playerdamsword[randint(0, 5)]
                sleep(1.5)
        except KeyError:
            try:
                if bag['rapier'] > 0:
                    print ('\nYou stab the werewolf with your rapier for ' \
                        + str(playerdamrapier[randint(0, 3)]) \
                        + ' damage.')
                werewolfhp -= playerdamrapier[randint(0, 3)]
                sleep(1.5)
            except KeyError:
                print ('\nYou strike the werewolf with your dagger for ' \
                    + str(playerdamdagger[randint(0, 3)]) + ' damage.')
                werewolfhp -= playerdamdagger[randint(0, 3)]
                sleep(1)
        if isdead2() is False:
            sleep(1.5)
            clear()
            werewolfturn()
        else:
            clear()
            print ("\nThe werewolf finally dies and falls to the ground as blood\
 pours from its wounds. You deliver a final blow and decapitate him.\
 Inside the cave you set the kidnapped women free and return to the\
 village with the goblin's head as a trophy.")
            sleep(2)
            input('\nPress enter to continue.')
            clear()
            print ("""
When you return to town, the villagers welcome you with fanfare. You are \
showered with flower petals and people shout praises from windows. Feasts and\
 drinking have started all over the village as the celebrations begin. 'Traveler\
 you are nothing but a blessing for us this day. Please, take this gold as a\
 token of our gratitude. Before you go, please feast and celebrate with us, it\
 is only tradition.

You obtain 1000 gold.

The old lady from earlier beckons you over to speak with her again.
""")
            bag['gold'] += 1000
            intown1()
    elif fight == '2':
        if mana >= 20:
            print ('\nYou fireball the werewolf for 15 damage.')
            mana -= 20
            werewolfhp -= 15
            if isdead2() is False:
                sleep(1)
                clear()
                werewolfturn()
            else:
                clear()
                print ("\nThe goblin finally dies and falls to the ground as\
 blood pours from its wounds. You deliver a final blow and \
decapitate him. Inside the cave you set the kidnapped women\
 free and return to the village with the goblin's head as a\
 trophy.")
                sleep(2)
                input('\nPress enter to continue.')
                clear()
                print ("""
When you return to town, the villagers welcome you with fanfare. You are \
showered with flower petals and people shout praises from windows. Feasts and\
 drinking have started all over the village as the celebrations begin. 'Traveler\
 you are nothing but a blessing for us this day. Please, take this gold as a\
 token of our gratitude. Before you go, please feast and celebrate with us, it\
 is only tradition. The old lady from earlier beckons you to go over and speak with her again.
\nYou obtain 1000 gold.""")
                bag['gold'] += 1000
                intown1()
        else:
            print ("\nYou don't have enough mana to cast this spell!")
            sleep(1)
            clear()
            combat2()
    elif fight == '4':
        if bag['mana potion'] > 0:
            print ('\n40 mana restored with mana potion.')
            bag['mana potion'] -= 1
            mana += 40
            manabal()
            sleep(1)
            clear()
            combat2()
        else:
            print ('\nYou have no more mana potions!')
            sleep(1)
            clear()
            combat2()
    elif fight == '3':
        if bag['health potion'] > 0:
            print ('\n40 health restored with health potion.')
            bag['health potion'] -= 1
            hp += 40
            hpbal()
            sleep(1)
            clear()
            combat2()
        else:
            print ('\nYou have no more health potions!')
            sleep(1)
            clear()
            combat2()
    else:
        print ('\nPlease choose an option.')
        combat2()



# Main shop function

def shop1():
    global bag
    stock = {
        'sword': 100,
        'rapier': 75,
        'mana potion': 30,
        'health potion': 50,
        }
    print ('''
Welcome to my shop. These are the items that I am selling today:

1. Bronze Sword: 100 gold
2. Bronze Rapier: 75 gold
3. Health Potion: 50 gold
4. Leave''')
    prompt = input('\nWhich item would you like to purchase?\n> ')
    if prompt == '1' or prompt == '2' or prompt == '3':
        if prompt == '1':
            prompt = 'sword'
        elif prompt == '2':
            prompt = 'rapier'
        elif prompt == '3':
            prompt = 'health potion'
        prompt2 = (input('\nHow many ' + prompt + 's '
                      + 'would you like to buy?\n> '))
        try:
            prompt2 = int(prompt2)
            if prompt2 < 0:
                print ("\nYou can't buy negative things!")
                clear()
                shop1()
            else:
                goldowe = prompt2 * stock[prompt]
                print ('\nThat will be ' + str(goldowe) \
                    + ' gold.\nYou have ' + str(bag['gold']) + ' gold.')
                prompt3 = input('\nConfirm purchase?\n> ')
                if prompt3.lower() == 'yes' or prompt3.lower() == 'y':
                    if bag['gold'] < goldowe:
                        print ("\nYou don't have enough money!")
                        input('Press enter to go back.')
                        clear()
                        shop1()
                    else:
                        try:
                            bag[prompt] += prompt2
                            bag['gold'] -= goldowe
                            print ('You bought ' + str(prompt2) + ' ' \
                                + prompt)
                            input('Press enter to keep shopping.')
                            clear()
                            shop1()
                        except KeyError:
                            bag[prompt] = 0
                            bag[prompt] += prompt2
                            bag['gold'] -= goldowe
                            print ('\nYou bought ' + str(prompt2) + ' ' \
                                + prompt)
                            input('Press enter to keep shopping.')
                            clear()
                            shop1()
                else:
                    input('''
Transaction cancelled.
Press enter to go back.''')
                    clear()
                    shop1()
        except ValueError:
            print("\nPlease enter a number.")
            input("\nPress enter to go back")
            clear()
            shop1()
    elif prompt == '4':
        clear()
        intown1()
    else:
        print ("\nI'm not selling that.")
        input('\nPress enter to go back')
        clear()
        shop1()


# Rest at the inn to fully restore your health

def rest1():
    global hp
    global mana
    sleepornah = \
        input('\nWelcome to the inn, a room for the night costs 30 gold. \
You have '
               + str(bag['gold'])
              + ' gold. \nWould you like to rent a room?\n> ')
    if sleepornah.lower() == 'yes' or sleepornah.lower() == 'y':
        if bag['gold'] < 30:
            print ("\nYou don't have enough money.")
            intown1()
        else:
            print ('\nEnjoy your stay and sweet dreams...')
            sleep(3)
            clear()
            hp = hpthresh
            mana = manathresh
            bag['gold'] -= 30
            print ('\nYou awaken feeling well rested. Your HP and Mana have been \
restored.')
            intown1()
    else:
        clear()
        intown1()

def rest2():
    global hp
    global mana
    sleepornah = \
        input('\nWelcome to the inn, a room for the night costs 30 gold. \
You have '
               + str(bag['gold'])
              + ' gold. \nWould you like to rent a room?\n> ')
    if sleepornah.lower() == 'yes' or sleepornah.lower() == 'y':
        if bag['gold'] < 30:
            print ("\nYou don't have enough money.")
            intown2()
        else:
            print ('\nEnjoy your stay and sweet dreams...')
            sleep(3)
            clear()
            hp = hpthresh
            mana = manathresh
            bag['gold'] -= 30
            print ('\nYou awaken feeling well rested. Your HP and Mana have been \
restored.')
            intown2()
    else:
        clear()
        intown2()
# Main function for being in town

def intown1():
    global talked
    global given
    global bag
    global hpthresh
    dowhat()
    if choice is '1':
        shop1()
    elif choice is '2':
        rest1()
    elif choice is '3':
        print ('\nYou decide to talk to the locals...')
        sleep(1.5)
        if bossdead is False:
            print ("\nOld Lady: My, what a handsome young man you are! My \
daughter could use a husband like you. She doesn't want to marry\
 any of the village boys. Perhaps a brave adventurer like you could\
 woo her? But who can think about marriage when there is a goblin\
 that comes into town every night and attacks our cattle and kidnaps\
 our women! Please do something about it. We will be forever grateful.\
 I would buy a better weapon from the shop and some potions too if you\
 want to stand a chance!")
            talked = True
            input('\nPress enter to return to town.')
            clear()
            intown1()
        else:
            if given is False:
                print ('\nOld Lady: My goodness you did it! We will be forever\
 grateful! Please, take this family heirloom as a token of my\
 gratitude! Now please, go to the next town and see if they need any\
 help.')
                print ('''
You obtained Ancestral Armor.
You armor has increased by 10%.''')
                bag['ancestral armor'] = 1
                hpthresh += 10
                given = True
                input('\nPress enter to return to town.')
                clear()
                intown1()
            else:
                print ('\nThank you for your brave acts, hero. Please, go\
 to the next town and see if they need help. Your work here\
 is done.')
                input('\nPress enter to return to town.')
                clear()
                intown1()
    elif choice is '4':
        clear()
        displayinv(bag)
        intown1()
    elif choice is '5':
        if goblinhp <= 0:
            wizardencounter()
            area2()
            combat2()
        else:
            print ("""
You decide to venture out to kill the goblin that is terrorizing the village.
Eventually you find his cave on the mountainside. You step inside and light\
 a torch. The walls are covered in scratches and blood. As you reach the inner\
 sanctum, the goblin is patiently sitting on a pile of animal bones. 'I knew I\
 smelled a human,' he says, eyeing you closely. 'I haven't tasted human flesh\
 in quite a while...looks like it's back on the menu.' 'Come then, your meal\
 awaits,' you say as you draw your weapon. He leaps down from his pile to\
 meet you in combat.""")
            combat1()
    else:
        print ('Please select a number.')
        intown1()

def shop2():
    global bag
    stock = {
        'sword': 200,
        'rapier': 150,
        'mana potion': 60,
        'health potion': 100,
        }
    print ('''
Welcome to my shop. These are the items that I am selling today:

1. Silver Sword: 200 gold
2. Silver Rapier: 150 gold
3. Health Potion: 100 gold
4. Mana Potion: 60 gold
5. Leave''')
    prompt = input('\nWhich item would you like to purchase?\n> ')
    if prompt == '1' or prompt == '2' or prompt == '3' or prompt == '4':
        if prompt == '1':
            prompt = 'sword'
        elif prompt == '2':
            prompt = 'rapier'
        elif prompt == '3':
            prompt = 'health potion'
        elif prompt == '4':
            prompt = 'mana potion'
        prompt2 = (input('\nHow many ' + prompt + 's '
                      + 'would you like to buy?\n> '))
        try:
            prompt2 = int(prompt2)
            if prompt2 < 0:
                print ("\nYou can't buy negative things!")
                clear()
                shop2()
            else:
                goldowe = prompt2 * stock[prompt]
                print ('\nThat will be ' + str(goldowe) \
                    + ' gold.\nYou have ' + str(bag['gold']) + ' gold.')
                prompt3 = input('\nConfirm purchase?\n> ')
                if prompt3.lower() == 'yes' or prompt3.lower() == 'y':
                    if bag['gold'] < goldowe:
                        print ("\nYou don't have enough money!")
                        input('Press enter to go back.')
                        clear()
                        shop2()
                    else:
                        try:
                            bag[prompt] += prompt2
                            bag['gold'] -= goldowe
                            print ('You bought ' + str(prompt2) + ' ' \
                                + prompt)
                            input('Press enter to keep shopping.')
                            clear()
                            shop2()
                        except KeyError:
                            bag[prompt] = 0
                            bag[prompt] += prompt2
                            bag['gold'] -= goldowe
                            print ('\nYou bought ' + str(prompt2) + ' ' \
                                + prompt)
                            input('Press enter to keep shopping.')
                            clear()
                            shop2()
                else:
                    input('''
Transaction cancelled.
Press enter to go back.''')
                    clear()
                    shop2()
        except ValueError:
            print("\nPlease enter a number.")
            input("\nPress enter to go back")
            clear()
            shop2()
    elif prompt == '5':
        clear()
        intown2()
    else:
        print ("\nI'm not selling that.")
        input('\nPress enter to go back')
        clear()
        shop2()

def intown2():
    global talked
    global given
    global bag
    global hpthresh
    bossdead = False
    dowhat()
    if choice is '1':
        shop2()
    elif choice is '2':
        rest2()
    elif choice is '3':
        print ('\nYou decide to talk to the locals...')
        sleep(1.5)
        if bossdead is False:
            print ("\nGovernor: The Goblin Slayer himself! What brings you to Devista huh? Don't even tell me, because I know. You came here to slay that damned werewolf that's been killing our hunters. We're worried that he might attack the town one night. These walls are good against humans but that creature can jump over it. There will be a hefty reward if you bring me his head. Our town shop is well stocked with silver weapons, they are way stronger than those silly bronze weapons. Stay safe out there!")
            talked = True
            input('\nPress enter to return to town.')
            clear()
            intown2()
        else:
            if given is False:
                print ("\nGovernor: Well I'll be damned, you actually did it! I'll be honest I thought you were dead.")
                print ('''
You obtained the rank of Thane of Devista and the Werewolf Pelt.
Your armor has increased by 10%''')
                bag['werewolf pelt'] = 1
                hpthresh += 10
                given = True
                input('\nPress enter to return to town.')
                clear()
                intown2()
            else:
                print ("\n If it isn't my favorite (and only) Thane! How are you my friend. I hear the women love your rank, don't use that to your advantage hehe. Anyway, I hear the town over is dealing with some sort of monster related issue. I would go over there and check it out. Now that you're " + name + " The Goblin and Werewolf Slayer! Good luck out there.")
                input('\nPress enter to return to town.')
                clear()
                intown2()
    elif choice is '4':
        clear()
        displayinv(bag)
        intown2()
    elif choice is '5':
        if werewolfhp <= 0:
    
            area3()
        else:
            print ("""
You decide to venture out to kill the NIGGER that is terrorizing the village.\
 Eventually you find his cave on the mountainside. You step inside and light\
 a torch. The walls are covered in scratches and blood. As you reach the inner\
 sanctum, the goblin is patiently sitting on a pile of animal bones. 'I knew I\
 smelled a human,' he says, eyeing you closely. 'I haven't tasted human flesh\
 in quite a while...looks like it's back on the menu.' 'Come then, your meal\
 awaits,' you say as you draw your weapon. He leaps down from his pile to\
 meet you in combat.""")
            combat2()
    else:
        print ('Please select a number.')
        intown1()

# Broke down intown into another function for ease

def dowhat():
    global choice
    if talked is True:
        whatdo = \
            input("""
What would you like to do?\
    
1. Shop\
    
2. Rest\
    
3. Talk\
    
4. View Inventory/Stats\
    
5. Leave Town
> """)
        choice = whatdo
        clear()
    else:
        whatdo = \
            input("""
What would you like to do?\
    
1. Shop\
    
2. Rest\
    
3. Talk\
    
4. View Inventory/Stats
> """)
        choice = whatdo
        clear()
# Second area function

def area2():
    clear()
    input("Eventually you happen upon the next village. Slightly bigger than the previous; this village actually has a small wall around it. At the gate, you try to walk right in but are met by some guards. 'Halt, outsider. What brings you here?' Before you can say anything, the second guard asks,'Oi hold on, aren't you " + name + "? The Goblin Slayer? Come right in then! the Governor would like to speak with you immediately!\n\nPress enter to continue")
    clear()
    intown2()

# Starts the game

def gamestart():
    choosediff()
    area1()


# Clears the terminal and starts the game when the file is run directly.

if __name__ == '__main__':
    clear()
    gamestart()
