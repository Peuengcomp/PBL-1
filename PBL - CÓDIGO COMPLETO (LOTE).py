# Declaração de variável booleana para período de vendas
periodo_de_venda = True
# Declaração de variáveis de entrada referentes ao total de ingressos e preços
total_de_ingressos = int(input("Digite a quantidade de ingressos disponíveis\n"))
preco_inteira = float(input("Digite o preço do ingresso do tipo INTEIRA\n"))
preco_meia = float(input("Digite o preço do ingresso do tipo MEIA\n"))
preco_ecomp = float(input("Digite o preço do ingresso do tipo ALUNOS DE ECOMP\n"))
# Declaração de variável auxiliar da quantidade de ingressos para cálculos
aux_total_ingressos = total_de_ingressos
# Entrada para quantidade de ingressos do D.A. e CONVIDADOS
cortesia_da = int(input("São quantos membros do D.A.\n"))
cortesia_convidados = int(input("Quantos convidados serão?\n"))
# Contador de ingressos totais, para evitar que haja excedente de ingressos em relação aos ingressos fornecidos para o D.A. e CONVIDADOS
soma_auxiliar = cortesia_da + cortesia_convidados
if aux_total_ingressos >= soma_auxiliar:
    total_de_ingressos -= soma_auxiliar
else:
    while aux_total_ingressos < soma_auxiliar:
        cortesia_da = 0
        cortesia_convidados = 0
        print("Há %d ingressos disponíveis\n" % aux_total_ingressos)
        print("Digite a quantidade de cortesias que não ultrapasse a quantidade de ingressos disponível\n")
        cortesia_da = int(input("São quantos membros do D.A.\n"))
        cortesia_convidados = int(input("Quantos convidados serão?\n"))
        soma_auxiliar = cortesia_da + cortesia_convidados
    total_de_ingressos -= soma_auxiliar
# Contadores dos canais de venda, que vão calcular as vendas em função respectivos canais de venda, direta ou comissionada
vendas_diretas = 0
vendas_bio_total = 0
vendas_enf_total = 0
# Contadores dos tipos de ingressos, que vão acumular a quantidade de ingressos em função de seus tipos
ingresso_inteira = 0
ingresso_meia = 0
ingresso_ecomp = 0
# Contadores de ingressos do tipo meia por critérios de idade e estudante
meia_estudante_total = 0
meia_idoso_total = 0
# Contadores de arrecadação, que vão calcular a arrecandação total e por tipo de ingresso
arrecadacao_total = 0
arrecadacao_inteira = 0
arrecadacao_meia = 0
arrecadacao_ecomp = 0
# Contador de comissão, que vai acumular a comissão total
comissao_total = 0
# Contadores de emissão de ingressos, incluindo o já emitidos para o D.A.
ingressos_emitidos = cortesia_da + cortesia_convidados
ingressos_nao_emitidos = 0
# Contador de idade, que vai acumular as cidades
idade_total = 0
# Loop que vai ser executado conforme ainda haja disponibilidade de ingresso e dentro do período de vendas
while periodo_de_venda and total_de_ingressos > 0:
    print("Há %d ingressos disponíveis\n" % total_de_ingressos)
    pergunta0 = int(input("Ainda está no período de vendas? 1 para SIM; 2 para NÃO\n"))
    if pergunta0 == 1:
        # Esta célula pergunta se a venda é comissionada ou não
        pergunta1 = int(input("A venda é comissionada? Digite 1 para SIM; 2, para NÃO\n"))
        # Esta se refere ao tipo de venda comissionada
        if pergunta1 == 1:
            # Variável utilizada para realizar cálculos referente à comissão
            total_de_ingressos_aux = total_de_ingressos
            # Questiona o curso
            curso = int(input("O curso do vendedor é biologia ou enfermagem? Digite 1 para BIOLOGIA; 2, para ENFERMAGEM\n"))
            # Esta célula contabiliza as vendas do curso de BIOLOGIA
            if curso == 1:
                total_aux = 0
                quantidade_vendida = int(input("Digite a quantidade de ingressos vendidos\n"))
                while quantidade_vendida > total_de_ingressos:
                    quantidade_vendida = int(input("Digite uma quantidade igual ou menor de ingressos disponíveis\n"))
                while total_aux != quantidade_vendida:
                    print("Digite as quantidades cuja soma seja equivalente à quantidade vendida\n")
                    # Ceĺula referente ao cálculo da quantidade de ingressos e idades para INTEIRAS
                    ingresso_inteira_bio = int(input("Quantas INTEIRAS foram vendidas?\n"))
                    if ingresso_inteira_bio != 0:
                        idade_inteira = int(input("Digite a soma das idades\n"))
                    else:
                        idade_inteira = 0
                    # Célula referente ao cálculo da quantidade de ingressos e idades para MEIAS
                    ingresso_meia_bio = int(input("Quantas MEIAS foram vendidas?\n"))
                    if ingresso_meia_bio != 0:
                        idade_meia = int(input("Digite a soma das idades\n"))
                        meia_estudante = int(input("Quantos ingressos para estudantes?\n"))
                        meia_idoso = int(input("Quantos ingressos para idosos?\n"))
                        while meia_estudante + meia_idoso != ingresso_meia_bio:
                            print("Digite a quantidade para cada tipo de meia equivalente à quantidade vendida\n")
                            meia_estudante = int(input("Quantos ingressos para estudantes?\n"))
                            meia_idoso = int(input("Quantos ingressos para idosos?\n"))
                    else:
                        meia_estudante = meia_idoso = idade_meia = 0
                    # Célula referente ao cálculo da quantidade de ingressos e idade para alunos de ECOMP
                    ingresso_ecomp_bio = int(input("Quantos ingressos para ALUNOS DE ECOMP?\n"))
                    if ingresso_ecomp_bio != 0:
                        idade_ecomp = int(input("Digite a soma das idades\n"))
                    else:
                        idade_ecomp = 0
                    total_aux = ingresso_inteira_bio + ingresso_meia_bio + ingresso_ecomp_bio
                # Desconta do total de ingressos disponíveis
                total_de_ingressos -= total_aux
                # Adiciona ao contador principal da idade a soma das idades contabilizadas
                idade_total += idade_inteira + idade_meia + idade_ecomp
                # Quantifica e adiciona ao contador de ingressos emitidos ao total e às vendas de biologia
                ingressos_emitidos += total_aux
                vendas_bio_total += total_aux
                # Quantifica e adiciona aos contadores de ingresso por tipo
                ingresso_inteira += ingresso_inteira_bio
                ingresso_meia += ingresso_meia_bio
                ingresso_ecomp += ingresso_ecomp_bio
                # Quantificação por tipo de meia
                meia_estudante_total += meia_estudante
                meia_idoso_total += meia_idoso
                # Cálculo referente à arrecadação
                arrecadacao_inteira += ingresso_inteira_bio*preco_inteira
                arrecadacao_meia += ingresso_meia_bio*preco_meia
                arrecadacao_ecomp += ingresso_ecomp_bio*preco_ecomp
                # Ceĺula que calcula a comissão da venda em função da diferença, ou seja, o vendedor só recebe a comissão se houver disponibilidade
                comissao_bio = total_aux // 10
                diferenca = total_de_ingressos_aux - total_aux
                if diferenca <= comissao_bio:
                    comissao_bio = diferenca
                    total_de_ingressos -= comissao_bio
                    ingressos_emitidos += comissao_bio
                    comissao_total += comissao_bio
                else:
                    total_de_ingressos -= comissao_bio
                    ingressos_emitidos += comissao_bio
                    comissao_total += comissao_bio
                # Fim da contabilização para o curso de BIOLOGIA
            
            elif curso == 2:
                total_aux = 0
                quantidade_vendida = int(input("Digite a quantidade de ingressos vendidos\n"))
                while quantidade_vendida > total_de_ingressos:
                    quantidade_vendida = int(input("Digite uma quantidade igual ou menor de ingressos disponíveis\n"))
                while total_aux != quantidade_vendida:
                    print("Digite as quantidades cuja soma seja equivalente à quantidade vendida\n")
                    # Ceĺula referente ao cálculo da quantidade de ingressos e idades para INTEIRAS
                    ingresso_inteira_enf = int(input("Quantas INTEIRAS foram vendidas?\n"))
                    if ingresso_inteira_enf != 0:
                        idade_inteira = int(input("Digite a soma das idades\n"))
                    else:
                        idade_inteira = 0
                    # Célula referente ao cálculo da quantidade de ingressos e idades para MEIAS
                    ingresso_meia_enf = int(input("Quantas MEIAS foram vendidas?\n"))
                    if ingresso_meia_enf != 0:
                        idade_meia = int(input("Digite a soma das idades\n"))
                        meia_estudante = int(input("Quantos ingressos para estudantes?\n"))
                        meia_idoso = int(input("Quantos ingressos para idosos?\n"))
                        while meia_estudante + meia_idoso != ingresso_meia_enf:
                            print("Digite uma quantidade válida\n")
                            meia_estudante = int(input("Quantos ingressos para estudantes?\n"))
                            meia_idoso = int(input("Quantos ingressos para idosos?\n"))
                    else:
                        meia_estudante = meia_idoso = idade_meia = 0
                    # Célula referente ao cálculo da quantidade de ingressos e idade para alunos de ECOMP
                    ingresso_ecomp_enf = int(input("Quantos ingressos para ALUNOS DE ECOMP?\n"))
                    if ingresso_ecomp_enf != 0:
                        idade_ecomp = int(input("Digite a soma das idades\n"))
                    else:
                        idade_ecomp = 0
                    total_aux = ingresso_inteira_enf + ingresso_meia_enf + ingresso_ecomp_enf
                # Desconta do total de ingressos disponíveis
                total_de_ingressos -= total_aux
                # Adiciona ao contador principal da idade a soma das idades contabilizadas
                idade_total += idade_inteira + idade_meia + idade_ecomp
                # Quantifica e adiciona ao contador de ingressos emitidos ao total e às vendas de ENFERMAGEM
                ingressos_emitidos += total_aux
                vendas_enf_total += total_aux
                # Quantifica e adiciona aos contadores de ingresso por tipo
                ingresso_inteira += ingresso_inteira_enf
                ingresso_meia += ingresso_meia_enf
                ingresso_ecomp += ingresso_ecomp_enf
                # Quantificação por tipo de meia
                meia_estudante_total += meia_estudante
                meia_idoso_total += meia_idoso
                # Cálculo referente à arrecadação
                arrecadacao_inteira += ingresso_inteira_enf*preco_inteira
                arrecadacao_meia += ingresso_meia_enf*preco_meia
                arrecadacao_ecomp += ingresso_ecomp_enf*preco_ecomp
                # Ceĺula que calcula a comissão da venda em função da diferença, ou seja, o vendedor só recebe a comissão se houver disponibilidade
                comissao_enf = total_aux // 10
                diferenca = total_de_ingressos_aux - total_aux
                if diferenca <= comissao_enf:
                    comissao_enf = diferenca
                    total_de_ingressos -= comissao_enf
                    ingressos_emitidos += comissao_enf
                    comissao_total += comissao_enf
                else:
                    total_de_ingressos -= comissao_enf
                    ingressos_emitidos += comissao_enf
                    comissao_total += comissao_enf
                # Fim da contabilização para o curso de ENFERMAGEM
        
        # Célula para cálculo de venda direta
        elif pergunta1 == 2:
            total_aux = 0
            quantidade_vendida = int(input("Digite a quantidade de ingressos vendidos\n"))
            while quantidade_vendida > total_de_ingressos:
                quantidade_vendida = int(input("Digite uma quantidade igual ou menor de ingressos disponíveis\n"))
            while total_aux != quantidade_vendida:
                print("Digite as quantidades cuja soma seja equivalente à quantidade vendida\n")
                # Ceĺula referente ao cálculo da quantidade de ingressos e idades para INTEIRAS
                ingresso_inteira_direta = int(input("Quantas INTEIRAS foram vendidas?\n"))
                if ingresso_inteira_direta != 0:
                    idade_inteira = int(input("Digite a soma das idades\n"))
                else:
                    idade_inteira = 0
                # Célula referente ao cálculo da quantidade de ingressos e idades para MEIAS
                ingresso_meia_direta = int(input("Quantas MEIAS foram vendidas?\n"))
                if ingresso_meia_direta != 0:
                    idade_meia = int(input("Digite a soma das idades\n"))
                    meia_estudante = int(input("Quantos ingressos para estudantes?\n"))
                    meia_idoso = int(input("Quantos ingressos para idosos?\n"))
                    while meia_estudante + meia_idoso != ingresso_meia_direta:
                        print("Digite uma quantidade válida\n")
                        meia_estudante = int(input("Quantos ingressos para estudantes?\n"))
                        meia_idoso = int(input("Quantos ingressos para idosos?\n"))
                else:
                    meia_estudante = meia_idoso = idade_meia = 0
                # Célula referente ao cálculo da quantidade de ingressos e idade para alunos de ECOMP
                ingresso_ecomp_direta = int(input("Quantos ingressos para ALUNOS DE ECOMP?\n"))
                if ingresso_ecomp_direta != 0:
                    idade_ecomp = int(input("Digite a soma das idades\n"))
                else:
                    idade_ecomp = 0
                total_aux += ingresso_inteira_direta + ingresso_meia_direta + ingresso_ecomp_direta
            # Desconta do total de ingressos disponíveis
            total_de_ingressos -= total_aux
            # Adiciona ao contador principal da idade a soma das idades contabilizadas
            idade_total += idade_inteira + idade_meia + idade_ecomp
            # Quantifica e adiciona ao contador de ingressos emitidos ao total e às vendas de ENFERMAGEM
            ingressos_emitidos += total_aux
            vendas_diretas += total_aux
            # Quantifica e adiciona aos contadores de ingresso por tipo
            ingresso_inteira += ingresso_inteira_direta
            ingresso_meia += ingresso_meia_direta
            ingresso_ecomp += ingresso_ecomp_direta
            # Quantificação por tipo de meia
            meia_estudante_total += meia_estudante
            meia_idoso_total += meia_idoso
            # Cálculo referente à arrecadação
            arrecadacao_inteira += ingresso_inteira_direta*preco_inteira
            arrecadacao_meia += ingresso_meia_direta*preco_meia
            arrecadacao_ecomp += ingresso_ecomp_direta*preco_ecomp
        # célula que mantém a estrutura de repetição caso haja erro de digitação
        else:
            pergunta1 = int(input("A venda é comissionada? Digite 1 para SIM; 2, para NÃO\n"))
    # Caso acabe o período de vendas, imprime o resultado do relatório
    elif pergunta0 == 2:
        periodo_de_venda = False
    # célula que mantém a estrutura de repetição caso haja erro de digitação   
    else:
        pergunta0 = int(input("Ainda está no período de vendas? 1 para SIM; 2 para NÃO\n"))

# Esta célula calcula quais tipos de ingressos venderam mais ou não venderam nenhum
if ingresso_inteira > ingresso_meia and ingresso_inteira > ingresso_ecomp:
    ingresso_aux = str("Ingresso do tipo INTEIRA\n")
elif ingresso_meia > ingresso_inteira and ingresso_meia > ingresso_ecomp:
    ingresso_aux = str("Ingresso do tipo MEIA\n")
elif ingresso_ecomp > ingresso_inteira and ingresso_ecomp > ingresso_meia:
    ingresso_aux = str("Ingresso do tipo ECOMP\n")
elif ingresso_inteira == ingresso_meia == ingresso_ecomp:
    if aux_total_ingressos == cortesia_da + cortesia_convidados or (ingresso_inteira == ingresso_meia == ingresso_ecomp == 0):
        ingresso_aux = str("Nenhum ingresso foi vendido\n")
    else:
        ingresso_aux = str("Todos foram vendidos em igual quantidade\n")
elif ingresso_inteira == ingresso_meia or ingresso_inteira == ingresso_ecomp or ingresso_meia == ingresso_ecomp:
    if ingresso_inteira == ingresso_meia:
        ingresso_aux = str("Os tipos mais vendidos foram do tipo INTEIRA e MEIA\n")
    elif ingresso_inteira == ingresso_ecomp:
        ingresso_aux = str("Os tipos mais vendidos foram do tipo INTEIRA e ECOMP\n")
    elif ingresso_meia == ingresso_ecomp:
        ingresso_aux = str("Os tipos mais vendidos foram do tipo MEIA e ECOMP\n")
# Esta célula utiliza uma variável que acumula as cortesias e as comissões e subtrai da quantidade de ingressos emitidos para calcular a média de idade
soma_auxiliar += comissao_total
if ingressos_emitidos != 0:
    if ingressos_emitidos == soma_auxiliar:
        media = 0
    else:
        media = idade_total // (ingressos_emitidos - soma_auxiliar)
else:
    media = 0
# Esta célula calcula a quantidade de ingressos não emitidos
ingressos_nao_emitidos = aux_total_ingressos - ingressos_emitidos
# Esta célula printa todos os valores no relatório
print("%d ingressos emitidos\n" % ingressos_emitidos)
print("%d não foram emitidos\n" % ingressos_nao_emitidos)
print("%d ingressos do TIPO INTEIRA foram emitidos\n" % ingresso_inteira)
print("%d ingressos do TIPO MEIA para ESTUDANTES foram emitidos\n" % meia_estudante_total)
print("%d ingressos do TIPO MEIA para IDOSOS foram emitidos\n" % meia_idoso_total)
print("%d ingressos emitidos para alunos de Ecomp\n" % ingresso_ecomp)
print("%d ingressos emitidos para o DA\n" % cortesia_da)
print("%d ingressos emitidos para os convidados\n" % cortesia_convidados)
print("%d ingressos de comissão para vendedores comissionados\n" % comissao_total)
print("%d ingressos foram vendidos por BIOLOGIA\n" % vendas_bio_total)
print("%d ingressos foram vendidos por ENFERMAGEM\n" % vendas_enf_total)
print("As vendas arrecadaram R$%.2f\n" % (arrecadacao_inteira + arrecadacao_meia + arrecadacao_ecomp))
print("As inteiras arrecadaram R$%.2f\n" % arrecadacao_inteira)
print("As meias-entradas arrecadaram R$%.2f\n" % arrecadacao_meia)
print("As entradas para alunos de ecomp arrecadaram R$%.2f\n" % arrecadacao_ecomp)
print("%s" % ingresso_aux)
print("%d é a média de idades em anos\n" % media)
