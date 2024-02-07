vestoque = 5
i = 1
x = int(input("Quantos pães você deseja?"))

for i in range(1,x+1):
    if i > vestoque:
        print("Só temos", vestoque, "unidades em estoque, Desculpe pelo transtorno")
        break
    print("Pão", i)
    if i == x:
            print("Obrigado!")
print("Fim do loop")        