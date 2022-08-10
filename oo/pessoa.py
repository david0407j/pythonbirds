class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=50):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    Davidson = Pessoa(nome='Davidson')
    luciano = Pessoa(Davidson, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrinho = 'santos'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos


    print(luciano.__dict__)
    print(Davidson.__dict__)
    Pessoa.olhos
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(Davidson.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(Davidson.olhos))



