class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("(Buzinando...)")

    def parar(self):
        print("Parando Bicicleta")
        print("A bicicleta parou")

    def correr(self):
        print("Fiaaaaummm...")

    # def __str__(self):
    #     return f"""
    #     Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}
    #     """

    def trocar_marcha(self, n_marcha):

        print("Trocando marcha...")

        def _trocar_macha():
            if n_marcha > self.marcha:
                print("Marcha trocada")
            else:
                print("Marcha nao foi trocada")

    def __str__(self):
        return f"{
        self.__class__.__name__}:{
        ', '.join([f'{chave}={valor}'
        for chave,valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.trocar_marcha(2)
b1.correr()
b1.parar()
