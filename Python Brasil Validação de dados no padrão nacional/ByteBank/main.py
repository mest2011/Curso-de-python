from acesso_cep import AcessoCep

cep = '03609000'
cep_obj = AcessoCep(cep)
rua, bairro, cidade = cep_obj.acessa_via_cep()
print(cep_obj.acessa_via_cep())
print(rua, bairro, cidade)



"""
#test class datas_br
from datas_br import DatasBr

data = DatasBr()
print(data.tempo_cadastro())

#test class cpf_cnpj
from cpf_cnpj import Documento

numero_cnpj = '78964433000154'
cnpj_1 = Documento().cria_documento(str(numero_cnpj))
print(cnpj_1)

numero_cpf = 92460300018
cpf_1 = Documento().cria_documento(str(numero_cpf))
print(cpf_1)

#test class TelefoneBr

from TelefoneBr import TelefoneBr

telefone = '121212341234'
telefone_objeto = TelefoneBr(telefone)
print(telefone_objeto.)


"""