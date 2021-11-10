from datetime import datetime

class Dish:
    Namn = ""
    Beskrivning=""
    AntalKalorier = 0
    Pris = 0
    LastModifed = None

def hej():
    print("111111")    
    print("111111234234234")    



def existInList(namn:str, dishes:list)->bool:
    for dish in dishes:
        if dish.Namn == namn:
            return True
    return False 

def createNew() -> Dish:
    dish = Dish()

    while True:
        dish.Namn = input("Maträttens namn:")
        if len(dish.Namn) > 0:
            break
    
    dish.Pris = int(input("Pris:"))
    dish.Beskrivning = input("Beskrivning:")
    dish.AntalKalorier = int(input("Kalorier:"))
    dish.LastModifed = datetime.now()
    return dish

def listAll(dishes:list):
    print("*** ALLA MATRÄTTER ***")
    for mat in dishes:
        print(f"{mat.Namn} {mat.Pris}kr Antal kalorier:{mat.AntalKalorier}") 





dishes = []
while True:
    print("1. Skapa maträtt")
    print("2. Lista alla")
    print("3. Ändra maträtt")
    print("4. Lista dagens meny")
    print("0. Avsluta")

    selection = input("Ange vad du vill göra:")

    if selection == "2":
        listAll(dishes)
    elif selection == "3":
        print("Ändra maträtt")
    elif selection == "4":
        print("Lista dagens meny")
    elif selection == "0":
        print("Avslutar. Ha en bra dag")
        break
    elif selection == "1":
        dish = createNew()

        if existInList(dish.Namn,dishes) :
            print("Finns redan")                
        else:
            dishes.append(dish)