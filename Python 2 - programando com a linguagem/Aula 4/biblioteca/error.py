from models import * 
try:
	perfis = Perfil.gerar_perfis('perfis.csv')
except Exception as e:
	print(e)
