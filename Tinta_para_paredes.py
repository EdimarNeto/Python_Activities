larg = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))
area = larg * alt
print(f'Sua parede têm a aréa de {area:.1f}m².'
      '\nSabendo que cada lata de tinta cobre uma aréa de 2m²'
      f'\nPara pintar uma parede como essa será necessário {area / 2:.1f} litros de tinta.')
