from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format()

    def mes_cadastro(self):
        meses_do_ano = [ "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
                         ]
        mes_cad = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cad]

    def dia_semana_cadastro(self):
        dia_semana = [ "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
        dia_cad = self.momento_cadastro.weekday()
        return dia_semana[dia_cad]

    def format(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        diferenca = datetime.today() - (self.momento_cadastro - timedelta(days=24))
        return diferenca