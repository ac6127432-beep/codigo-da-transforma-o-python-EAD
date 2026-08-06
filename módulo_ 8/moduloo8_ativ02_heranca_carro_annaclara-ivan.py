class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"marca: {self.marca}, modelo: {self.modelo}"

meu_carro = Carro("Renault", "clio")
print(meu_carro.exibir_info())

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        return f"marca: {self.marca}, modelo: {self.modelo}, autonomia da bateria: {self.autonomia_bateria} km"