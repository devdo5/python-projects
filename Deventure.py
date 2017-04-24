# I was really tired and rushed and couldn't give a fuck to make this look good, sorry to whoever is reading this (probably future me)
from time import sleep
from random import randint
#GLOBAL VARIABLES
goblinhp = 60
playerdamdagger = [2,3,4,5]
playerdamsword = [5,6,7,8,9,10]
playerdambow = [2,4,6,8,10,12]
difficulty = ''
meddam = [2,4,6,8,10]
intdam = [5,10,15,20]
harddam = [10,15,20,25]
hp = 50
stuff = { 'gold': 300, 'potion': 1, 'arrow': 20, 'dagger': 1}
hpthresh = 100
idk = ''

def resetvars():
    global goblinhp
    global hp
    global stuff
    goblinhp = 60
    hp = 50
    stuff = { 'gold': 300, 'potion': 1, 'arrow': 20, 'dagger': 1}
def choosediff():
    global difficulty
    print("\nWelcome to Deventure. This is a text based turn style role playing game. Responses don't need to be case sensitive when not entering numbers. Just follow the on screen instructions. Thanks for playing.")
    choice = input("\nChoose a difficulty.\
    \n1. Easy\
    \n2. Medium\
    \n3. Hard\
    \n: ")
    if choice == '1':
      print("\nEasy difficulty selected...you baby.")
    elif choice == '2':
      print("\nMedium difficulty selected. Have fun.")
    elif choice == '3':
      print("\nHard difficulty selected. Good luck, you'll need it.")
    else:
      print("\nPlease select a valid difficulty.")
      choosediff()
    difficulty = choice
    
def gameend():
  print("\nThanks for playing, i'm a shitty programmer so this was a fun and fairly simple project to do. Even though it looks simple, it took a while to make and I appreciate any feedback if you happen to want to torture yourself and look at the source code. My email is dev@udel.edu.")
  input("\nPress enter to play again, press Control-C or Control-D to exit.")
  resetvars()
  gamestart()

def isdead():
  return  bool(goblinhp <= 0)
  
def goblinturn():
  global hp
  if difficulty == '1':
    attackdmg = (meddam[randint(0,4)])
  elif difficulty == '2':
    attackdmg = (intdam[randint(0,3)])
  elif difficulty == '3':
    attackdmg = (harddam[randint(0,3)])
  print("\nThe goblin attacks you for " + str(attackdmg) + " damage.")
  hp -= attackdmg
  if hp <= 0:
    print("\nYou have died. You suck (unless this is hard mode) at this game.")
    gameend()
  else:
    combat1()  
    
    
def combat1():
  global hp
  global goblinhp
  print("\nYou have "+str(hp)+" health.")
  fight = input("\n1. Attack\
    2. Use potion\n:")
  if fight == '1':
    try:
      if stuff['sword'] > 0:
        print("\nYou strike the goblin with your sword for "+str(playerdamsword[randint(0,5)])+" damage.")
        goblinhp -= playerdamsword[randint(0,5)]
        sleep(1)
    except KeyError:
      try:
        if stuff['bow'] > 0:
            if stuff['arrow'] > 0:
                print("\nYou strike the goblin with your bow for " + str(playerdambow[randint(0,5)])+" damage.")
                goblinhp -= playerdambow[randint(0,5)]
                stuff['arrow']-= 1
                sleep(1)
            else:
                print("\nYou are out of arrows!")
      except KeyError:
          print("\nYou strike the goblin with your dagger for "+str(playerdamdagger[randint(0,3)])+" damage.")
          goblinhp -= playerdamdagger[randint(0,3)]
          sleep(1)
    if isdead() is False:
        sleep(1)
        goblinturn()
    else:
      print("\nThe goblin finally dies and falls to the ground as blood pours from its wounds. You deliver a final blow and decapitate him. Inside the cave you set the kidnapped women free and return to the village with the goblin's head as a trophy.")
      sleep(2)
      input("\nPress enter to continue.")
      gameend()
  elif fight == '2':
    if stuff['potion'] > 0:
        print("\n40 health restored with potion.")
        stuff['potion']-= 1
        hp += 40
        hpbal()
        sleep(1)
        combat1()
    else: 
        print("\nYou have no more potions!")
        sleep(1)
        combat1()
  else:
      print("\nPlease choose an option.")
      combat1()
    
  
def displayinv(inv):
    print("\nInventory:")
    for k, v in inv.items():
        if v > 1:
            if k == 'gold':
                print("\n", v, k)
            else:
                print("\n", v, k+"s")
        else:
            print("\n", v, k)
            
            
def rest():
  global hp
  sleepornah = input("\nWelcome to the inn, a room for the night costs 30 gold. You have " + str(stuff['gold'])+" gold. \nWould you like to rent a room?: ")
  if sleepornah.lower() == 'yes' or sleepornah.lower() == 'y':
    if stuff['gold'] < 30:
      print("\nYou don't have enough money.")
      intown()
    else:
      print("\nEnjoy your stay and sweet dreams...")
      sleep(3)
      hp = hpthresh 
      stuff['gold'] -= 30
      print("\nYou awaken feeling well rested. Your HP has been restored.")
      intown()
  else:
    intown()
  
def intown():
  dowhat()
  if idk is '1':
    shop1()
  elif idk is '2':
    rest()
  elif idk is '3':
   print("\nYou decide to talk to the locals...")
   sleep(1.5)
   print("\nOld Lady: My, what a handsome young man you are! My daughter could use a husband like you. She doesn't want to marry any of the village boys. Perhaps a brave adventurer like you could woo her? But who can think about marriage when there is a goblin that comes into town every night and attacks our cattle and kidnaps our women! Please do something about it. We will be forever grateful. I would buy a sword or bow from the shop and some potions too if you want to stand a chance.")
   input("\nPress enter to return to town.")
   intown()
  elif idk is '4':
    displayinv(stuff)
    intown()
  elif idk is '5':
    print("\nYou decide to venture out to kill the goblin that is terrorizing the village.\nEventually you find his cave on the mountainside. You step inside and light a torch. The walls are covered in scratches and blood. As you reach the inner sanctum, the goblin is patiently sitting on a pile of animal bones. 'I knew I smelled a human,' he says, eyeing you closely. 'I haven't tasted human flesh in quite a while...looks like it's back on the menu.' 'Come then, your meal awaits,' you say as you draw your weapon. He leaps down from his pile to meet you in combat.")
    combat1()
  else:
    print("Please select a number.")
    intown()

def dowhat():
  global idk
  whatdo = input("\nWhat would you like to do?\
  \n1. Shop\
  \n2. Rest\
  \n3. Talk\
  \n4. View Inventory\
  \n5. Leave\n:")
  idk = whatdo
  

def gamestart():
    choosediff()
    area1()
  

def hpbal():
  global hp
  if hp > hpthresh:
    hp = hpthresh


def shop1():
    global stuff
    stock = {'sword': 100, 'arrow': 3, 'bow': 75, 'potion': 50}
    print("\nWelcome to my shop. These are the items that I am selling today:\n\n1. Sword: 100 gold\n2. Arrow: 3 gold\n3. Bow: 75 gold\n4. Potion: 50 gold\nType leave to go back")
    prompt = input("\nWhich item would you like to purchase?: ")
    if prompt == '1' or prompt == '2' or prompt == '3' or prompt == '4':
      if prompt == '1':
        prompt = "sword"
      elif prompt == '2':
        prompt = 'arrow'
      elif prompt == '3':
        prompt = 'bow'
      elif prompt == '4':
        prompt = 'potion'
      prompt2 = int(input("\nHow many " + prompt + "s " + "would you like to buy?: "))
      if prompt2 < 0:
        print("\nYou can't buy negative things!")
        shop1()
      else:
        goldowe = prompt2*stock[prompt]
        print("\nThat will be " + str(goldowe) + " gold.\nYou have " + str(stuff['gold']) + " gold.")
        prompt3 = (input("\nConfirm purchase? (y/n): "))
        if prompt3.lower() == 'yes' or prompt3.lower() == 'y':
          if stuff['gold'] < goldowe:
            print("\nYou don't have enough money!")
            input("Press enter to go back.")
            shop1()
          else:
            try:
              stuff[prompt] += prompt2
              stuff['gold'] = stuff['gold'] - goldowe
              print("You bought " + str(prompt2) + " " + prompt)
              input("Press enter to keep shopping.")
              shop1()
            except KeyError:
              stuff[prompt] = 0 
              stuff[prompt] += prompt2
              stuff['gold'] = stuff['gold'] - goldowe
              print("\nYou bought " + str(prompt2) + " " + prompt)
              input("Press enter to keep shopping.")
              shop1()
        else:
          input("\nTransaction cancelled.\nPress enter to go back.")
          shop1()
    elif prompt == 'leave':
      intown()
    else:
      print("\nI'm not selling that.")
      input("\nPress enter to go back")
      shop1()
        
def area1():
  name = input("\nWelcome to the Land of Devonia young traveller, my name is Jacob and i'll be your guide. His Majesty King Devon has decree that all travellers must be treated with utmost respect and kindness.\nMay I have your name please?: ")
  print("\nGreetings, " + name + ". Follow me to the nearest village where you can rest and stock up on supplies. You seem injured, you're only at half hp! I would go to the inn and have a rest to restore your health.")
  sleep(3)
  print("\nWelcome to Dev-ville. This is my home village, i've lived here all my life! Why don't you have a look around? I highly recommend talking to the locals for jobs.")
  intown()
  
    




if __name__ == "__main__":
    gamestart()
