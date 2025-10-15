class Watch:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def __str__(self):
        return f"{self.__hora:02}:{self.__minuto:02}:{self.__segundo:02}"

    def get_hora(self):
        return self.__hora

    def get_minuto(self):
        return self.__minuto

    def get_segundo(self):
        return self.__segundo

    def set_hora(self, valor):
        if 0 <= valor <= 23:
            self.__hora = valor
        else:
            print("fail: hora invalida")

    def set_minuto(self, valor):
        if 0 <= valor <= 59:
            self.__minuto = valor
        else:
            print("fail: minuto invalido")

    def set_segundo(self, valor):
        if 0 <= valor <= 59:
            self.__segundo = valor
        else:
            print("fail: segundo invalido")

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1
        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora += 1
        if self.__hora > 23:
            self.__hora = 0


def main():
    watch = Watch(0, 0, 0)
    while True:
        raw = input()
        if raw is None:
            continue
        line = raw.rstrip("\r\n")
        if line == "":
            continue

        print(f"${line}")
        parts = line.split()

        if parts[0] == "end":
            break
        elif parts[0] == "show":
            print(watch)
        elif parts[0] == "set":
            hora = int(parts[1])
            minuto = int(parts[2])
            segundo = int(parts[3])
            watch.set_hora(hora)
            watch.set_minuto(minuto)
            watch.set_segundo(segundo)
        elif parts[0] == "next":
            watch.nextSecond()
        elif parts[0] == "init":
            hora = int(parts[1])
            minuto = int(parts[2])
            segundo = int(parts[3])
            watch = Watch(hora, minuto, segundo)


main()
