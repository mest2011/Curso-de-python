# -*- coding: UTF-8 -*-
import re

def procurar_part(nomes):
	regex = ' '.join(nomes)
	#print(regex)
	print('Digite o nome:')
	part_name = input()
	command = r'('+part_name+'\w+)'
	resultado = re.findall(command, regex)
	print(resultado)
	
def procurar(nomes):
	print('Digite o nome que deseja saber se foi cadastrado:')
	nome = input()
	if (nome in nomes):
		print('O nome existe no sistema!')
	else:
		print('O nome não existe ainda no sistema!')

def alterar(nomes):
	print('Qual nome vc deseja alterar?')
	nome_digitado = input()
	if (nome_digitado in nomes):
		print('Qual o novo nome?')
		nome_novo = input()
		nomes[nomes.index(nome_digitado)] = nome_novo
	else:
		print('Nome não existe.')

def remover(nomes):
	print('Qual nome vc deseja remover?')
	nome = input()
	nomes.remove(nome)

def listar(nomes):
	print('Listando nomes:')
	for nome in nomes:
		print(nome)

def cadastrar(nomes):
	print('Digite o nome: ')
	nome = input()
	nomes.append(nome)

def menu():
	nomes = ['Miguel', 'Mayara']
	escolha = ''
	while (escolha != '0'):
		print('Digite: 1 para cadastrar, 2 para listar, 3 remover, 4 alterar, 5 procurar e 0 para sair')
		escolha = input()

		if (escolha == '1'):
			cadastrar(nomes)

		if (escolha == '2'):
			listar(nomes)

		if (escolha == '3'):
			remover(nomes)

		if (escolha == '4'):
			alterar(nomes)

		if (escolha == '5'):
			procurar(nomes)

		if (escolha == '6'):
			procurar_part(nomes)

menu()