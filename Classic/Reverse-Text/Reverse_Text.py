#!/usr/bin/env python
kata = input('masukan kata yang ingin di balik : ')
balik = ''
i = len(kata) - 1
while i >= 0:
	balik = balik + kata[i]
	i = i-1
print('hasil : '+balik)
