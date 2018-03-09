import subprocess

selecao = input("lista ou unico?: ")

if selecao == 'lista':
	for server in open('server_list.txt'):
		subprocess.Popen(('nslookup' + server))
elif selecao == 'unico':
	dominio = input('Insira o Domínio a ser pesquisado: ')
	subprocess.Popen(('nslookup' + dominio))
else:
	print('Opçao inválida!'')
	
	

