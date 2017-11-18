#!/usr/bin/env python
#Johan Wahyudi

from string import lowercase, uppercase

def caesar_en(text, key):
    result = []
    for c in text:
        if c in lowercase:
            enkripsi = lowercase.index(c)
            enkripsi = (enkripsi + key) % 26
            result.append(lowercase[enkripsi])
        elif c in uppercase:
            enkripsi = uppercase.index(c)
            enkripsi = (enkripsi + key) % 26
            result.append(uppercase[enkripsi])
        else:
            result.append(c)
    return "".join(result)
 
def caesar_dec(ciphertext, key_dec):
	hasil = []
	for d in ciphertext:
		if d in lowercase:
			dekripsi = lowercase.index(d)
			dekripsi = (dekripsi - key_dec) % 26
			hasil.append(lowercase[dekripsi])
		elif d in uppercase:
			dekripsi = uppercase.index(d)
			dekripsi = (dekripsi - key_dec) % 26
			hasil.append(uppercase[dekripsi])
		else:
			result.append(d)
	return "".join(hasil)

def main():
	text = raw_input("masukkan text :" )
	key = input ("masukkan key :")
	print caesar_en(text, key)
	print '\nEncrypting \"' + text + '\" dengan ROT' + str(key) + " => " + caesar_en(text, key) + '\n'
	ciphertext = raw_input("masukkan ciphertext :" )
	key_dec = input("masukkan key :" )
	print caesar_dec(ciphertext, key_dec)
	print '\nDecrypting \"' + ciphertext + '\" dengan ROT' + str(key_dec) + " => " + caesar_dec(ciphertext, key_dec) + '\n'
	

if __name__ == '__main__':
	main()
