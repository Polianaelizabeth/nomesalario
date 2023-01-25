meses = int(1)
caderneta = float(1.02)
rendafixa = 1.05

salCarlos = float(input("Salário de Carlos"))
salJoao = salCarlos/3

valorJ = salJoao*rendafixa
valorC = salCarlos*caderneta

while valorJ < valorC:
    meses += 1

    valorJ = valorJ*rendafixa
    valorC = valorC*caderneta

print("O valor de João igualou ou ultrapassou de Carlos em ", meses, "meses. João tendo ", valorJ,
      " reais, e Carlos ", valorC)