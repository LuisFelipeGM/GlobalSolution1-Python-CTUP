#    Global Solution dupla:
#RM: 94615  Nome: Daniel Henrique Alcântara Oliveira Martins
#RM: 94015  Nome: Luís Felipe Garcia Menezes

defeito = ["Falta de toner", "Necessita de limpeza", "Troca de cabo ou conector", "Quebrada ou inutilizada"]
maior = 0
impressoras = []
equipamento_analisado = 0
cont = 1
print(f" ..: Menu :.. \n 1. Falta de toner \n 2. Necessita de limpeza \n 3. Troca de cabo ou conector \n 4. Quebrada ou inutilizada \n 0. Exit \n")
while cont != 0:
    cont = int(input(f"Digite o problema da impressora {equipamento_analisado + 1}: "))
    if cont == 0 or cont == 1 or cont == 2 or cont == 3 or cont == 4:
        if cont == 0:
            break
        equipamento_analisado += 1
        if cont == 1:
            impressoras.append(defeito[0])
        if cont == 2:
            impressoras.append(defeito[1])
        if cont == 3:
            impressoras.append(defeito[2])
        if cont == 4:
            impressoras.append(defeito[3])
    else:
        print("Digite um valor válido")
    

print(f"\nQuantidade de equipamentos: {equipamento_analisado}")
print(f"Situação                        Quantidade              Percentual")
for i in range(len(defeito)):
    print(f"{defeito[i]}                    {impressoras.count(defeito[i])}                     {impressoras.count(defeito[i])/equipamento_analisado*100:.2f}%")
    if impressoras.count(defeito[i]) > maior:
        maior = impressoras.count(defeito[i])
        nome = defeito[i]
print(f"\n Maior ocorrência: {nome} - {maior}\n")
