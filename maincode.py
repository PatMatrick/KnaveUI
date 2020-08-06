import math
import random
import os
import pickle


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
    print(" _  ___   _     __      ________ _    _ _____")
    print("| |/ / \ | |   /\ \    / /  ____| |  | |_   _|")
    print("| ' /|  \| |  /  \ \  / /| |__  | |  | | | |")
    print("|  < | . ` | / /\ \ \/ / |  __| | |  | | | |")
    print("| . \| |\  |/ ____ \  /  | |____| |__| |_| |")
    print("|_|\_\_| \_/_/    \_\/   |______|\____/|_____|")
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
    Player.speech = input("->")
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
    os.system('cls')
    if Player.hp <= 0:
        dead()
    if Player.hp > Player.maxhp:
        Player.hp = Player.maxhp
    nameplate = "Name: " + Player.name
    hp = "HP: " + str(Player.hp) + "/" + str(Player.maxhp)
    plevel = "Level: " + str(Player.level)
    money = "Copper: " + str(Player.copper)
    food = "Rations: " + str(Player.rations)
    inventoryslots = "Inventory Slots: " + str(Player.currentinventory) + "/" + str(Player.inventoryslots)
    statindicators = "  DEFENSE    ABILITY    BONUS"
    commandoptions1 = "1.) Dice Roller and Attack"
    commandoptions2 = "2.) Change HP"
    commandoptions3 = "3.) Change Level"
    commandoptions4 = "4.) Change Copper Amount"
    commandoptions5 = "5.) Change Stats"
    commandoptions6 = "6.) Consume Ration"
    commandoptions7 = "7.) View Inventory"
    commandoptions8 = "8.) Change Inventory"
    commandoptions9 = "9.) Save Current State"
    print(" _  ___   _     __      ________ _    _ _____")
    print("| |/ / \ | |   /\ \    / /  ____| |  | |_   _|")
    print("| ' /|  \| |  /  \ \  / /| |__  | |  | | | |")
    print("|  < | . ` | / /\ \ \/ / |  __| | |  | | | |")
    print("| . \| |\  |/ ____ \  /  | |____| |__| |_| |")
    print("|_|\_\_| \_/_/    \_\/   |______|\____/|_____|")
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
    print(commandoptions1.center(40, " "))
    print(commandoptions2.center(40, " "))
    print(commandoptions3.center(40, " "))
    print(commandoptions4.center(40, " "))
    print(commandoptions5.center(40, " "))
    print(commandoptions6.center(40, " "))
    print(commandoptions7.center(40, " "))
    print(commandoptions8.center(40, " "))
    print(commandoptions9.center(40, " "))
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
        consumeration()
    if option == "7":
        viewinventory()
    if option == "8":
        changeinventory()
    if option == "9":
        savegame()
    else:
        mainscreen()




def savegame():
    if os.path.exists("savefile") == True:
        os.system('cls')
        with open("savefile", "rb") as f:
            global Player
            Player = pickle.load(f)
        print("Loaded save state...your journey onto perfection continues!")
        option = input("->")
        mainscreen()


def changehp():
    print("Max HP or Current HP? Select b and enter to go back.")
    print("1.) Max HP")
    print("2.) Current HP")
    option1 = input("->")
    if option1.strip() == "1":
        print("What is your new max hp? (Enter a number)")
        option = int(input("->"))
        Player.maxhp = option
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
            Player.hp += option3
            print("Your HP has increased")
            input("->")
            mainscreen()
        if option2.strip() == "2":
            print("By how much? (Enter a number)")
            option4 = int(input("->"))
            Player.hp -= option4
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
    if option == "1":
        dicerolld4()
    elif option == "2":
        dicerolld6()
    elif option == "3":
        dicerolld8()
    elif option == "4":
        dicerolld10()
    elif option == "5":
        dicerolld12()
    elif option == "6":
        dicerolld20()
    elif option == "7":
        dicerolld100()
    elif option.strip().lower() == "b":
        mainscreen()
    else:
        print("Invalid Option")
        start()


def dicerolld10():
    print("Roll the d10 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option == "b":
        start()
    else:
        print(random.randint(1, 10))

    dicerolld10()


def dicerolld20():
    print("Roll the d20 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option == "b":
        start()
    else:
        print(random.randint(1, 20))

    dicerolld20()


def dicerolld4():
    print("Roll the d4 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option == "b":
        start()
    else:
        print(random.randint(1, 4))

    dicerolld4()


def dicerolld6():
    print("Roll the d6 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option == "b":
        start()
    else:
        print(random.randint(1, 6))

    dicerolld6()


def dicerolld8():
    print("Roll the d8 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option == "b":
        start()
    else:
        print(random.randint(1, 8))

    dicerolld8()


def dicerolld12():
    print("Roll the d12 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option == "b":
        start()
    else:
        print(random.randint(1, 12))

    dicerolld12()



def dicerolld100():
    print("Roll the d100 dice! Click Enter! Click b to return")
    option = input("-> ")
    if option == "b":
        start()
    else:
        print(random.randint(1, 100))

    dicerolld100()

















def dead():
    print("You dead sucka! Time to roll up a new one! Click Enter to continue")
    input("->")




startmenu()
