from itertools import*
s='457 46 567 12 136 235 13'.split()
v='FE EC CA AB BD DF FG DG GC'.split()
print(*range(1,8))
for p in permutations('ABCDEFG'):
    if all(str(p.index(a)+1)in s[p.index(b)] for a,b in v):
        print(*p)


from itertools import*
# дороги из пунктов в порядке возрастания
# 347 из п1, 3456 из п2 и т.д.
s = '347 3456 1245 1237 236 25 14'.split()
# дороги в графе
# из A в B, из A в C
v = 'AB AC AD BC CD CE DE DF EF EG FG'.split() 
# стивим цифры от 1 до 7       
print(*range(1,8))  
# стивим цифры от 1 до 7  
# перебираем все перестановки букв      
for p in permutations('ABCDEFG'):
  # формируем предполагаемое соответствие именам номеров
  # если все дороги на графе соответствуют дорогам из таблицы
  if all(str(p.index(b)+1)in s[p.index(a)] for a,b in v):
      # выводим номера пунктов
      print(*p)
