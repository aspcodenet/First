def getTotalLength(listan:list)->int:
    sum = 0
    for one in listan:
        sum = sum + len(one)
    return sum

listan = ["Stockholm", "Sundsvall", "Göteborg"]
summan = getTotalLength(listan)

def getLargestIn(allaTal:list)->int:
    largest = None
    for tal in allaTal:
        if largest == None or tal > largest:
            largest = tal
    return largest

listan = [12,11,1234,35,45]	
tal = getLargestIn(listan)


def calclatePoints(lista:list)->float:
    summa = 0
    for point in lista:
        summa = summa + point
    

listan = [9,4,6,7,6]	
points = calculatePoints(listan)

