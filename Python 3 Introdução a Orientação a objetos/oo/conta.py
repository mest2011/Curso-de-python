class Conta:
    def __init__ (self, numero, titular, saldo, limite):
        print('Contruindo objeto....')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print(f"Seu saldo é R$ {self.__saldo}")
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        limite = self.limite + self.saldo
        return valor_a_sacar <= limite

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Limite insuficiente!")

    def transferir(self, conta_destino, valor):
        self.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return __codigo_banco

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}