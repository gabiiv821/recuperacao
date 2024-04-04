# import forca 
# import adivinhacao 

def escolhe_jogo():
    print("***********************************")
    print("*******escolha o seu jogo !********")
    print("***********************************")
    
    print("(1) força (2) adivinhação")
    
    jogo = int (input("jogando forca"))
    
    if(jogo == 1):
         print ("jogando forca")
        #  forca.jogar()
    elif (jogo==2):
             print ("jogando adivinhação")
            #  adivinhacao.jogar()
if(__name__ == "__main__"):
     escolhe_jogo()

