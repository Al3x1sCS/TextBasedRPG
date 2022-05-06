# Pega os dados do player.

nome = input("Escreva o seu nome: ")
idade = input("Escreva sua idade: ")

# aprendendo a usar try
try:
    print(nome + ", você nasceu em {}" .format(2012 - int(idade)))
except TypeError:
    print('Não foi possivel...')