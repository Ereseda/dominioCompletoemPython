numero_guiche_atendimento = "RK550999"
print(numero_guiche_atendimento)
len(numero_guiche_atendimento)
print(numero_guiche_atendimento[1])

numero_guiche_atendimento = "RK550999"
for i in range(0,len(numero_guiche_atendimento)):
    print(numero_guiche_atendimento[i])

# Exemplo resolvido do gpt
import random
import string

def gerar_identificacoes():
    identificacoes = []
    for i in range(5):
        identificacao = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        identificacoes.append(identificacao)
    return identificacoes

def gerar_senha():
    caracteres_especiais = "!@#$%&*"
    senha = ''.join(random.choices(string.ascii_letters + string.digits + caracteres_especiais, k=6))
    return senha

def gerar_senhas_por_identificacao(identificacao):
    senhas = []
    for i in range(10):
        senha = gerar_senha()
        senhas.append(senha)
    return senhas

def main():
    identificacoes = gerar_identificacoes()
    guiches_senhas = {}
    for identificacao in identificacoes:
        senhas = gerar_senhas_por_identificacao(identificacao)
        guiches_senhas[identificacao] = senhas

    print("Identificações dos Guichês:")
    for identificacao, senhas in guiches_senhas.items():
        print(identificacao)
        print("Senhas de Atendimento:")
        for senha in senhas:
            print(senha)
        print()

if __name__ == "__main__":
    main()

# Exemplo resolvido do curso
import random, string

def Guiche():
    C_MAIN_GUICHE = 'RK56737YTU802'
    return C_MAIN_GUICHE

def getLowerCase(lenght):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(lenght))
    
def getUpperCase(lenght):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(lenght))
    
def getSpecialCharacter(lenght):
    return ''.join(random.choice('!@#$%&amp;*') for i in range(lenght))

def getNumbers(lenght):
    return ''.join(random.choice(string.digits) for i in range(lenght))
    
def getRandomNewPasswd():
    return ''.join(random.choice(getSpecialCharacter(1) +
                                 getUpperCase(2) +
                                 getLowerCase(4) +
                                 getNumbers(2)
                                 ) for i in range(6))

def RandomGuiche(valueGuiche):
    count = 0
    while True:
        count += 1
        newGuiche = ''.join(random.sample(valueGuiche, len(valueGuiche)))
        print('-----------GUICHE-----------')
        print('|- Guiche: ', newGuiche, '-|')
        for i in range (0, 6):
            print('|-- Senha: ', getRandomNewPasswd(), '--------|')
        print('----------------------------')
        if count == 5:
            break
        
def main ():
    RandomGuiche(Guiche())
        
main()