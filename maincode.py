import math
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.strength = int(0)
        self.strbonus = int(0)
        self.dex = int(0)
        self.dexbonus = int(0)
        self.con = int(0)
        self.conbonus = int(0)
        self.intel = int(0)
        self.intelbonus = int(0)
        self.wis = int(0)
        self.wisbonus = int(0)
        self.cha = int(0)
        self.chabonus = int(0)
        self.hp = int(0)
        self.maxhp = int(0)
        self.armor = int(0)
        self.level = int(0)
        self.xp = int(0)
        self.inventory = []
        self.physique = physique
        self.face = face
        self.skin = skin
        self.hair = hair
        self.clothing = clothing
        self.virute = virtue
        self.vice = vice
        self.speech = speech
        self.background = background
        self.misfortune = misfortune
        self.alignment = alignment
        self.copper = int(0)
        self.inventoryslots = int(0)
        self.currentinventory = int(0)
        self.rations = int(0)


def startmenu():
    print("Hello and Welcome to the Knave Interactive Character Sheet! Select an option below by choosing a number")
    print("1.) Create a new character")
    print("2.) Load Current Character")
    option = input("-> ")
    if option == "1":
        newchar()
    if option == "2":
        load()

def newchar():
    print("Let's make a new character! You will need to roll up you stats and enter them here. Enter your name and click enter to continue.")
    Player.name = input("->")
    print("What is your strength stat?")
    Player.strength = int(input("->"))
    print("What is your strength bonus?")
    Player.strbonus = int(input("->"))
    print("What is your dexterity stat?")
    Player.dex = int(input("->"))
    print("What is your dexterity bonus?")
    Player.dexbonus = int(input("->"))
    print("What is your constitution stat?")
    Player.con = int(input("->"))
    print("What is your constitution bonus?")
    Player.conbonus = int(input("->"))
    print("What is your intelligence stat?")
    Player.intel = int(input("->"))
    print("What is your intelligence bonus?")
    Player.intelbonus = int(input("->"))
    print("What is your wisdom stat?")
    Player.wis = int(input("->"))
    print("What is your wisdom bonus?")
    Player.wisbonus = int(input("->"))
    print("What is your charisma stat?")
    Player.cha = int(input("->"))
    print("What is your charisma bonus?")
    Player.chabonus = int(input("->"))
    print("What is your level?")
    Player.level = int(input("->"))
    print("What is your xp?")
    Player.xp = int(input("->"))
    print("What is your physique")
    Player.physique = input("->")
    print("What is your face?")
    Player.face = input("->")
    print("What is your skin?")
    Player.skin = input("->")
    print("What is your hair?")
    Player.hair = input("->")
    print("What is your clothing?")
    Player.clothing = input("->")
    print("What is your virtue?")
    Player.virtue = input("->")
    print("What is your vice?")
    Player.vice = input("->")
    print("What is your speech?")
    Player.speech = input ("->")
    print("What is your background?")
    Player.background = input("->")
    print("What is your misfortune?")
    Player.misfortune = input("->")
    print("What is your alignment?")
    Player.alignment = input("->")
    print("What is your armor stat?")
    Player.armor = int(input("->"))
    print("What is your max HP?")
    Player.maxhp = int(input("->"))
    print("How many rations do your start with?")
    Player.rations = int(input("->"))
    print("How many copper do you start with?")
    Player.copper = int(input("->"))
    print("How many Inventory Slots do you start with?")
    Player.inventoryslots = int(input("->"))
    print("How many Inventory slots are currently full right now?")
    Player.currentinventory = int(input("->"))
    Player.hp = Player.maxhp
    mainscreen()

def mainscreen():

    nameplate = "Name: " + Player.name
    hp = "HP: " + str(Player.hp) + "/" + str(Player.maxhp)
    plevel = "Level: " + str(Player.level)
    money = "Copper: " + str(Player.copper)
    food = "Rations: " + str(Player.rations)
    inventoryslots = "Inventory Slots: " + str(Player.currentinventory) + "/" + str(Player.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    commandoptions1 = "1.) Attack"
    commandoptions2 = "2.) Change HP"
    commandoptions3 = "3.) Change Level"
    commandoptions4 = "4.) Change Copper Amount"
    commandoptions5 = "5.) Change Stats"
    commandoptions6 = "6.) Consume Ration"
    commandoptions7 = "7.) View Inventory"
    commandoptions8 = "8.) Change Inventory"
    commandoptions9 = "9.) Save Current State"
    strline = str(Player.strength) + "       " + " STR        " + str(Player.strbonus)
    dexline = str(Player.dex) + "       " + " DEX        " + str(Player.dexbonus)
    conline = str(Player.con) + "       " + " CON        " + str(Player.conbonus)
    intline = str(Player.intel) + "       " + " INT        " + str(Player.intelbonus)
    wisline = str(Player.wis) + "       " + " WIS        " + str(Player.wisbonus)
    chaline = str(Player.cha) + "       " + " CHA        " + str(Player.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print(commandoptions1.center(40, " ")
    print(commandoptions2.center(40, " ")
    print(commandoptions3.center(40, " ")
    print(commandoptions4.center(40, " ")
    print(commandoptions5.center(40, " ")
    print(commandoptions6.center(40, " ")
    print(commandoptions7.center(40, " ")
    print(commandoptions8.center(40, " ")
    print(commandoptions9.center(40, " ")
    print("Select command optiont by selecting a number.")
    option = input("->")
    if option == "1":
          attack()
    if option == "2":
          changehp()
    if option == "3":
          changelevel()
    if option == "4":
          changecopper()
    if option == "5":
          changestats()
    if option == "6":
          consumeration()
    if option == "7":
          viewinventory()
    if option == "8":
          changeinventory()
    if option == "9":
          savegame()
    else:
          print("Invalid choice, click enter to try again")
          input("->")
          mainscreen()
          



startmenu()

######YEAHHHHHH
 #yup





