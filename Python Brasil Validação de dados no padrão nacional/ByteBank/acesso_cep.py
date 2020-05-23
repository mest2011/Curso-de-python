import requests

class AcessoCep:
    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError('Cep inválido!')

    def __str__(self):
        return self.format()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def acessa_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json'
        r = requests.get(url)
        dados = r.json()
        return (
            dados['logradouro'],
            dados['bairro'],
            dados['localidade']
        )