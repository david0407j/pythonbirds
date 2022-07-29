class Pessoa:
    def Cumprimentar(self):
        return 'olá'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.Cumprimentar(p))
    print(id(p))
    print(p.Cumprimentar())