import platform
import pyperclip


plataforma = platform.platform()
processador = platform.processor()
arq = platform.architecture()

valor = "Plataforma: " + str(plataforma) + "\nCPU: " + str(processador) + "\nArquitetura: " + str(arq)
print(valor) 

pyperclip.copy(valor)

