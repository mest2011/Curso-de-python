class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'Nome: {self.nome} - Ano {self.ano} - Likes: {self.likes} '


class Filme(Programa):
    # Python Data Model
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    #Python Data Model
    def __str__(self):
        return f'Nome: {self.nome} - Duração {self.duracao} - Likes: {self.likes} '

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Temporadas {self.temporadas} - Likes: {self.likes} '

class Playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self._programas = programa

    # Python Data Model
    def __getitem__(self):
       return self._programas

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

    def __iter__(self):
        return self._programas.__iter__()

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in filmes_e_series:
    print(programa)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')
print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')