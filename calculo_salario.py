#CALCULO DE SALARIO BRUTO E LIQUIDO

#REQUERIMENTO
"""
1) Crie um programa que receba o salário bruto, calcule a gratificação (5% do salário), calcule o imposto 
(7% do salário), calcule o salário líquido (salBruto- imposto + gratif) e exiba o salário líquido
"""

#QUEBRANDO O PROBLEMA EM PARTES
#receber o salário bruto 
#gratificação 5%
#imposto 7%
#bruto-imposto+gratificação 
#salário líquido 

#RECEBIMENTO DOS DADOS 
bruto=float(input("\nQual seu salário\n"))

#REALIZAÇÃO DOS CALCULOS 
gratificacao=float(bruto*0.05)
imposto=float(bruto*0.07)
liquido=float(bruto-imposto+gratificacao)

#SAÍDA DOS DADOS 
print(f"\nSeu salário liquido é {liquido}")


