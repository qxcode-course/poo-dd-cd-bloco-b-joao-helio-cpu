class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def setTamanho(self, valor):
        tamanhosValidos = ["PP", "P", "M", "G", "GG", "XG"]
        valor = valor.strip()
        if valor in tamanhosValidos:
            self.__tamanho = valor
        else:
            print(f"fail: Valor inválido, tente PP, P, M, G, GG, XG")

    def getTamanho(self):
        return self.__tamanho


def main():

    roupa = Roupa()

    while True:
        comando = input().strip()

        if comando == "end":
            break
        elif comando == "show":
            print(f"size: ({roupa.getTamanho()})")
        elif comando.startswith("size "):
            _, valor = comando.split(maxsplit=1)
            roupa.setTamanho(valor)
        else:
            print("fail: comando inválido")


main()
