cabeloList = []
generoList = []
idadeList = []
alturaList = []
idadeRuiva = 0
totalLoiro = 0
homemLoiro = 0
alunoVelhoAlto = 0
alturaMaisVelho = 0

while True:
    cabeloCor = input("Insira a cor do cabelo do aluno (P-preto, L-louro, C-castanho, R-ruivo, D-demais cores ou F-TÉRMINO DA ENTRADA DE DADOS): ")
    if cabeloCor == "F" or cabeloCor == "f":
        break
    genero = input("Insira o gênero do aluno (A- feminino, O-masculino, X- não deseja responder): ")
    idade = int(input("Insira a idade do aluno: "))
    altura = float(input("Insira a altura do aluno: "))
    cabeloList.append(cabeloCor)
    generoList.append(genero)
    idadeList.append(idade)
    alturaList.append(altura)
    if cabeloCor == "L":
        totalLoiro += 1
        if genero == "O":
            homemLoiro += 1
    elif cabeloCor == "R":
        idadeRuiva = (idadeRuiva + idade)/2
    if idade > 10 and altura > 1.8:
        alunoVelhoAlto += 1
    if idade > idadeList[(len(idadeList) - 1)]:
        alturaMaisVelho = altura

percentHomemLouro = (homemLoiro * 100)/totalLoiro

print("A média de idade das mulheres : {}".format(int(idadeRuiva)))
print("O percentual de homens dentre as pessoas de cabelo louro: {}".format(round(percentHomemLouro, 2)))
print("A quantidade de alunos da escola com mais de 10 anos e altura superior a 1.80m: {}".format(alunoVelhorAlto))
print("A altura da pessoa mais velha: {}".format(alturaMaisVelho))


        