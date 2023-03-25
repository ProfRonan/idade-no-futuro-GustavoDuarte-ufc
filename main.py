ano_atual = int(input())
idade_atual = int(input())

ano_comp = int(input())
nome = str(input())

if ano_atual < ano_comp:
    print(nome+", no ano de",ano_comp,"você terá",ano_comp-ano_atual+idade_atual,"anos")