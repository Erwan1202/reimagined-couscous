# reimagined-couscous

                                            Chiffrement et déchiffrement en Python
Ce projet Python propose un ensemble de fonctions pour chiffrer et déchiffrer des messages en utilisant différents types de chiffrement. Il inclut le chiffrement de César, le chiffrement affine, le chiffrement par substitution, et le chiffrement binaire.

        Table des matières:
1.Introduction

2.Fonctionnalités

3.Comment utiliser

4.Explication des fonctions



        Introduction:

Ce projet est destiné à être utilisé comme une boîte à outils de chiffrement et de déchiffrement pour protéger ou décoder des messages. Les différentes fonctions fournies peuvent être utilisées pour explorer diverses méthodes de chiffrement.



        Fonctionnalités:

Ce projet offre les fonctionnalités suivantes :

Chiffrement et déchiffrement de César avec un décalage donné.
Chiffrement et déchiffrement affine avec les clés a et b.
Chiffrement et déchiffrement par substitution à l'aide d'un dictionnaire.
Chiffrement et déchiffrement en binaire.
Trouvé la clé utilisée pour chiffrer un message en utilisant la chiffrement César.



        Comment utiliser:
        
1.Assurez-vous d'avoir Python installé sur votre système.

2.Clonez ce dépôt ou téléchargez les fichiers du projet sur votre ordinateur.

3.Exécutez le fichier Python main.py pour utiliser les différentes fonctions de chiffrement et de déchiffrement.

4.Suivez les instructions fournies dans le terminal pour choisir l'option de chiffrement ou de déchiffrement, puis saisissez les paramètres requis.



        Explications des fonctions:

Les fonctions `crypt_cesar`, `decrypt_cesar`, et `cle_cesar` sont des fonctions qui implémentent l'algorithme de chiffrement de César. L'algorithme de chiffrement de César est une méthode de chiffrement par substitution monoalphabétique qui consiste à remplacer chaque lettre d'un texte clair par une lettre à distance fixe, toujours du même côté, dans l'ordre alphabétique. La distance fixe est appelée la clé de chiffrement. La fonction `crypt_cesar` prend en entrée un message clair `m` et une clé de chiffrement `d`, et renvoie le message chiffré correspondant. La fonction `decrypt_cesar` prend en entrée un message chiffré `m` et une clé de déchiffrement `d`, et renvoie le message déchiffré correspondant. La fonction `cle_cesar` prend en entrée un message clair `m` et un mot-clé `mc`, et renvoie la clé de chiffrement correspondante.

La fonction `crypt_affine` est une fonction qui implémente l'algorithme de chiffrement affine. L'algorithme de chiffrement affine est une méthode de chiffrement par substitution monoalphabétique qui consiste à remplacer chaque lettre d'un texte clair par une lettre obtenue à partir d'une fonction affine. La fonction affine est définie par deux paramètres : la clé de chiffrement `cle_a` et le décalage `cle_b`. La fonction `crypt_affine` prend en entrée un message clair `m`, une clé de chiffrement `cle_a`, et un décalage `cle_b`, et renvoie le message chiffré correspondant.

La fonction `mod_inverse` est une fonction qui calcule l'inverse modulaire d'un nombre entier modulo un autre nombre entier. L'inverse modulaire d'un nombre entier a modulo m est un nombre entier b tel que a * b ≡ 1 (mod m). Si l'inverse modulaire existe, il est unique modulo m. La fonction `mod_inverse` prend en entrée deux nombres entiers a et m, et renvoie l'inverse modulaire correspondant s'il existe, ou None sinon.

La fonction `decrypt_affine` est une fonction qui implémente l'algorithme de déchiffrement affine. L'algorithme de déchiffrement affine est une méthode de déchiffrement par substitution monoalphabétique qui consiste à remplacer chaque lettre d'un texte chiffré par une lettre obtenue à partir d'une fonction affine. La fonction affine est définie par deux paramètres : la clé de chiffrement `cle_a` et le décalage `cle_b`. La fonction `decrypt_affine` prend en entrée un message chiffré `m`, une clé de chiffrement `cle_a`, et un décalage `cle_b`, et renvoie le message déchiffré correspondant.

La fonction `crypt_sub` est une fonction qui implémente l'algorithme de chiffrement par substitution. L'algorithme de chiffrement par substitution est une méthode de chiffrement par substitution monoalphabétique qui consiste à remplacer chaque lettre d'un texte clair par une autre lettre, selon une table de correspondance prédéfinie. La table de correspondance est appelée le dictionnaire. La fonction `crypt_sub` prend en entrée un message clair `m`, et renvoie le message chiffré correspondant.

La fonction `decrypt_sub` est une fonction qui implémente l'algorithme de déchiffrement par substitution. L'algorithme de déchiffrement par substitution est une méthode de déchiffrement par substitution monoalphabétique qui consiste à remplacer chaque lettre d'un texte chiffré par la lettre correspondante dans la table de correspondance prédéfinie. La fonction `decrypt_sub` prend en entrée un message chiffré `mc`, et renvoie le message déchiffré correspondant.

La fonction `new_dict` est une fonction qui permet de créer un dictionnaire. Le dictionnaire est créé en demandant à l'utilisateur d'entrer la taille du dictionnaire, puis en demandant à l'utilisateur d'entrer chaque mot du dictionnaire. Le dictionnaire est ensuite affiché à l'écran et renvoyé.

La fonction `crypt_binaire` est une fonction qui implémente l'algorithme de chiffrement binaire. L'algorithme de chiffrement binaire est une méthode de chiffrement qui consiste à remplacer chaque lettre d'un texte clair par sa représentation binaire. La fonction `crypt_binaire` prend en entrée un message clair `m`, et renvoie le message chiffré correspondant.

La fonction `decrypt_binaire` est une fonction qui implémente l'algorithme de déchiffrement binaire. L'algorithme de déchiffrement binaire est une méthode de déchiffrement qui consiste à remplacer chaque groupe de 8 bits d'un texte chiffré par la lettre correspondante dans le code ASCII. La fonction `decrypt_binaire` prend en entrée un message chiffré `m`, et renvoie le message déchiffré correspondant.

