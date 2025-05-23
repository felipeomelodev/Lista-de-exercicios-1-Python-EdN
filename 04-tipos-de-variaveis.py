"""
Imprima na tela o tipo de cada variável abaixo, 
depois mude o tipo de cada uma e verifique o novo tipo
"""

x = 10
y = "Dez"

print("Tipo inicial da variável x:", type(x))
print("Tipo inicial da variável y:", type(y))

x = str(x)
y = 10

print("Novo tipo da variável x:", type(x))
print("Novo tipo da variável y:", type(y))