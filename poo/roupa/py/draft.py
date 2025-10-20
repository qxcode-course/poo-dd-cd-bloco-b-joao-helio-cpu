class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def set_tamanho(self, valor: str) -> None:
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhos_validos:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        self.__tamanho = valor

    def get_tamanho(self) -> str:
        return self.__tamanho


def main():
    roupa = Roupa()

    while True:
        line = input().strip()
        if not line:
            continue
        print(f"${line}")
        parts = line.split()

        if parts[0] == "end":
            break
        elif parts[0] == "show":
            print(f"size: ({roupa.get_tamanho()})")
        elif parts[0] == "size":
            tamanhoEscolhido = parts[1]
            roupa.set_tamanho(tamanhoEscolhido)


main()
