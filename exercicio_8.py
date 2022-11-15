def retornaLetraRepetida(palavra, letraRecebida):
    contador = 0
    for letra in palavra:
        if letraRecebida == letra:
            contador += 1
    return contador

print(str(retornaLetraRepetida("palavra","a")))
