'''

i = 0

while i<10:
    print(i)
    i+=1



num1 = int(input("Digite o número para ser começar o calculo dos pares: "))
num2 = int(input("Digite um número maior que o anterior: "))
i = num1

while i <= num2:
    if i%2==0:
        print(f"{i} é par!")
    i+=1



i=0

qtd_pares = 0

num = int(input("Digite um numero: "))
while i<10:
    num = int(input("Digite outro numero: "))
    if num%2==0:
        qtd_pares+=1
    i+=1
print(f"Há {qtd_pares} entre os numero digitados")



i = 0
qtd_vog = 0
while i<10:
    letra = input("Digite uma letra: ")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        qtd_vog += 1
    i += 1

print(f"Vc digitou {qtd_vog+1} vogais dentre essas {i+1} letras")

'''


usuario = "aluno_fiap"
senha = "123456"

i = 0



while i != 4:
    dgt_usuario = input("Digite o usuário: ")
    dgt_senha = input("Digite a senha: ")
    if dgt_usuario == usuario and dgt_senha == senha:
        print(f"Bem vindo {usuario}!!!")
        i = 4
    elif dgt_usuario == usuario or dgt_senha == senha:
        print(f"Usuário ou senha incorretos!!! Você tem {3-i} tentativas para acertar")
        i += 1
    else:
        print(f"Burro da porrakkkk!!! Você tem {3-i} tentativas para acertar")
        i += 1