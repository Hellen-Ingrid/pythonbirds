class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    hellen.sobrenome = 'Cunha'
    del hellen.filhos
    hellen.olhos = 1
    del hellen.olhos
    print(hellen.__dict__)
    print(romeu.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(hellen.olhos)
    print(romeu.olhos)
    print(id(Pessoa.olhos), id(hellen.olhos), id(romeu.olhos))
    print(Pessoa.metodo_estatico(), hellen.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), hellen.nome_e_atributos_de_classe())
