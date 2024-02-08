print(10, ['Azul', 'vermelho'])
i = 10
lista = ['Azul', 'vermelho']
print(i,lista)

lista
lista.pop()
lista


def funcaoteste(param_a,param_b):
    param_a = param_a - 1
    param_b.pop()
    print(param_a,"->valor da variavel param_0 modificado da função.")
    if __name__ == "__main__":
        i = 4
        lista = ["Azul", "branco"]
        funcaoteste(i,lista)
        print(i,"-> manteve o valor da variavel param_a que foi atributo antes da chamada da função.", '\n', lista)