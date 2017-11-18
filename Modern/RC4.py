##!/usr/bin/env python 
""""Johan Wahyudi""""
def rc4(data, key,):
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)

def main():
    print " RC4 Encryption"
    data = raw_input("Input Message : ")
    key = raw_input("Input Key : ")
    encrypt = rc4(data,key)
    print "Encrypt Message : " + encrypt
    print "Decrypt Message : " + rc4(encrypt,key)
if __name__ == '__main__':
    	main()