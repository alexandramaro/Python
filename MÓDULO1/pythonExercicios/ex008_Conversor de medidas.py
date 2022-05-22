medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'{medida}m corresponde a {dm:.0f}dm, a {cm:.0f}cm e a {mm:.0f}mm'
      f'\n{medida}m corresponde a {dam}dam, a {hm}hm e a {km}km')
