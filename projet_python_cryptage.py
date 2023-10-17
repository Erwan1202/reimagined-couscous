
###############################################

# Fonction de chiffrement de César
def crypt_cesar(m, d):
    nv_m = ""
    for i in m:
        print("i="+i)
        if i != " ":
            if 97 <= ord(i) <= 122:  # Vérifie si la lettre est minuscule
                nv_l = (ord(i) - 97 + d) % 26
                nv_m += chr(nv_l + 97)
            elif 65 <= ord(i) <= 90:  # Vérifie si la lettre est majuscule
                nv_l = (ord(i) - 65 + d) % 26
                nv_m += chr(nv_l + 65)
        else:
            nv_m += " "
        print(nv_m)
    return nv_m

# Fonction de déchiffrement de César
def decrypt_cesar(m, d):
    nv_m = ""
    for i in m:
        if i != " ":
            if 97 <= ord(i) <= 122:
                nv_l = (ord(i) - 97 - d) % 26
                nv_m += chr(nv_l + 97)
            elif 65 <= ord(i) <= 90:
                nv_l = (ord(i) - 65 - d) % 26
                nv_m += chr(nv_l + 65)
        else:
            nv_m += " "
    return nv_m

# Fonction pour trouver la clé de César
def cle_cesar(m, mc):
    mc = mc.lower()
    for i in range(26):
        nv_m = decrypt_cesar(m, i)
        if mc in nv_m.lower():
            return i
    return None

###############################################

# Fonction de chiffrement affine
def crypt_affine(m, cle_a, cle_b):
    nv_m = ""
    for i in m:
        if i != " ":
            if 65 <= ord(i) <= 90:  # Vérifie si la lettre est majuscule
                nv_l = ((ord(i) - 65) * cle_a) + cle_b
                nv_l %= 26
                nv_m += chr(nv_l + 65)
            elif 97 <= ord(i) <= 122:  # Vérifie si la lettre est minuscule
                nv_l = ((ord(i) - 97) * cle_a) + cle_b
                nv_l %= 26
                nv_m += chr(nv_l + 97)
        else:
            nv_m += " "
    return nv_m

# Fonction de calcul de l'inverse modulaire
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Fonction de déchiffrement affine
def decrypt_affine(m, cle_a, cle_b):
    nv_m = ""
    inverse_a = mod_inverse(cle_a, 26)
    if inverse_a is not None:
        for i in m:
            if i != " ":
                if 97 <= ord(i) <= 122:
                    nv_l = ((ord(i) - 97 - cle_b) * inverse_a) % 26
                    nv_m += chr(nv_l + 97)
                elif 65 <= ord(i) <= 90:
                    nv_l = ((ord(i) - 65 - cle_b) * inverse_a) % 26
                    nv_m += chr(nv_l + 65)
            else:
                nv_m += " "
        return nv_m
    else:
        return "La clé de déchiffrement n'a pas d'inverse modulaire."

###############################################

# Fonction pour créer un dictionnaire
def new_dict(m):
    dict = {}
    for i, mot in enumerate(m):
        dict[mot] = i
    return dict

# Fonction de chiffrement par substitution
def crypt_sub(m, dict):
    mots = m.split()
    texte_chiffre = [str(dict.get(mot, -1)) for mot in mots]
    return ' '.join(texte_chiffre)

# Fonction de déchiffrement par substitution
def decrypt_sub(mc, dict):
    indices = mc.split()
    m = [list(dict.keys())[list(dict.values()).index(int(idx))] for idx in indices]
    return ' '.join(m)

###############################################

# Fonction de chiffrement binaire
def crypt_binaire(m):
    def lettre_en_binaire(l):
        b = bin(ord(l))[2:]
        return '0' * (8 - len(b)) + b

    nv_m = ""
    for i in m:
        if i != ' ':
            nv_m += lettre_en_binaire(i) + ' '
        else:
            nv_m += ' '
    return nv_m

# Fonction de déchiffrement binaire
def decrypt_binaire(m):
    def binaire_en_lettre(b):
        l = chr(int(b, 2))
        return l

    nv_m = ""
    binaire_temp = ""

    for i in m:
        if i == ' ':
            if binaire_temp:
                l = binaire_en_lettre(binaire_temp)
                nv_m += l
                binaire_temp = ""
            else:
                nv_m += ' '
        else:
            binaire_temp += i
    return nv_m


