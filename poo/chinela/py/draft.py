class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho 
    
    def setTamanho(self, valor:int):
        if valor % 2 == 0 and 20 <= valor <= 50:
            self.__tamanho = valor
            return self.__tamanho
             
        else:
            print ("errado")


def main():
    chinela = Chinela()

    while chinela.getTamanho() == 0: 

        tamanho = int(input("Digite seu tamanho de chinela ")) 

        if chinela.setTamanho(tamanho):
            print("Tamanho", chinela.getTamanho(), "registrado com sucesso!")
            break

        else: 
            print("Valor inválido! O tamanho deve ser PAR e estar entre 20 e 50.")

main()