# Desenvolva um programa Python que oferece a funcionalidade de contar o número de caracteres
# ou o número de palavras em um texto fornecido pelo usuário. O programa continuará executando
# até que o usuário opte por sair do sistema.



def menuPrincipal():
  condicao = False
  while(condicao == False):
    print("-------------------------------------")
    print("1 -------------- Digite um texto")
    print("2 -------------- Contar palavra")
    print("3 -------------- Contar caracter")
    print("0 -------------- Sair")
    print("-------------------------------------")
    op = int(input("Digite a opção: "))
    
    if(op == 1):
            texto = input("Digite um texto: ")
            condicao = False
            continue
    elif(op == 2):
           qtdletras = len(texto.strip())
           textoTam = len(texto) - texto.count(" ")
           print("Quantidade de letras: " + str(textoTam))
           condicao = False
           continue
    elif(op == 3):
          palavras = texto.split()
          contagem = len(palavras)
          print(contagem)
          condicao = False
          continue
    elif(op == 0):
        condicao = True
        break
    else:
        codicao = False
        return 
      
menuPrincipal()