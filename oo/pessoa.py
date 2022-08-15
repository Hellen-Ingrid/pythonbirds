class Pessoa:
    def __init__(self, *filhos, nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    romeu = Pessoa(nome='Romeu')
    hellen = Pessoa(romeu, nome='Hellen')
    print(Pessoa.cumprimentar(hellen))
    print(id(hellen))
    print(hellen.cumprimentar())
    print(hellen.nome)
    print(hellen.idade)
    for filho in hellen.filhos:
        print(filho.nome)

