import math
import random
import os
import pickle
import sys

global PlayerIG

class Player:
    def __init__(self, name):
        self.name = name
        self.strength = 0
        self.strbonus = 0
        self.dex = 0
        self.dexbonus = 0
        self.con = 0
        self.conbonus = 0
        self.intel = 0
        self.intelbonus = 0
        self.wis = 0
        self.wisbonus = 0
        self.cha = 0
        self.chabonus = 0
        self.hp = 0
        self.maxhp = 0
        self.armor = 0
        self.level = 0
        self.xp = 0
        self.inventory = {"Basic Clothes": 0}
        self.physique = " "
        self.face = " "
        self.skin = " "
        self.hair = " "
        self.clothing = " "
        self.virtue = " "
        self.vice = " "
        self.speech = " "
        self.background = " "
        self.misfortune = " "
        self.alignment = " "
        self.copper = 0
        self.inventoryslots = 0
        self.currentinventory = 0
        self.rations = 0



def startmenu():
    print("                               _  ___   _     __      ________ _    _ _____")
    print("                              | |/ / \ | |   /\ \    / /  ____| |  | |_   _|")
    print("                              | ' /|  \| |  /  \ \  / /| |__  | |  | | | |")
    print("                              |  < | . ` | / /\ \ \/ / |  __| | |  | | | |")
    print("                              | . \| |\  |/ ____ \  /  | |____| |__| |_| |")
    print("                              |_|\_\_| \_/_/    \_\/   |______|\____/|_____|")
    print("\n")
    print("\n")
    print("                                             Developed by:")
    print("\n")
    print("                                                 PyRev")
    print("\n")
    print("\n")
    print("                         Hello and Welcome to the Knave Interactive Character Sheet!")
    print("                                       Select an option to continue.")
    print("\n")
    print("                                     1.) Create a new character")
    print("                                     2.) Load Current Character")
    option = input("-> ")
    if option == "1":
        startup()
    if option == "2":
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open("savefile", "rb") as f:
                os.getcwd()
                global PlayerIG
                PlayerIG = pickle.load(f)
                print("Loaded save state...your journey continues!")
                input("->")
                mainscreen()
        else:
            print("No saved data.")
            startmenu()
    else:
        startmenu()


def startup():
    print("NOTE: WHEN ASKED FOR A NUMBER ENTER A NUMBER, WHEN ASKED FOR A TRAIT, USE LETTERS. FAILURE TO DO SO WILL CAUSE CRASH.")
    print("Let's make a new character! You will need to roll up you stats and enter them here. Enter your name and click enter to continue.")
    option = input("->")
    global PlayerIG
    PlayerIG = Player(option)
    newchar()


def newchar():
    print("What is your strength stat?")
    PlayerIG.strength = int(input("->"))
    print("What is your strength bonus?")
    PlayerIG.strbonus = int(input("->"))
    print("What is your dexterity stat?")
    PlayerIG.dex = int(input("->"))
    print("What is your dexterity bonus?")
    PlayerIG.dexbonus = int(input("->"))
    print("What is your constitution stat?")
    PlayerIG.con = int(input("->"))
    print("What is your constitution bonus?")
    PlayerIG.conbonus = int(input("->"))
    print("What is your intelligence stat?")
    PlayerIG.intel = int(input("->"))
    print("What is your intelligence bonus?")
    PlayerIG.intelbonus = int(input("->"))
    print("What is your wisdom stat?")
    PlayerIG.wis = int(input("->"))
    print("What is your wisdom bonus?")
    PlayerIG.wisbonus = int(input("->"))
    print("What is your charisma stat?")
    PlayerIG.cha = int(input("->"))
    print("What is your charisma bonus?")
    PlayerIG.chabonus = int(input("->"))
    print("What is your level?")
    PlayerIG.level = int(input("->"))
    print("What is your xp?")
    PlayerIG.xp = int(input("->"))
    print("What is your physique")
    PlayerIG.physique = input("->")
    print("What is your face?")
    PlayerIG.face = input("->")
    print("What is your skin?")
    PlayerIG.skin = input("->")
    print("What is your hair?")
    PlayerIG.hair = input("->")
    print("What is your clothing?")
    PlayerIG.clothing = input("->")
    print("What is your virtue?")
    PlayerIG.virtue = input("->")
    print("What is your vice?")
    PlayerIG.vice = input("->")
    print("What is your speech?")
    PlayerIG.speech = input("->")
    print("What is your background?")
    PlayerIG.background = input("->")
    print("What is your misfortune?")
    PlayerIG.misfortune = input("->")
    print("What is your alignment?")
    PlayerIG.alignment = input("->")
    print("What is your armor stat?")
    PlayerIG.armor = int(input("->"))
    print("What is your max HP?")
    PlayerIG.maxhp = int(input("->"))
    print("How many rations do your start with?")
    PlayerIG.rations = int(input("->"))
    print("How many copper do you start with?")
    PlayerIG.copper = int(input("->"))
    print("How many Inventory Slots do you start with?")
    PlayerIG.inventoryslots = int(input("->"))
    PlayerIG.hp = PlayerIG.maxhp
    PlayerIG.inventory = {"Basic Clothes": 0}
    mainscreen()


def mainscreen():
    global PlayerIG
    os.system('cls')
    if PlayerIG.hp <= 0:
        dead()
    if PlayerIG.hp > PlayerIG.maxhp:
        PlayerIG.hp = PlayerIG.maxhp
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    commandoptions1 = "1.) Dice Roller and Attack"
    commandoptions2 = "2.) Change HP"
    commandoptions3 = "3.) Change Level"
    commandoptions4 = "4.) Change Copper Amount"
    commandoptions5 = "5.) Change Stats"
    commandoptions6 = "6.) Change Ration Amount"
    commandoptions7 = "7.) View Inventory"
    commandoptions8 = "8.) Change Inventory"
    commandoptions9 = "9.) Save Current State"
    print("                               _  ___   _     __      ________ _    _ _____")
    print("                              | |/ / \ | |   /\ \    / /  ____| |  | |_   _|")
    print("                              | ' /|  \| |  /  \ \  / /| |__  | |  | | | |")
    print("                              |  < | . ` | / /\ \ \/ / |  __| | |  | | | |")
    print("                              | . \| |\  |/ ____ \  /  | |____| |__| |_| |")
    print("                              |_|\_\_| \_/_/    \_\/   |______|\____/|_____|")
    print("\n")
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    physique = "Physique: " + (PlayerIG.physique)
    face = "Face: " + (PlayerIG.face)
    skin = "Skin: " + (PlayerIG.skin)
    hair = "Hair: " + (PlayerIG.hair)
    clothing = "Clothing " + (PlayerIG.clothing)
    virtue = "Virtue: " + (PlayerIG.virtue)
    vice = "Vice: " + (PlayerIG.vice)
    speech = "Speech: " + (PlayerIG.speech)
    background = "Background: " + (PlayerIG.background)
    misfortune = "Misfortune: " + (PlayerIG.misfortune)
    alignment = "Alignment: " + (PlayerIG.alignment)
    features = "   TRAITS"
    print(statindicators.center(100, " ") + features.ljust(10, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " ") + physique.rjust(48, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " ") + face.rjust(48, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " ") + skin.rjust(48, " "))
    print(money.ljust(40, " ") + intline.center(20, " ") + hair.rjust(48, " "))
    print(food.ljust(40, " ") + wisline.center(20, " ") + clothing.rjust(48, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " ") + virtue.rjust(48, " "))
    print(vice.rjust(111, " "))
    print(speech.rjust(111, " "))
    print(background.rjust(111, " "))
    print(misfortune.rjust(111, " "))
    print(alignment.rjust(111, " "))
    print("\n")
    print(commandoptions1.center(100, " "))
    print(commandoptions2.center(100, " "))
    print(commandoptions3.center(100, " "))
    print(commandoptions4.center(100, " "))
    print(commandoptions5.center(100, " "))
    print(commandoptions6.center(100, " "))
    print(commandoptions7.center(100, " "))
    print(commandoptions8.center(100, " "))
    print(commandoptions9.center(100, " "))
    print("Select command option by selecting a number.")
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
        changeration()
    if option == "7":
        viewinventory()
    if option == "8":
        changeinventory()
    if option == "9":
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("\n Game has been saved! And so has your soul!\n")
            input("->")
            mainscreen()
    else:
        mainscreen()



def viewinventory():
    inventorydisplay = PlayerIG.inventory
    print("You open your bag and check your inventory. Press b to return.")
    print("Item is on the left column, number of Inventory Slots is on the right")
    print("\n")
    for key, value in inventorydisplay.items():
        print(key, " : ", value)
    option = input("->")
    if option.strip().lower() == "b":
        mainscreen()
    else:
        viewinventory()



def changeinventory():
    slotsremaining = PlayerIG.inventoryslots - sum(PlayerIG.inventory.values())
    inventorydisplay = PlayerIG.inventory
    print("Are you removing or adding something?")
    print("1.) Removing")
    print("2.) Adding")
    option = input("->")
    if option == "1":
        print("Item:           Slots")
        for key, value in inventorydisplay.items():
            print(key, " : ", value)
        print("Type the item you wish to remove.")
        option = input("->")
        if option in PlayerIG.inventory:
            PlayerIG.inventory.pop(option)
            print("Item Removed!")
            input("->")
        else:
            print("Item not in inventory, try again.")
            changeinventory()
    if option == "2":
        print("Item:           Slots")
        for key, value in inventorydisplay.items():
            print(key, " : ", value)
        print("Type the item you wish to add.")
        option = input("->")
        print("Type the number of slots it takes up.")
        option2 = input("->")
        if int(option2) > slotsremaining:
            print("Not enough space! Remove items and try again!")
        else:
            PlayerIG.inventory.update({str(option) : int(option2)})
            print("Item Added!")
            input("->")
            mainscreen()
    if option.strip().lower() == "b":
        mainscreen()
    else:
        changeinventory()






def changeration():
    print("What would you like to do? Press b to return")
    print("1.) Consume ration")
    print("2.) Add rations")
    option = input("->")
    if option.strip() == "1":
        PlayerIG.rations -= 1
        mainscreen()
    if option.strip() == "2":
        print("How many? Enter a number to continue.")
        option = input("->")
        if option.strip().lower() == "b":
            changeration()
        else:
            PlayerIG.rations += int(option)
            mainscreen()







def changestats():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Which stat would you like to change? Bonuses will automatically change. Press b to return")
    print("1.) Strength")
    print("2.) Dexterity")
    print("3.) Constitution")
    print("4.) Intelligence")
    print("5.) Wisdom")
    print("6.) Charisma")
    option = input("->")
    if option.strip() == "1":
        print("What is your new strength stat?")
        option2 = int(input("->"))
        PlayerIG.strength = option2
        PlayerIG.strbonus = PlayerIG.strength - 10
        mainscreen()
    if option.strip() == "2":
        print("What is your new dexterity stat?")
        option = int(input("->"))
        PlayerIG.dex = option
        PlayerIG.dexbonus = PlayerIG.dex - 10
        mainscreen()
    if option.strip() == "3":
        print("What is your new constitution stat?")
        option = int(input("->"))
        PlayerIG.con = option
        PlayerIG.conbonus = PlayerIG.con - 10
        mainscreen()
    if option.strip() == "4":
        print("What is your new intelligence stat?")
        option = int(input("->"))
        PlayerIG.intel = option
        PlayerIG.intelbonus = PlayerIG.intel - 10
        mainscreen()
    if option.strip() == "5":
        print("What is your new wisdom stat?")
        option = int(input("->"))
        PlayerIG.wis = option
        PlayerIG.wisbonus = PlayerIG.wis - 10
        mainscreen()
    if option.strip() == "6":
        print("What is your new charisma stat?")
        option = int(input("->"))
        PlayerIG.cha = option
        PlayerIG.chabonus = PlayerIG.cha - 10
        mainscreen()
    if option.strip().lower() == "b":
        mainscreen()
    else:
        print("Invalid response, try again.")
        changestats()



def changecopper():
    print("Increase or decreasing copper? Press b to return")
    print("1.) Increase")
    print("2.) Decrease")
    option = input("->")
    if option.strip() == "1":
        print("By how much?")
        option2 = int(input("->"))
        PlayerIG.copper = option2
        mainscreen()
    if option.strip() == "2":
        print("By how much?")
        option3 = int(input("->"))
        PlayerIG.copper = option3
        mainscreen()
    if option.lower().strip() == "b":
        mainscreen()
    else:
        print("Invalid choice, try again.")
        changecopper()




def changelevel():
    print("Level Up or Level Down? Press b to return")
    print("1.) Level Up")
    print("2.) Level Down")
    option = input("->")
    if option.strip() == "1":
        PlayerIG.level += 1
    if option.strip() == "2":
        PlayerIG.level -= 1
    if option.lower().strip() == "b":
        mainscreen()
    else:
        print("Invalid choice, try again.")
        changelevel()


def savegame():
    with open('savefile', 'wb') as f:
        pickle.dump(PlayerIG, f)
        print("\n Game has been saved! And so has your soul!\n")
        input("->")
        mainscreen()



def load():
    if os.path.exists("savefile") == True:
        with open("savefile", "rb") as f:
            global PlayerIG
            PlayerIG = pickle.load(f)
            print("Loaded save state...your journey continues!")
            input("->")
            mainscreen()


def changehp():
    print("Max HP or Current HP? Select b and enter to go back.")
    print("1.) Max HP")
    print("2.) Current HP")
    option1 = input("->")
    if option1.strip() == "1":
        print("What is your new max hp? (Enter a number)")
        option = int(input("->"))
        PlayerIG.maxhp = option
        print("Your new max HP has been saved!")
        mainscreen()
    if option1.strip() == "2":
        print("Increase or Decrease?")
        print("1.) Increase")
        print("2.) Decrease")
        option2 = input("->")
        if option2.strip() == "1":
            print("By how much? (Enter a number)")
            option3 = int(input("->"))
            PlayerIG.hp += option3
            print("Your HP has increased")
            input("->")
            mainscreen()
        if option2.strip() == "2":
            print("By how much? (Enter a number)")
            option4 = int(input("->"))
            PlayerIG.hp -= option4
            print("Your HP has decreased")
            input("->")
            mainscreen()
    if option1.strip().lower() == "b":
        mainscreen()
    else:
        print("Invalid option try again.")
        changehp()


def attack():
    start()

def start():
    print("Hello! Welcome to the KnaveUI dice roller! Which dice would you like to roll? (Press b to return)")
    print("1.) D4")
    print("2.) D6")
    print("3.) D8")
    print("4.) D10")
    print("5.) D12")
    print("6.) D20")
    print("7.) D100")
    option = input("-> ")
    if option.strip() == "1":
        dicerolld4()
    elif option.strip() == "2":
        dicerolld6()
    elif option.strip() == "3":
        dicerolld8()
    elif option.strip() == "4":
        dicerolld10()
    elif option.strip() == "5":
        dicerolld12()
    elif option.strip() == "6":
        dicerolld20()
    elif option.strip() == "7":
        dicerolld100()
    elif option.strip().lower() == "b":
        mainscreen()
    else:
        print("Invalid Option")
        start()


def dicerolld10():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d10 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 10))

    dicerolld10()


def dicerolld20():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d20 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 20))

    dicerolld20()


def dicerolld4():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d4 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 4))

    dicerolld4()


def dicerolld6():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d6 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 6))

    dicerolld6()


def dicerolld8():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d8 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 8))

    dicerolld8()


def dicerolld12():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d12 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 12))

    dicerolld12()



def dicerolld100():
    nameplate = "Name: " + PlayerIG.name
    hp = "HP: " + str(PlayerIG.hp) + "/" + str(PlayerIG.maxhp)
    plevel = "Level: " + str(PlayerIG.level)
    money = "Copper: " + str(PlayerIG.copper)
    food = "Rations: " + str(PlayerIG.rations)
    inventoryslots = "Inventory Slots: " + str(sum(PlayerIG.inventory.values())) + "/" + str(PlayerIG.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    strline = str(PlayerIG.strength) + "       " + " STR        " + str(PlayerIG.strbonus)
    dexline = str(PlayerIG.dex) + "       " + " DEX        " + str(PlayerIG.dexbonus)
    conline = str(PlayerIG.con) + "       " + " CON        " + str(PlayerIG.conbonus)
    intline = str(PlayerIG.intel) + "       " + " INT        " + str(PlayerIG.intelbonus)
    wisline = str(PlayerIG.wis) + "       " + " WIS        " + str(PlayerIG.wisbonus)
    chaline = str(PlayerIG.cha) + "       " + " CHA        " + str(PlayerIG.chabonus)
    print(statindicators.center(100, " "))
    print(nameplate.ljust(40, " ") + strline.center(20, " "))
    print(hp.ljust(40, " ") + dexline.center(20, " "))
    print(plevel.ljust(40, " ") + conline.center(20, " "))
    print(money.ljust(40, " ") + intline.center(20, " "))
    print(food.ljust(40, " ") + wisline.center(20, " "))
    print(inventoryslots.ljust(40, " ") + chaline.center(20, " "))
    print("Roll the d100 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option.strip() == "b":
        start()
    else:
        print(random.randint(1, 100))

    dicerolld100()

















def dead():
    print("You dead sucka! Time to roll up a new one! Click Enter to continue")
    input("->")




startmenu()
