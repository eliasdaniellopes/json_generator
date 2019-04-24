#Anteção, isto é somente um protótipo irá gerar somente arquivos json básicos com somente 1 nível e que aceita somente strings, no futuro irei aprimorá-lo
from teste_json1 import GerarJson

dict = {}
while True:
    chave = str(input('Digite a chave'))
    valor = str(input('Digite o valor'))
    continuar = str(input('Deseja continuar? s/n'))
    
    if continuar.lower() != 's':
        dict[chave] = valor
        break
    
    dict[chave] = valor

gerar = GerarJson(dict)

