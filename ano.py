def calcular_idade(ano_nascimento):
    return 2022 - ano_nascimento

while True:
    nome = input("Digite seu nome completo: ")
    ano = input("Digite seu ano de nascimento (entre 1922 e 2021): ")
    
    try:
        ano = int(ano)
        if 1922 <= ano <= 2021:
            idade = calcular_idade(ano)
            print(f"{nome}, você completou ou completará {idade} anos em 2022.")
            break
        else:
            print("Ano inválido. Por favor, insira um ano entre 1922 e 2021.")
    except ValueError:
        print("Por favor, insira um número válido para o ano.")

