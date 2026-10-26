import random
import time
Slot1 = {
"hp":"10",
"attack bonus":"0",

}
Slot2 = {
"hp":"10",
"attack bonus":"3",
"weaponequipped":"claws"
}
creaturesinroom = [
    "player",
    "jerry",

]
creaturesandslots = {
    "player":Slot1,
    "jerry":Slot2,

}
PlayerSlot = Slot1
placeholdervar = ""
weapon = ""
berry = ""
first = ""
second = ""
secondpart = False
incombat = False
jerry = 10
itemsinroom = ["dagger","sword","banana"]
itemsanddamage ={
    "dagger":4,
    "sword":6,
}
itemsandweight = {
"banana":0.5,
"sword":2,
"dagger":1.5,
"apple":1,
}
inven = ["apple"]
def combat():
    print("wip")
def hello():
    print("hi!")
def goodbye():
    print("goodbye")
def take(x):
    if x in itemsinroom:
        global weapon
        if x in itemsanddamage:
            print("you pick up the "+x)
            inven.append(weapon)
            weapon = x
        else:
            inven.append(x)
            print("You pick up the"+x)
    else:
        print("I'm sorry, what?")
def attack(target):
    global placeholdervar
    global weapon
    global inven
    global incombat
    if target not in creaturesandslots:
        print("I'm sorry, what?")
        return
    barry = creaturesandslots[target]
    jerry = barry["hp"]
    jerry = int(jerry)
    if weapon != "":
        larry = random.randint(1,itemsanddamage[weapon])
        jerry -= larry
        if jerry <= 0:
            print(target,"is dead.")
            barry["hp"] = jerry
        else:
            barry["hp"] = jerry
            print(target,"is mad you hurt him for",larry,"damage")
            target["hostile"] = True
    else:
        global berry
        bag = ""
        berry = input("you're not holding a weapon, do you want to throw something from your backpack?(y/n)")
        if berry == "y" or berry == "Y" or berry == "yes" or berry == "Yes":
            for a in inven:
                bag = bag + ", " + a
            jeff = input("what do you want to throw?"+" inventory: "+bag+"    ")
            if jeff in inven:
                if random.randint(1,3) == 3:
                    jerry -= int(itemsandweight[jeff])
                    print("you hit him with the ",jeff,".")
                else:
                    print("your throw misses.")
                itemsinroom.append(jeff)
                inven.remove(jeff)
            else:
                print("you don't have that.")
        elif berry == "n" or berry == "N" or berry == "no" or berry == "No":
            print("OK, then...")
        else:
            print("What? Sorry, I had my beeswax in my ears.")
        if jerry <= 0:
            if (berry == "n" or berry == "N" or berry == "no" or berry == "No") == False:
                print("jerry is dead..")
            incombat = False
        barry["hp"] = jerry
    if incombat == True:
        combat()




func_map = {
    "hello",
    "goodbye",
    "attack",
    "take",
}
func_map_one_word = {
    "hello",
    "goodbye"
}
def hmm():
    global secondpart
    secondpart = False
    global first
    global second
    jeff = input()
    bob = jeff.split()
    for a in bob:
        if secondpart == False:
            if a in func_map:
                first = a
                if a in func_map_one_word:
                    first = first + "()"
                    eval(first)
                    first = ""
                else:
                    secondpart = True
        else:
            second = a
            hmm = first + "('" + second + "')"
            first = ""
            second = ""
            eval(hmm)
            secondpart = False
while True:
    if int(PlayerSlot["hp"]):
        if int(PlayerSlot["hp"]) >= 0:
            hmm()
            if int(PlayerSlot["hp"]) >= 0:
                if incombat == True:
                    print("you have",PlayerSlot["hp"],"hp left.")
            else:
                print("sorry, you died! you need to restart the game to play again.")