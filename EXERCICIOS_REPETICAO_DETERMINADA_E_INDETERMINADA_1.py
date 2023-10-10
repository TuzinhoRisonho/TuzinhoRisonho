import random as r

maxList = []
minList = []
medList = []
atipicoList = []
medMax = 0
medMin = 0
medMed = 0

def atipico(temp):
    if temp < 15 or temp > 38:
        return True
    else:
        return False

for i in range(30):
    temp1 = r.randint(-10, 45)
    temp2 = r.randint(-10, 45)
    if temp1 < temp2:
        minTemp = temp1
        maxTemp = temp2
    else:
        minTemp = temp2
        maxTemp = temp1
    minList.append(minTemp)
    maxList.append(maxTemp)
    media = (minTemp + maxTemp)/2
    medList.append(media)
    if atipico(media) == True:
        atipicoList.append(i+1)
    
        
    

for i in range(30):
    print("Dia {}: Temperatura Média = {}".format((i+1), medList[i]))
    medMax = (medMax + maxList[i])/2
    medMin = (medMin + minList[i])/2

percAtipico = (len(atipicoList) * 100)/30
print("MÉDIA TEMPERATURAS MINIMAS = {}".format(round(medMin, 1)))
print("MÉDIA TEMPERATURAS MÁXIMAS = {}".format(round(medMax, 1)))
print("PORCENTAGEM DE DIAS ATÍPICOS = {}%".format(round(percAtipico, 1)))
print(atipicoList)

