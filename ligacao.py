import codigomorse
import crypto
import cutMusic
import cutvideo
import TextSpeech
import Financee

print("What tool do you want use?")
desire = input("A - Codigo Morse, B - Criptografar Mensagem, C - Cortar Musica, D - Cortar Video, E - Consultar Stocks, F - Converter Texto para audio  ")
desire.upper()

if desire.isString():
    if desire == "A":
        try: 
    
            mensagem = input("Mensagem to transform in Codigo Morse:")
            codigomorse(mensagem)
        except:
            print("Error , digit just the letter of the option ")

    if desire == "B":
        try: 
    
            mensagem = input("Mensagem to transform Cryptograph:")
            crypto.Cryptography(mensagem)
        except:
            print("Error , digit just the letter of the option ")

    if desire == "C":
        try: 
    
            start = input("Começo do Audio em segundos:")
            end = input("final do audio em segundos:")
            path = input("Endereço do Audio:")
            formats = input("Formato desejado:")

            cutMusic(start, end, path, formats)
        except:
            print("Error , digit just the letter of the option ")
 
    if desire == "D":
        try: 
    
            start = input("Começo do Video em segundos:")
            end = input("final do Video em segundos:")
            path = input("Endereço do Video:")
            path2 = input("Endereço de onde gostaria de salva-lo")

            cutvideo(start, end, path, path2)
        except:
            print("Error , digit just the letter of the option ")
   
    if desire == "E":
        try:
            name = input("Nome da Stock que queres Consultar:")
            timeperiod = input("Periodo de Tempo:")
            Financee.stocks(name, timeperiod)

        except:
            print("Error , digit just the letter of the option ")

    if desire == "F":

        try: 
            message = input("Mensagem que queres passar para audio")
            nome = input("nome do audio queres dar:")
            TextSpeech.textSp(message, nome)

        except:
            print("Error , digit just the letter of the option ")



