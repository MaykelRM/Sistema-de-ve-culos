class Veiculos:
    def __init__(self, marca, modelo, ano, tipo, info_extra, cap_tanq, cons_medio):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.tipo = tipo
        self.info_extra = info_extra
        self.cap_tanq = cap_tanq
        self.cons_medio = cons_medio

    def calcular_autonomia(self):
        return self.cap_tanq * self.cons_medio

    def exibir_detalhes(self):
        print(f"{self.tipo}:")
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
        print(f"Capacidade do Tanque: {self.cap_tanq}L, Consumo Médio: {self.cons_medio} km/L")
        print(f"Informação Extra: {self.info_extra}")
        print(f"Autonomia: {self.calcular_autonomia()} km")