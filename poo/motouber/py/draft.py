class Pessoa:
    def __init__(self, nome, dinheiro):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def get_nome(self):
        return self.__nome

    def get_dinheiro(self):
        return self.__dinheiro

    def pagar(self, valor):
        if valor >= self.__dinheiro:
            valor_pago = self.__dinheiro
            self.__dinheiro = 0
            return valor_pago
        else:
            self.__dinheiro -= valor
            return valor

    def __str__(self):
        return f'{self.__nome}:{self.__dinheiro}'


class Moto:
    def __init__(self):
        self.__custo = 0
        self.__passageiro = None
        self.__motorista = None

    def set_motorista(self, nome, dinheiro):
        self.__motorista = Pessoa(nome, dinheiro)

    def set_passageiro(self, nome, dinheiro):
        if self.__motorista is None:
            print("fail: No driver available")
            return
        self.__passageiro = Pessoa(nome, dinheiro)

    def drive(self, km):
        if self.__passageiro is not None:
            self.__custo += km
        else:
            print("fail: No passenger to drive")

    def leave_passenger(self):
        if self.__passageiro is not None:
            passageiro_nome = self.__passageiro.get_nome()
            custo_total = self.__custo

            valor_pago = self.__passageiro.pagar(custo_total)
            dinheiro_restante = self.__passageiro.get_dinheiro()

            if valor_pago < custo_total:
                print("fail: Passenger does not have enough money")
            print(f"{passageiro_nome}:{dinheiro_restante} left")

            novo_dinheiro_motorista = self.__motorista.get_dinheiro() + custo_total
            self.__motorista = Pessoa(
                self.__motorista.get_nome(), novo_dinheiro_motorista)

            self.__passageiro = None
            self.__custo = 0

        else:
            print("fail: No passenger to leave")

    def __str__(self):
        motorista_info = str(self.__motorista) if self.__motorista else "None"
        passageiro_info = str(
            self.__passageiro) if self.__passageiro else "None"
        return f"Cost: {self.__custo}, Driver: {motorista_info}, Passenger: {passageiro_info}"


def main():
    moto = Moto()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if line == "end":
            break

        elif args[0] == "show":
            print(moto)

        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            moto.set_motorista(nome, dinheiro)

        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            moto.set_passageiro(nome, dinheiro)

        elif args[0] == "drive":
            km = int(args[1])
            moto.drive(km)

        elif args[0] == "leavePass":
            moto.leave_passenger()

        else:
            print("fail: Unknown command")


main()
