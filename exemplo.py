# Vamos criar uma classe para Clientes da Netflix

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['Basic', 'Premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano Inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano Inválido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver Filme {filme}')
        elif self.plano == 'Premium':
            print(f'Ver Filme {filme}')
        elif self.plano == 'Basic' and plano_filme == 'Premium':
            print('Faça um upgrade para ver esse filme')
        else:
            print('Plano Inválido')


cliente = Cliente('Adler', 'adler@gmail.com', 'Basic')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'Premium')
# botao de upgrade
cliente.mudar_plano('Premium')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'Premium')
