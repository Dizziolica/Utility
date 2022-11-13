def codigomorse(mensagem):
    codigomorse = { "A":".-" ,
    "B": "-...", 
    "C": "-.-.", 
    "D": "-..", 
    "E": ".", 
    "F": "..-.", 
    "G": "--.", 
    "H": "....",
    "I": "..", 
    "J": ".---", 
    "K": "-.-", 
    "L": ".-..", 
    "M": "--", 
    "N": "-.", 
    "O": "---", 
    "P": ".--.", 
    "Q": "--.-", 
    "R": ".-.",
    "S": "...", 
    "T": "- ", 
    "U": "..-", 
    "V": "...-",
    "W": ".--", 
    "X": "-..-", 
    "Y": "-.--",
    "Z": "--.."}

    palavra = input("Texto para converter em codigo morse:  ").upper()
    lista= list(palavra)
    comprimento = len(lista)


    for i in lista:
    
        if i != "":
            try:
                print(i)
                print(codigomorse[i])
        
            except:
                print("Error, Try Again")

