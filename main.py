'''class ControleRemoto:
    caracteristicas:
    - cor
    - altura
    - profundidade
    - largura

    metodos:
    - passar de canal
    - aumentar/diminuir o volume
    - abrir a netflix
    - desligar a TV'''

class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura


    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar o canal')
        elif botao == '-':
            print('Diminuir o canal')
controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm') #instancia do ControleRemoto
controle_remoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm') #instancia do ControleRemoto

controle_remoto.passar_canal('+')