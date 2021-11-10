from colorama import init, Fore, Back, Style
init()

print(Fore.RED + "some red text")
print(Back.GREEN + "some green text")



print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')


x = 12
y = int(input("Ange tal:"))
z = x * y
print(z)


def test():
    print("asdaasd")
    print("sdfsdf")


a = test()


def calculateArea(width: float,height: float) -> float:
    return width * height

def canIBuyBeer(age:int,location:str) -> bool:
    if age > 17 and location == "K":
        return True
    elif age > 19 and location == "S":
        return True
    elif location == "Kompis" or location == "Fiket" or location == "Hemma":
        return True
    else:
        return False

area = calculateArea(2.2, 3.3)

while True:
    age = int(input("Hur gammal är du?"))
    location = input("Var är du?")
    if canIBuyBeer(age,location) == True:
        print("Ja du får köpa öl")
    else:
        print("Nej du får INTE köpa öl")
    #canIBuyBeer(age,location)
    cont = input("Vill du fortsätta?")
    if cont == "N":
        break


# Bank system i sin enklaste form
# koppling MAPPNING mellan kontonummer och saldo

accounts = {}

accounts["52570012345"] = 28
accounts["5212121212"] = 1588







spelare = []

stefansBarn = ["Fanny", "Josefine", "Oliver"]
# meny 1 Skapa nytt barn
stefansBarn.append("HJkh")
for namn in stefansBarn:
    print(namn)
    

    #
    #
    #
    # avsluta med break



