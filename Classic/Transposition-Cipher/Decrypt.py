#!/usr/bin/env python
import math
from string import ascii_lowercase, ascii_uppercase
def caesar_dec(ciphertext, key_dec):
    hasil = []
    for d in ciphertext:
        if d in ascii_lowercase:
            dekripsi = ascii_lowercase.index(d)
            dekripsi = (dekripsi - key_dec) % 26
            hasil.append(ascii_lowercase[dekripsi])
        elif d in ascii_uppercase:
            dekripsi = ascii_uppercase.index(d)
            dekripsi = (dekripsi - key_dec) % 26
            hasil.append(ascii_uppercase[dekripsi])
        else:
            hasil.append(d)
    return "".join(hasil)

def decryptmessage(key, pesan):
    numofkolom = math.ceil(len(pesan)/key)
    numofbaris = key
    numofshadedboxes = (numofkolom * numofbaris) - len(pesan)
    plaintext = ['']*numofkolom

    col = 0
    row = 0
    for i in pesan:
        plaintext[col] += i
        col += 1

        if (col ==numofkolom) or (col == numofkolom - 1 and row >= numofbaris - numofshadedboxes):
            col = 0
            row += 1
    return ''.join(plaintext)

def main ():
    pesan = input("Masukkan ciphertext sebelum di acak kolom :")
    jumlahkolom = int(input("masukkan jumlah kolom :"))
    print(decryptmessage(jumlahkolom,pesan))
    ciphertext = decryptmessage(jumlahkolom,pesan)
    keyrot = int(input("masukkan key ROT :"))
    print("Plaintext :"+caesar_dec(ciphertext,keyrot))
if __name__ == '__main__':
    main()
#program decrypt acak kolom, hasil output belum sama dng yg diingikan
"""import math
def bismillah(key,pesan,jumlahkolom):
    bagi = math.ceil(len(pesan)/jumlahkolom)
    sisip =','.join(pesan[i:i+bagi] for i in range(0, len(pesan),bagi))
    print(sisip)
    pecahdata = sisip.split(',')
    pecahkey = list(map(int,key))
    a =[]
    for i in range (len(key)):
        a.append(pecahdata[pecahkey[i]])
    data1 = ''.join(a)
    bagi1 = math.ceil(len(data1)/jumlahkolom)
    sisip1 =','.join(data1[i:i+bagi1] for i in range(0, len(data1),bagi1))
    pecahdata1 =sisip1.split(',')
    b = []
    for i in range (len(key)):
        b.append(pecahdata1[pecahkey[i]])
    data2 = ''.join(b)
    print(data1)
    return data2
def main():
    pesan = input("masukkan pesan :")
    jumlahkolom = int(input("jumlah kolom :"))
    key = input("masukkan key :")
    print(bismillah(key,pesan,jumlahkolom))
if __name__ == '__main__':
    main()
"""
