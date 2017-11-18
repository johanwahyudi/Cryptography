#!/usr/bin/env python
from string import lowercase, uppercase
#library cuma untuk besar kecil huruf saja

#fungsi enkripsi caesar
def caesar_en(text, key):
    result = []
    for c in text:
        if c in lowercase:
            enkripsi = lowercase.index(c)
            enkripsi = (enkripsi + key) % 26
            result.append(lowercase[enkripsi])
            print result
        elif c in uppercase:
            enkripsi = uppercase.index(c)
            enkripsi = (enkripsi + key) % 26
            result.append(uppercase[enkripsi])
        else:
            result.append(c)
    return "".join(result)
#fungsi transposition
def permutasi(key, pesan, key02):
    ciphertext = [''+","]*key
    for kolom in range(key):
        c = kolom

        while c < len(pesan):
            ciphertext[kolom] += pesan[c]
            c += key
            print ciphertext
            
    data = ''.join(ciphertext)
    #split data, di buat list
    pecah = data.split(',')
    print pecah
    #fungsi acak kolom :
    key1 = key02
    a = []
    l = list(map(int,key1))
    for i in range(0,len(l)):
       a.append(pecah[l[i]+1])
    ciphertext02 =''.join(a)
    
    datafix = data.replace(",","")
    print "kunci acak kolom :"+key1
    print "Ciphertext sebelum di acak : "+datafix
    print "Ciphertext Setelah di acak kolomnya : "
    return ciphertext02
def main():
    pesan = raw_input("masukkan pesan :")
    rot = input("masukkan kunci ROT :")
    print "hasil Enkripsi dengan ROT "+str(rot)+" :"
    print caesar_en(pesan,rot)
    pesan1 = caesar_en(pesan,rot)
    key = input("masukkan jumlah kolom :")
# kunci acak kolom di mulai dari nol, misal jumlah kolom 3, maka range
#untuk kunci acak kolom adalah 0-2, akan error apabila melebihi angka itu
    key02 = raw_input("masukkan kunci acak kolom : ")
    print "pesan Asli (plaintext) : "+pesan
    print "hasil Enkripsi dengan ROT "+str(rot)+" :"
    print caesar_en(pesan,rot)
    print permutasi(key, pesan1, key02)

if __name__ == '__main__':
    main()
