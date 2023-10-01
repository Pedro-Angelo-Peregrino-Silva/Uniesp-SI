# Peça ao usuário para inserir o número de horas extras e o número de horas que o funcionário faltou.
# Se a quantidade de horas extras for maior que as horas faltadas mais 50%, imprima "Bônus de R$ 500.00".
# Caso contrário, imprima "Sem bônus".

hora_extra, hora_falta = (int(input('Digite a quantidade de horas extras: ')),
                          int(input('Digite a quantidade de horas faltadas: ')))
hora_falta_50 = hora_falta + (hora_falta//2)

if hora_extra >= hora_falta_50:
    print('Bônus de R$ 500,00.')
else:
    print('Sem bônus.')
