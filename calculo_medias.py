print('Olá, sou um programa desenvolvido para você verificar suas notas ;-;\n')

T1 = float(input('Digite sua primeira nota: '))
T2 = float(input('Digite a segunda nota: '))
T3 = float(input('Digite a terceira nota: '))
s = T1 + T2 + T3
Ma = s / 3

print('\nA soma da nota trimestral foi de:{:.1f}'.format(s))
print('E sua média trimestral foi:{:.1f}\n'.format(Ma))

if Ma >= 7.0:
    print('parabéns você passou por nota ;-;')
    exit()
eles: Ma < 7.0
f = float(input('Qual foi a nota da média final: '))
Sf = round((f + Ma)/2)

if Sf >= 5.0:
    print('Parabéns você passosu na final!')
    exit()
eles: Sf < 4.9
print('Infelizmente você não recuperou na final!')
exit()