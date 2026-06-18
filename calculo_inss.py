#CALCULO DE DESCONTO 

#SOLICITAÇÃO
"""
Faça um software que solicite o número de horas trabalhadas, o valor recebido 
por hora e o percentual de desconto (INSS), de um funcionário que trabalhe por 
hora. O algoritmo deverá mostrar o salário bruto, o valor descontado e o valor 
do salário líquido.
"""
#1-DESMEMBRANDO O PROBLEMA 
#solicitar horas trabalhadas
#valor recebido por hora
#percentual de desconto (inss)
#mostrar salario bruto
#mostrar valor descontado
#mostrar valor do salario liquido

#2-RECEBIMENTO DOS DADOS 
print("="*50)
print("CALCULO DE DESCONTO (INSS)")
print("="*50)

horas=float(input("\nDigitar o numero de horas trabalhadas:\n"))
valor_hora=float(input("\nDigite o valor da hora trabalhada:\n"))
inss=float(input("\nDigite a porcentagem de desconto do inss:\n"))

#PROCESSAMENTO DOS DADOS 

salario_bruto=horas * valor_hora
desconto=valor_hora*inss/100
salario_liquido=salario_bruto-desconto

#SAIDA DE DADOS 
print("="*50)
print("RESULTADOS DOS DESCONTOS")
print("="*50)
print(f"\nO salario bruto é {salario_bruto}.")
print(f"\nO valor descontado é {desconto}.")
print(f"\nO valor liquido é {salario_liquido}.")

