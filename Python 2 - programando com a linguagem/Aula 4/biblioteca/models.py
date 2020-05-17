# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrão para perfis de usuários'

	def __init__(self, nome, telefone, empresa):
		if(len(nome) < 3):
			raise ArgumentoInvalidoError('Nome deve ter pelo menos 3 caravteres')
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print('Nome: %s, Telefone: %s, Empresa: %s' %(self.nome,self.telefone,self.empresa))

	def curtir(self):
		self.__curtidas += 1

	def get_curtidas(self):
		return self.__curtidas

	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		for linha in arquivo:
			valores = linha.split(',')
			if(len(valores) != 3):
				raise ArgumentoInvalidoError('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
			perfis.append(classe(*valores))
		arquivo.close()
		return perfis

class Perfil_vip(Perfil):
	'Classe padrão para perfis de usuários VIP'

	def __init__(self, nome, telefone, empresa, apelido=''):
		super (Perfil_vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_vip, self).get_curtidas() * 10.0

class ArgumentoInvalidoError (Exception):
	def __init__(self, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return repr(self.mensagem)



class Data(object):
	'Classe para formatação de data e impressao no console'

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprime(self):
		print('%s/%s/%s' % (self.dia, self.mes, self.ano))
