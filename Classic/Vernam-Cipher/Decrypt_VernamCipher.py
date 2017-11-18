#!/usr/bin/env python
import random
import string
from operator import xor
def vernam_dec(key):
    #ciphertext diambil dari file karena waktu di copy manual hasil konversi sering berbeda
    textcipher = open('ciphertext.txt','r').read()
    #fungsi convert ke desimal text
    convdecimal = []
    for i in range(len(textcipher)):
        convdecimal.append(str(ord(textcipher[i])))
    decimal = ' '.join(convdecimal)
    print decimal
    #fungsi convert ke biner
    convbiner = []
    for i in range(len(convdecimal)):
        convbiner.append(str(bin(int(convdecimal[i]))[2:].zfill(8)))
    biner = ''.join(convbiner)
    print "hasil konversi ke biner karakter Ciphertext : "
    print ' '.join(convbiner)

    #perintah convert key ke desimal
    convkeydecimal = []
    for i in range(len(key)):
        convkeydecimal.append(str(ord(key[i])))
    keydecimal = ' '.join(convkeydecimal)
    #fungsi conver key ke biner
    convkeybiner = []
    for i in range(len(convkeydecimal)):
        convkeybiner.append(str(bin(int(convkeydecimal[i]))))
    binerkey = ''.join(convkeybiner)
    print "Hasil Konversi ke biner karakter kunci :"
    print ' '.join(convkeybiner)
    #fungsi replace biner ciphertext
    binercipher =biner.replace("b","")
    print "biner Ciphertext : \n"+binercipher
    #fungsi replace biner kunci
    binerkey =binerkey.replace("b","")
    print "biner kunci : \n"+binerkey
    #fungsi xor variabel pesan dan key
    ciphertext = []
    for i in range(len(binercipher)):
        ciphertext.append(xor(int(binercipher[i]),int(binerkey[i])))
    cipherfix =''.join(map(str,ciphertext))
    splits=[cipherfix[x:x+8] for x in range(0,len(cipherfix),8)]
    print "Hasil XOR variabel ciphertext dan kunci : \n"+str(splits)
    #fungsi convert ke hexa
    hexa = []
    for i in range(len(splits)):
        hexa.append(hex(int(splits[i],2)))
    print "Hasil KOnversi hasil XOR ke hexa : \n"+str(hexa)
    #fungsi convert ke desimal
    dec = []
    for i in range(len(hexa)):
        dec.append(int(hexa[i], 16))
    print "Hasil Konversi ke Desimal : \n"+str(dec)
    #fungsi convert ke ascii text
    teks = []
    for i in range(len(dec)):
        teks.append(chr(dec[i]))
    print "Gotcha!, Plaintext : \n"+''.join(teks)
    return exit()


def main():
    print "Vernam Cipher Dekriptor (ciphertext dari file)"
    key = raw_input("Masukkan key : ")
    print vernam_dec(key)
if __name__ == '__main__':
    	main()
