nota_maxima = 100

def entrevista_tecnica(nome_do_candidato, *provas):
    global nota_maxima
    print('Valor inicial da variável global nota_maxima: ', nota_maxima)
    print('-------------------------------------')  
    print('Nome do Candidato: ', nome_do_candidato)
    nota_total = 0
    for nota_prova in provas:
        nota_total += nota_prova
    nota_maxima = 70    
    print('Nota total do candidato: ', nota_total)

entrevista_tecnica('Rodrigo Mello', 10, 7, 8)
print('-------------------------------------') 
print('O valor atual da variável global nota_maxima é: ', nota_maxima)       