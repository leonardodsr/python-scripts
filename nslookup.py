import subprocess, os


selecao = input("lista ou unico?: ")


if selecao == 'lista':
	for server in open('server_list.txt'):
		os.system('nslookup' + server)
		#subprocess.Popen(['nslookup' + server])
elif selecao == 'unico':
	dominio = input('Insira o Dominio a ser pesquisado: ')
	os.system('nslookup '+dominio)
	#subprocess.Popen(['nslookup ' + dominio])
else:
	print('Opcao invalida!')


