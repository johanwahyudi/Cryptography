#!/usr/bin/env python
import random
import string
from operator import xor
def vernam_enc(pesan):
    #perintah random string
    acak = ''.join([random.choice(string.ascii_letters) for i in xrange(len(pesan))])
    print "Teks random sebagai kunci : "+acak
    #fungsi convert ke desimal
    convdecimal = []
    for i in range(len(pesan)):
        convdecimal.append(str(ord(pesan[i])))
    decimal = ' '.join(convdecimal)
    #fungsi convert ke biner
    convbiner = []
    for i in range(len(convdecimal)):
        convbiner.append(str(bin(int(convdecimal[i]))[2:].zfill(8)))
    biner = ''.join(convbiner)
    print "hasil konversi ke biner karakter pesan : "
    print ' '.join(convbiner)

    #perintah convert key ke desimal
    convkeydecimal = []
    for i in range(len(acak)):
        convkeydecimal.append(str(ord(acak[i])))
    keydecimal = ' '.join(convkeydecimal)
    #fungsi conver key ke biner
    convkeybiner = []
    for i in range(len(convkeydecimal)):
        convkeybiner.append(str(bin(int(convkeydecimal[i]))))
    binerkey = ''.join(convkeybiner)
    print "Hasil KOnversi ke biner karakter kunci :"
    print ' '.join(convkeybiner)
    binerpesan =biner.replace("b","")
    print "biner pesan : \n"+binerpesan
    binerkey =binerkey.replace("b","")
    print "key biner : \n"+binerkey
    #fungsi xor variabel pesan dan key
    ciphertext = []
    for i in range(len(binerpesan)):
        ciphertext.append(xor(int(binerpesan[i]),int(binerkey[i])))
    cipherfix =''.join(map(str,ciphertext))
    splits=[cipherfix[x:x+8] for x in range(0,len(cipherfix),8)]
    print "Hasil XOR variabel pesan dan key : \n"+str(splits)
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
    save2file = ''.join(teks)
    print "Ciphertext : \n"+''.join(teks)
    #ciphertext di simpan ke file, supaya memudahkan pada waktu dekripsi,
    #karena pada waktu ciphertext di copas hasil conversi ke binernya beda
    outfile = open('ciphertext.txt','w')
    outfile.write(save2file)
    print "Ciphertext di simpan di ciphertext.txt"
    return exit()

def main():
    print "Vernam Cipher"
    pesan = raw_input("Masukkan Pesan : ")
    print vernam_enc(pesan)
if __name__ == '__main__':
    	main()
