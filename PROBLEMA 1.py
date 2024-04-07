# Início do código
periodo_de_vendas = True
total_de_ingressos = int(input("Quantos ingressos deseja vender para este evento\n"))
total_aux = total_de_ingressos
# Cortesia dos membros do DA
cortesia_da = int(input("São quantos membros do D.A.\n"))
# Cortesia para convidados
cortesia_convidados = int(input("Quantos convidados serão?\n"))
# Contador de ingressos totais
total_de_ingressos -= (cortesia_da + cortesia_convidados)
# Tipos de vendas
vendas_diretas = 0
vendas_bio_total = 0
vendas_enf_total = 0
# Tipos de ingressos
ingresso_inteira = 0
ingresso_meia = 0
ingressos_alunos_ecomp_total = 0
# Tipos de arrecadação
arrecadacao_total = 0
arrecadacao_inteira = 0
arrecadacao_meia = 0
arrecadacao_ecomp = 0
# Cortesias:
cortesia_comissionadas_total = 0
# Emissão
ingressos_emitidos = cortesia_da + cortesia_convidados
ingressos_nao_emitidos = 0
# Idades
idades = 0
# Quantidades
ingressos_meias_estudantes = 0
ingressos_meias_idosos = 0

while periodo_de_vendas and total_de_ingressos > 0:
    pergunta0 = int(input("Ainda está no período de vendas? 1 para SIM; 2 para NÃO\n"))
    if pergunta0 == 1:
        print("Há %d ingressos disponíveis\n" % total_de_ingressos)
        pergunta1 = int(input("A venda é comissionada? Digite 1 para SIM; 2, para NÃO\n"))
        if pergunta1 == 1:
            total_de_ingressos_aux = total_de_ingressos
            curso = int(input("O curso do vendedor é biologia ou enfermagem? Digite 1 para BIOLOGIA; 2, para ENFERMAGEM\n"))
            if curso == 1:
                ingressos_vendidos = int(input("Qual foi a quantidade de ingressos emitidos?\n"))
                while ingressos_vendidos > total_de_ingressos:
                    ingressos_vendidos = int(input("Digite um valor válido\n"))
                aux = 1
                venda_comissionada_bio = 0
                cortesia_comissionada_bio = 0
                ingresso_inteira_bio = 0
                ingresso_meia_bio = 0
                ingresso_alunos_ecomp_bio = 0
                while aux <= ingressos_vendidos:
                    print("Insira as informações do ingresso nº %d" % aux)
                    idade = int(input("Digite a idade do comprador\n"))
                    idades += idade
                    ingresso = int(input("Qual tipo de ingresso emitido? Digite 1 para inteira; 2, para meia; 3, para alunos de ECOMP\n"))
                    if ingresso == 1:
                        venda_comissionada_bio += 1
                        ingresso_inteira_bio += 1
                        ingressos_emitidos += 1
                        aux += 1
                        total_de_ingressos -= 1
                    elif ingresso == 2:
                        pergunta_meia = int(input("Digite 1 para meia para estudantes; 2, para idosos\n"))
                        venda_comissionada_bio += 1
                        ingresso_meia_bio += 1
                        ingressos_emitidos += 1
                        aux += 1
                        total_de_ingressos -= 1
                        while pergunta_meia != 1 and pergunta_meia != 2:
                            pergunta_meia = int(input("Digite 1 para meia para estudantes; 2, para idosos\n"))
                        if pergunta_meia == 1:
                            ingressos_meias_estudantes += 1
                        elif pergunta_meia == 2:
                            ingressos_meias_idosos += 1
                    elif ingresso == 3:
                        venda_comissionada_bio += 1
                        ingresso_alunos_ecomp_bio += 1
                        ingressos_emitidos += 1
                        aux += 1
                        total_de_ingressos -= 1
                    while ingresso != 1 and ingresso != 2 and ingresso != 3:
                        ingresso = int(input("Qual tipo de ingresso emitido? Digite 1 para inteira; 2, para meia; 3, para alunos de ECOMP\n"))
                # Vendas de biologia
                vendas_bio_total += ingressos_vendidos
                # Cálculo para inteira, meia e ecomp:
                ingresso_inteira += ingresso_inteira_bio
                ingresso_meia += ingresso_meia_bio
                ingressos_alunos_ecomp_total += ingresso_alunos_ecomp_bio
                # Cálculo da arrecadação da inteira, meia e computação:
                arrecadacao_inteira += ingresso_inteira_bio*30
                arrecadacao_meia += ingresso_meia_bio*15
                arrecadacao_ecomp += ingresso_alunos_ecomp_bio*10
                # Cálculo das cortesias
                cortesia_comissionada_bio = venda_comissionada_bio // 10
                if total_de_ingressos_aux >= venda_comissionada_bio:
                    diferenca = total_de_ingressos_aux - venda_comissionada_bio
                    if diferenca <= cortesia_comissionada_bio:
                        cortesia_comissionada_bio = diferenca
                        total_de_ingressos -= cortesia_comissionada_bio
                        ingressos_emitidos += cortesia_comissionada_bio
                        cortesia_comissionadas_total += cortesia_comissionada_bio
                    else:
                        total_de_ingressos -= cortesia_comissionada_bio
                        ingressos_emitidos += cortesia_comissionada_bio
                        cortesia_comissionadas_total += cortesia_comissionada_bio
            elif curso == 2:
                ingressos_vendidos = int(input("Qual foi a quantidade de ingressos emitidos?\n"))
                while ingressos_vendidos > total_de_ingressos:
                    ingressos_vendidos = int(input("Digite um valor válido\n"))
                aux = 1
                venda_comissionada_enf = 0
                cortesia_comissionada_enf = 0
                ingresso_inteira_enf = 0
                ingresso_meia_enf = 0
                ingresso_alunos_ecomp_enf = 0
                while aux <= ingressos_vendidos:
                    print("Insira as informações do ingresso nº %d" % aux)
                    idade = int(input("Digite a idade do comprador\n"))
                    idades += idade
                    ingresso = int(input("Qual tipo de ingresso foi emitido? Digite 1 para inteira; 2, para meia; 3, para alunos de ECOMP\n"))
                    if ingresso == 1:
                        venda_comissionada_enf += 1
                        ingresso_inteira_enf += 1
                        ingressos_emitidos += 1
                        aux += 1
                        total_de_ingressos -= 1
                    elif ingresso == 2:
                        pergunta_meia = int(input("Digite 1 para meia para estudantes; 2, para idosos\n"))
                        venda_comissionada_enf += 1
                        ingresso_meia_enf += 1
                        ingressos_emitidos += 1
                        aux += 1
                        total_de_ingressos -= 1
                        while pergunta_meia != 1 and pergunta_meia != 2:
                            pergunta_meia = int(input("Digite 1 para meia para estudantes; 2, para idosos\n"))
                        if pergunta_meia == 1:
                            ingressos_meias_estudantes += 1
                        elif pergunta_meia == 2:
                            ingressos_meias_idosos += 1
                    elif ingresso == 3:
                        venda_comissionada_enf += 1
                        ingresso_alunos_ecomp_enf += 1
                        ingressos_emitidos += 1
                        aux += 1
                        total_de_ingressos -= 1
                    while ingresso != 1 and ingresso != 2 and ingresso != 3:
                        ingresso = int(input("Qual tipo de ingresso emitido? Digite 1 para inteira; 2, para meia; 3, para alunos de ECOMP\n"))
                # vendas de enfermagem:
                vendas_enf_total += ingressos_vendidos
                # Cálculo para inteira, meia e ecomp:
                ingresso_inteira += ingresso_inteira_enf
                ingresso_meia += ingresso_meia_enf
                ingressos_alunos_ecomp_total += ingresso_alunos_ecomp_enf
                # Cálculo da arrecadação da inteira, meia e computação:
                arrecadacao_inteira += ingresso_inteira_enf*30
                arrecadacao_meia += ingresso_meia_enf*15
                arrecadacao_ecomp += ingresso_alunos_ecomp_enf*10
                # Cálculo das cortesias
                cortesia_comissionada_enf = venda_comissionada_enf // 10
                if total_de_ingressos_aux >= venda_comissionada_enf:
                    diferenca = total_de_ingressos_aux - venda_comissionada_enf
                    if diferenca <= cortesia_comissionada_enf:
                        cortesia_comissionada_enf = diferenca
                        total_de_ingressos -= cortesia_comissionada_enf
                        ingressos_emitidos += cortesia_comissionada_enf
                        cortesia_comissionadas_total += cortesia_comissionada_enf
                    else:
                        total_de_ingressos -= cortesia_comissionada_enf
                        ingressos_emitidos += cortesia_comissionada_enf
                        cortesia_comissionadas_total += cortesia_comissionada_enf
        elif pergunta1 == 2:
            ingressos_vendidos = int(input("Qual é a quantidade de ingressos a emitir?\n"))
            ingresso_inteira_direta = 0
            ingresso_meia_direta = 0
            ingresso_alunos_ecomp_direta = 0
            aux = 0
            while ingressos_vendidos > total_de_ingressos:
                ingressos_vendidos = int(input("Digite um valor válido\n"))
            while aux < ingressos_vendidos:
                print("Insira as informações do ingresso nº %d" % aux)
                idade = int(input("Digite a idade do comprador\n"))
                idades += idade
                ingresso = int(input("Qual tipo de ingresso foi vendido? Digite 1 para inteira; 2, para meia; 3, para alunos de ECOMP\n"))
                if ingresso == 1:
                    vendas_diretas += 1
                    ingressos_emitidos += 1
                    ingresso_inteira_direta += 1
                    total_de_ingressos -= 1
                    aux += 1
                elif ingresso == 2:
                    vendas_diretas += 1
                    pergunta_meia = int(input("Digite 1 para meia para estudantes; 2, para idosos\n"))
                    ingressos_emitidos += 1
                    ingresso_meia_direta += 1
                    total_de_ingressos -= 1
                    aux += 1
                    while pergunta_meia != 1 and pergunta_meia != 2:
                        pergunta_meia = int(input("Digite 1 para meia para estudantes; 2, para idosos\n"))
                    if pergunta_meia == 1:
                        ingressos_meias_estudantes += 1
                    elif pergunta_meia == 2:
                        ingressos_meias_idosos += 1
                elif ingresso == 3:
                    vendas_diretas += 1
                    ingressos_emitidos += 1
                    ingresso_alunos_ecomp_direta += 1
                    total_de_ingressos -= 1
                    aux += 1
                while ingresso != 1 and ingresso != 2 and ingresso != 3:
                    ingresso = int(input("Qual tipo de ingresso emitido? Digite 1 para inteira; 2, para meia; 3, para alunos de ECOMP\n"))
            # Cálculo para inteira, meia e ecomp:
            ingresso_inteira += ingresso_inteira_direta
            ingresso_meia += ingresso_meia_direta
            ingressos_alunos_ecomp_total += ingresso_alunos_ecomp_direta
            # Cálculo da arrecadação direta
            arrecadacao_inteira += ingresso_inteira_direta*30
            arrecadacao_meia += ingresso_meia_direta*15
            arrecadacao_ecomp += ingresso_alunos_ecomp_direta*10
    elif pergunta0 == 2:
        periodo_de_vendas = False
    else:
        pergunta0 = int(input("Ainda está no período de vendas? 1 para SIM; 2 para NÃO\n"))

if ingresso_inteira > ingresso_meia and ingresso_inteira > ingressos_alunos_ecomp_total:
    ingresso_aux = str("Ingresso do tipo INTEIRA\n")
    print(ingresso_aux)
elif ingresso_meia > ingresso_inteira and ingresso_meia > ingressos_alunos_ecomp_total:
    ingresso_aux = str("Ingresso do tipo MEIA\n")
    print(ingresso_aux)
elif ingressos_alunos_ecomp_total > ingresso_inteira and ingressos_alunos_ecomp_total > ingresso_meia:
    ingresso_aux = str("Ingresso do tipo ECOMP\n")
    print(ingresso_aux)
elif ingresso_inteira == ingresso_meia == ingressos_alunos_ecomp_total:
    ingresso_aux = str("Todos foram vendidos em igual quantidade\n")
    print(ingresso_aux)
elif ingresso_inteira == ingresso_meia or ingresso_inteira == ingressos_alunos_ecomp_total or ingresso_meia == ingressos_alunos_ecomp_total:
    if ingresso_inteira == ingresso_meia:
        ingresso_aux = str("Os tipos mais vendidos foram do tipo INTEIRA e MEIA\n")
        print(ingresso_aux)
    elif ingresso_inteira == ingressos_alunos_ecomp_total:
        ingresso_aux = str("Os tipos mais vendidos foram do tipo INTEIRA e ECOMP\n")
        print(ingresso_aux)
    elif ingresso_meia == ingressos_alunos_ecomp_total:
        ingresso_aux = str("Os tipos mais vendidos foram do tipo MEIA e ECOMP\n")
        print(ingresso_aux)
else:
    print("Não é possível dizer\n")

soma_auxiliar = cortesia_da + cortesia_convidados + cortesia_comissionadas_total
if ingressos_emitidos != 0:
    media = idades // (ingressos_emitidos - soma_auxiliar)
else:
    media = 0
ingressos_nao_emitidos = total_aux - ingressos_emitidos

print("%d ingressos emitidos\n" % ingressos_emitidos)
print("%d não foram emitidos\n" % ingressos_nao_emitidos)
print("%d ingressos de meia-entrada para estudantes foram emitidos\n" % ingressos_meias_estudantes)
print("%d ingressos de meia-entrada para idosos foram emitidos\n" % ingressos_meias_idosos)
print("%d ingressos de inteira foram emitidos\n" % ingresso_inteira)
print("%d ingressos emitidos para alunos de Ecomp\n" % ingressos_alunos_ecomp_total)
print("%d ingressos emitidos para o DA\n" % cortesia_da)
print("%d ingressos emitidos para os convidados\n" % cortesia_convidados)
print("%d ingressos de cortesia para vendedores comissionados\n" % cortesia_comissionadas_total)
print("%d ingressos foram vendidos por BIOLOGIA\n" % vendas_bio_total)
print("%d ingressos foram vendidos por ENFERMAGEM\n" % vendas_enf_total)
print("As vendas arrecadaram R$%.2f\n" % (arrecadacao_inteira + arrecadacao_meia + arrecadacao_ecomp))
print("As inteiras arrecadaram R$%.2f\n" % arrecadacao_inteira)
print("As meias-entradas arrecadaram R$%.2f\n" % arrecadacao_meia)
print("As entradas para alunos de ecomp arrecadaram R$%.2f\n" % arrecadacao_ecomp)
print("%s\n" % ingresso_aux)
print("%d\n é a média de idades\n" % media)
