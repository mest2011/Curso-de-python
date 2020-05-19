#Imprimindo um texto no console
print("O Brasil ja conquistou 5 titulos mundiais!")
#Imprimindo texto no console e alterando separados de variaveis recebidas por parametro
print("O", "Brasil", "ja", "conquistou", "5", "titulos", "mundiais!", sep="-")
#Mudando ação apos impressão no console, passando por parametro
print("O Brasil ja conquistou 5 titulos mundiais!", end='')
#definindo variaveis e verificando seus tipos
pais = 'Italia'
qtd_mundiais = 4
print(type(pais))
print(type(qtd_mundiais))
#Imprimindo no console frase montada apartir de variaveis
print("\nA",pais,"ja ganhou",qtd_mundiais," vez(es) a copa do mundo!")

#exercicio 9
dia = 15
mes = 10
ano = 2015
print(dia, mes, ano, sep='/')