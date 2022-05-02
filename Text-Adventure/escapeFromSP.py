# Este jogo é uma aventura baseada em texto, que consiste em escapar de São Paulo.
print("Escape de São Paulo!")
print("Ações validas: Norte [n], Sul [s], Este [e], Oeste [o].")
action_input = input("Digite uma direção: ")
if action_input == "n":
    print("Indo para o Norte!")
elif action_input == "s":
    print("Indo para o Sul!")
elif action_input == "e":
    print("Indo para o Este!")
elif action_input == "o":
    print("Indo para o Oeste!")
else:
    print("Direção invalida! Digite uma direção valida. ")
