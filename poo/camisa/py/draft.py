class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) :
        return self.__tamanho
        
    def setTamanho(self, valor:str):
        if valor == "PP" or valor == "P" or valor == "M" or valor == "G" or valor == "GG" or valor == "XG":
            self.__tamanho = valor
            return self.__tamanho
        
        else:
            print("Errado!")
        
    
def main():
    blusa = Camisa()

    while blusa.getTamanho() == "":
        tam = str(input("Digite o tamanho da blusa: "))

        if blusa.setTamanho(tam):
            print(f"Sua blusa é tamanho {blusa.getTamanho()}!")
            break
        else:
            print ("Opção invalida! As disponiveis são: PP, P, M e G, GG e XG")

main()
