import math
import random

###############################################

def crypt_cesar(m, d):
    nv_m = ""
    for i in m:
        if type(i) == str:
            if 97<ord(i)<122:
                nv_l = (ord(i) - 97 + d) % 26 + 97
                nv_m += chr(nv_l)
            elif 65<ord(i)<90:
                nv_l = (ord(i) - 65 + d) % 26 + 65
                nv_m += chr(nv_l)
    return nv_m



def decrypt_cesar(m, d):
    nv_m = ""
    for i in m:
        if type(i) == str:
            if 97<ord(i)<122:
                nv_l = (ord(i) - 97 - d) % 26 + 97
                nv_m += chr(nv_l)
            elif 65<ord(i)<90:
                nv_l = (ord(i) - 65 - d) % 26 + 65
                nv_m += chr(nv_l)
    return nv_m



def cle_cesar(m, mc):
    mc = mc.lower()
    for i in range(26):
        nv_m = decrypt_cesar(m, i)
        if mc in nv_m.lower():
            return i

    return None

###############################################

def crypt_affine(m, cle_a, cle_b):
    nv_m = ""   

    for i in m:
        if i != " ":
            if 65 <= ord(i) <= 90:
                nv_l = ((ord(i) - 65)*cle_a)+cle_b
                nv_l %= 26
                nv_m += chr(nv_l + 65)
            elif 97 <= ord(i) <= 122:
                nv_l = ((ord(i) - 97) *cle_a)+cle_b
                nv_l %= 26
                nv_m += chr(nv_l+97)
        
        else:
            nv_m += " "
    print(nv_m)
    return nv_m

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt_affine(m, cle_a, cle_b):
    nv_m = ""
    inverse_a = mod_inverse(cle_a, 26)
    print(inverse_a)
    if inverse_a is not None:
        for i in m:
            if i != " ":
                if 97 <= ord(i) <= 122:
                    print('minuscules')
                    nv_l = ((ord(i)-97)-cle_b)*inverse_a 
                    nv_l %= 26
                    nv_m += chr(nv_l + 97)
                elif 65 <= ord(i) <= 90:
                    print('majuscules')
                    nv_l = ((ord(i)-65)-cle_b)*inverse_a
                    nv_l %= 26
                    nv_m += chr(nv_l + 65)
            else:
                nv_m += " "
        return nv_m
    else:
        return "La clé de déchiffrement n'a pas d'inverse modulaire."



#1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 
#49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99

print(decrypt_affine(crypt_affine("B b", 17,3), 17, 3)+"\n")

print(decrypt_affine(crypt_affine("QCM Javascript", 71,79), 71, 79)+"\n")

print(decrypt_affine(crypt_affine("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 17,3), 17, 3)+"\n")

print(decrypt_affine(crypt_affine("CODE", 17,3), 17, 3)+"\n")
###############################################

def new_dict(m):
    dict = {}
    for i, mot in enumerate(m):
        dict[mot] = i
    return dict

def crypt_sub(m, dict):
    mots = m.split()  
    texte_chiffre = [str(dict.get(mot, -1)) for mot in mots] 
    return ' '.join(texte_chiffre) 


def decrypt_sub(mc, dict):
    indices = mc.split() 
    m = [list(dict.keys())[list(dict.values()).index(int(idx))] for idx in indices]
    return ' '.join(m)  

###############################################

