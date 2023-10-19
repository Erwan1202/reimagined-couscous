from projet_python_cryptage import *

def main():
    while True:
        print("Choisissez une option :")
        print("1. Chiffrement de César")
        print("2. Déchiffrement de César")
        print("3. Chiffrement Affine")
        print("4. Déchiffrement Affine")
        print("5. Chiffrement par substitution")
        print("6. Déchiffrement par substitution")
        print("7. Chiffrement en binaire")
        print("8. Déchiffrement en binaire")
        print("9. Trouver la clé de César")
        print("10. Quitter")

        choix = input("Entrez le numéro de l'option : ")

        if choix == "1":
            message = input("Entrez le message à chiffrer : ")
            decalage = int(input("Entrez le décalage : "))
            message_chiffre = crypt_cesar(message, decalage)
            print("Message chiffré : ", message_chiffre)

        elif choix == "2":
            message_chiffre = input("Entrez le message chiffré : ")
            decalage = int(input("Entrez le décalage : "))
            message_dechiffre = decrypt_cesar(message_chiffre, decalage)
            print("Message déchiffré : ", message_dechiffre)

        elif choix == "3":
            message = input("Entrez le message à chiffrer : ")
            cle_a = int(input("Entrez la clé a : "))
            cle_b = int(input("Entrez la clé b : "))
            message_chiffre = crypt_affine(message, cle_a, cle_b)
            print("Message chiffré : ", message_chiffre)

        elif choix == "4":
            message_chiffre = input("Entrez le message chiffré : ")
            cle_a = int(input("Entrez la clé a : "))
            cle_b = int(input("Entrez la clé b : "))
            message_dechiffre = decrypt_affine(message_chiffre, cle_a, cle_b)
            print("Message déchiffré : ", message_dechiffre)

        elif choix == "5":
            message = input("Entrez le message à chiffrer : ")
            message_chiffre = crypt_sub(message)
            print("Message chiffré : ", message_chiffre)

        elif choix == "6":
            message_chiffre = input("Entrez le message chiffré : ")
            message_dechiffre = decrypt_sub(message_chiffre)
            print("Message déchiffré : ", message_dechiffre)

        elif choix == "7":
            message = input("Entrez le message à chiffrer en binaire : ")
            message_chiffre = crypt_binaire(message)
            print("Message chiffré en binaire : ", message_chiffre)

        elif choix == "8":
            message_chiffre = input("Entrez le message chiffré en binaire : ")
            message_dechiffre = decrypt_binaire(message_chiffre)
            print("Message déchiffré : ", message_dechiffre)

        elif choix == "9":
            message = input("Entrez le message chiffré : ")
            mot_cle = input("Entre le message d'origine : ")
            cle = cle_cesar(mot_cle, message)
            if cle is not None:
                print(f"Clé de chiffrement de César trouvée : {cle}")
            else:
                print("La clé de chiffrement de César n'a pas été trouvée.")

        elif choix == "10":
            print("Au revoir <3")
            break

        else:
            print("Option non valide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
