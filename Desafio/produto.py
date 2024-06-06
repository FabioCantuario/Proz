def validar(preco):
    if(preco>100):
        return "Alto"
    elif(preco>=50 and preco <=100):
        return "Medio"
    else:
        return "Baixo"

produto =input("Produto: ")
classificacao = validar(float(input("Preco: ")))
print("O produto : " + produto + " é classificado como: " + classificacao)
