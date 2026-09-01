import random
weapon = ""
berry = ""
first = ""
second = ""
secondpart = False
jerry = 10
itemsinroom = ["dagger","sword","banana"]
itemsanddamage ={
    "dagger":4,
    "sword":6,

}
inven = ["apple"]
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
def attack():
    global jerry
    global weapon
    global inven
    if weapon != "":
        larry = random.randint(1,itemsanddamage[weapon])
        jerry -= larry
        if jerry <= 0:
            print("jerry is dead.")
        else:
            print("jerry is mad you stabbed him for",larry,"damage")
    else:
        global berry
        bag = ""
        berry = input("you're not holding a weapon, do you want to throw something from your backpack?(y/n)")
        if berry == "y" or berry == "Y" or berry == "yes" or berry == "Yes":
            first = True
            for a in inven:
                if first == True:
                    bag = bag + a
                    first = False
                bag = bag + ", " + a
            jeff = input("what do you want to throw?"+" inventory: "+bag)
            if jeff in inven:
                inven.remove(jeff)
                itemsinroom.append(jeff)
        elif berry == "n" or berry == "N" or berry == "no" or berry == "No":
            print("OK, then...")
        else:
            print("What? Sorry, I had my beeswax in my ears.")




func_map = {
    "hello",
    "goodbye",
    "attack",
    "take",
}
func_map_one_word = {
    "attack",
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