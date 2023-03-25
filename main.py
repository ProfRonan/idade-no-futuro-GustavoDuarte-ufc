anoatual = int(input())
idadeatual = int(input())

anocomp = int(input())
nome = str(input())

if anoatual < anocomp and anoatual > 0 and idadeatual > 0 and anocomp > 0:
    print(nome+", no ano de",anocomp,"você terá",(anocomp-anoatual+idadeatual),"anos")