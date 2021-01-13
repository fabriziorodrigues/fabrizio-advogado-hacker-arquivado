
texto = input("Digite o seu texto aqui: ")

if texto.find("$") != -1:
    texto = texto.replace("$", "i")

    
if texto.find("#") != -1:
    texto = texto.replace("#", "a")

    
if texto.find("*") != -1:
    texto = texto.replace("*", "e")

print(texto)