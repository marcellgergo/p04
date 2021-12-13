# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!
szam = int(input('Kérek egy számot!'))
szám = int(input('Kérek egy másik számot!'))
szam1 = int(input('Kérekegy harmadik számot!'))

if szam > szám < szam1:
  print( szám , 'a kisebb!')
if szám > szam < szam1:
  print( szam , 'a kisebb!') 
if szam > szam1 < szám:
  print( szam1 , 'a kisebb!')
else:
  print('Egyenlőek!')