import random
Slot1 = [
#player always goes in slot 1
#hp
"10",
#attack bonus
"0"
]
Slot2 = [
#other creatures go in slots 2+
#hp
"10",
#attack bonus
"3"
]
creaturesinroom = [
    "player",
    "jerry",

]
creaturesandslots = {
    "player":Slot1,
    "jerry":Slot2,

}
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
            print(("you pick up the "+x))
            weapon = x
        else:
            inven.append(x)
            print("that's not a weapon, but OK!")
    else:
        print("that's not in the room")
def attack(target):
    global placeholdervar
    global weapon
    global inven
    global incombat
    if target not in creaturesandslots:
        print("sorry, ",target," is not in the room.")
        return
    larry = creaturesandslots[target]
    jerry = larry[0]
    jerry = int(jerry)
    if weapon != "":
        larry = random.randint(1,itemsanddamage[weapon])
        jerry -= larry
        if jerry <= 0:
            pass
        else:
            print("jerry is mad you stabbed him for",larry,"damage")
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
    hmm()