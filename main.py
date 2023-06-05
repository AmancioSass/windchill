import math

temperatura = float(input("Qual é a temperatura? "))
tipo = input("Fahrenheit ou Celsius (F/C)? ")

def celsius_para_fahrenheit(temperatura):
    return temperatura * 9 / 5 + 32

def sensacao_termica(temperatura, velocidade):
    return 35.74 + 0.6215 * temperatura - 35.75 * (velocidade ** 0.16) + 0.4275 * temperatura * (velocidade ** 0.16)
   
if(tipo.strip().upper() == "C"):
    temperatura = celsius_para_fahrenheit(temperatura)

for velocidade in range(5, 61, 5):
    sensacao = sensacao_termica(temperatura, velocidade)
    print("A temperatura de {}F, e a velocidade do vento {} mph, a sensação termica é: {:.2f}F".format(temperatura, velocidade, sensacao))

 