import os

def log(mensagem): 
    if 'MINHA_VAR' in os.environ:
        print(os.environ['MINHA_VAR'])
    print("Adicionando log via função: ", mensagem)

