# =========================================================================
print("============ Exemplo de Herança Simples ============")

class Veiculo:
    def __init__(self, cor, placa, modelo, motor, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.modelo = modelo
        self.motor = motor
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor...")

    def __str__(self):
        return f"{self.__class__.__name__}:\n- {'\n- '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    ...


class Carro(Veiculo):
    ...


class Caminhao(Veiculo):
    def __init__(self, cor, placa, modelo, motor, numero_rodas, carregado):
        super().__init__(cor, placa, modelo, motor, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado")


moto = Motocicleta("Preta", "QWE-1234", "Hornet", "600cc", 2)
print("Motocicleta")
moto.ligar_motor()

carro = Carro("Branco", "ASD-1234", "Fiat Uno", "1.0", 4)
print("\nCarro")
carro.ligar_motor()

caminhao = Caminhao("Azul", "ZXC-1234", "Scania", "420", 10, False)
print("\nCaminhão")
caminhao.ligar_motor()
caminhao.esta_carregado()

print(f"\n\n{moto}")
print(f"\n{carro}")
print(f"\n{caminhao}")
