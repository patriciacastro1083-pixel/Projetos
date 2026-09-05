# Calculadora de consumo Elétrico Inteligente
# Autora: Patricia Elen Castro Alves


#Entrada

aparelho = input('Digite o aparelho ')
potência = float(input('Qual a potência do aparelho em Whatts? '))
horas_dias = float(input('Tempo médio de uso em Horas, por dia '))


# Cálculo do consumo mensal (em kwh)

consumo_mensal = (potência * horas_dias * 30) /1000


# Definindo o valor da tarifa fixa por kWh em reais

tarifa_kWh = 1.04


# Cálculo do consumo estimado por hora (em kWh)

consumo_por_hora = (potência / 1000)


# Exibição do resultado

print(f'O consumo estimado do(a) {aparelho} é de {consumo_mensal} kWh/mês')    
print(f'o custo estimado do consumo do(a) {aparelho} é de R$ {consumo_por_hora:.2f} por kWh')
