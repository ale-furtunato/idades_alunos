import statistics

aluno = input("Deseja informar as idades dos alunos: ")
lista_idade_aluno = []

while aluno == "sim":
  contador = 1
  if contador < 26:
    idade_aluno = int(input("Qual a idade do aluno: "))
    lista_idade_aluno.append(idade_aluno)
    aluno = str(input("Deseja informar a idade do proximo aluno? "))
    contador += 1
  else:
    continue
  if aluno == "sim":
    continue
  elif aluno == "nao":
    maiores = [x for x in lista_idade_aluno if x >= 18]
    menores = [x for x in lista_idade_aluno if x < 18]
    
    print(f"\nO aluno mais novo tem {min(lista_idade_aluno)} anos.")
    print(f"O aluno mais velho tem {max(lista_idade_aluno)} anos.")
    print(f"Os alunos que tem mais de 18 anos sao: {maiores}")
    print(f"Os alunos que tem menos de 18 anos sao: {menores}")
    print(f"A media de idade entre os alunos é de {sum(lista_idade_aluno) / len(lista_idade_aluno):.2f}")
    print(f"A mediana é {statistics.median(lista_idade_aluno)}")
    
