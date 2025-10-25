class Lapiseira:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.tip = None

    def hasGrafite(self) -> bool:
        return self.tip is not None

    def inserir(self, grafite: "Grafite"):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return
        if grafite.thickness != self.thickness:
            print("fail: calibre incompativel")
            return
        self.tip = grafite

    def remover(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return None
        grafiteRemovido = self.tip
        self.tip = None
        return grafiteRemovido

    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return
        grafite = self.tip
        if grafite.size <= 10:
            print("fail: tamanho insuficiente")
            return

        gasto = grafite.usagePerSheet()
        tamanhoFinal = grafite.size - gasto

        if tamanhoFinal < 10:
            grafite.size = 10
            print("fail: folha incompleta")
        else:
            grafite.size = tamanhoFinal
            return

    def __str__(self):
        if self.tip is None:
            return f"calibre: {self.thickness}, grafite: null"
        else:
            return f"calibre: {self.thickness}, grafite: [{self.tip}]"


class Grafite:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self) -> int:
        tabela = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6
        }
        return tabela.get(self.hardness, 1)

    def __str__(self):
        return f"{self.thickness}:{self.hardness}:{self.size}"


def main():
    lapiseira = None
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if line == "end":
            break

        if args[0] == "init":
            lapiseira = Lapiseira(float(args[1]))

        elif args[0] == "insert":
            grafite = Grafite(float(args[1]), args[2], int(args[3]))
            lapiseira.inserir(grafite)

        elif args[0] == "remove":
            lapiseira.remover()

        elif args[0] == "write":
            lapiseira.writePage()

        elif args[0] == "show":
            print(lapiseira)


main()
