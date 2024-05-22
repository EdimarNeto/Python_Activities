m = float(input('Digite a distâcia em Metros para converter em outros valores: '))
cm = m * 100
mm = m * 1000
dc = m / 100
km = m / 1000
print(f'Convertendo esse valor temos:'
      f'\n{cm:.0f} centímetros'
      f'\n{mm:.0f} milímetros')
print('Também temos:'
      f'\n{dc} decâmetros'
      f'\n{km} quilômetros')
