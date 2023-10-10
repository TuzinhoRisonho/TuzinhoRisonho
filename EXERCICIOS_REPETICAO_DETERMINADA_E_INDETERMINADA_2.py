import random as r

generoList = ["A", "O", "X"]
salarioMed = 0
filhosHomem = 0
salarioMulher = 0
pessoasRica = 0
mulheresRica = 0

for i in range(50):
    genero = r.choice(generoList)
    salario = r.randint(1300, 40000)
    filhos = r.randint(0, 10)
    if salario > 15000:
        pessoasRica += 1
        if genero == "A":
            mulheresRica += 1
    if genero == "A":
        if salario > salarioMulher:
            salarioMulher = salario
    elif genero == "O":
        filhosHomem = (filhosHomem + filhos)/2
    salarioMed = (salarioMed + salario)/2
    
percentMulheresRicas = (mulheresRica * 100)/pessoasRica

print("Média salarial: {}".format(round(salarioMed,2)))
print("Número médio de filhos dos homens: {}".format(int(filhosHomem)))
print("Maior salário de uma mulher: {}".format(salarioMulher))
print("O percentual de mulheres entre as pessoas que ganham mais de R$ 15.000,00: {}".format(round(percentMulheresRicas,1)))
    
        