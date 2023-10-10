import math
import random 

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

def crypt_affine(m):
    nv_m = ""   
    cle_a= random.randint(1, 100)
    cle_b = random.randint(1, 100)

    while math.gcd(cle_a, 94) != 1:
        cle_a = random.randint(1, 100)

    for i in m:
        if i != " ":
            nv_l = ((cle_a * (ord(i) - 32)) + cle_b) % 94
            nv_m += chr(nv_l + 32)
        else:
            nv_m += " "

    return nv_m


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
