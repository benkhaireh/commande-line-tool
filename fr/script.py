from os import system, name
# -----------------------------------------
# Les fonctions

# fonction clear

def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

# fonction système mac & linux

def systemcmd(elem):
    system(elem)


# -----------------------------------------
clear()
print("-------------- Authentification")
print("")
auth = True
# -----------------------------------------
while auth:
    username = input("Nom d'utilisateur: ")
    if username == "benkhaireh":
        password = input("Mot de passe: ")
        
        if password == "root":
            print("")
            print("-------------- Bienvenu "+username +
                  " à la ligne de commande")
            print("")
            console = True

            while console:
                commande = input("> ")

                if commande == "help":
                    print("")
                    print("-------------- Commande disponible")
                    print("")
                    print(
                        "cmdsys                 --------------      Obtenir une documentation des commandes disponible")
                    print(
                        "help                 --------------      Obtenir une documentation des commandes disponible")
                    print(
                        "logout               --------------      Se deconnecter de la ligne de commande")
                    print(
                        "exit                 --------------      Se deconnecter de l'application")
                    print("")

                elif commande == "clear":
                    clear()
                elif commande == "cmdsys":
                    systemcmd('help')

                elif commande == "logout":
                    print("")
                    print("-------------- Deconnexion de la ligne de commande.")
                    print("")
                    console = False

                elif commande == "exit":
                    print("")
                    print("-------------- Deconnexion de la ligne de commande.")
                    print("-------------- Deconnexion de l'application")
                    print("")
                    auth = False
                    console = False

                elif commande == "":
                    continue

                else:
                    print("")
                    print("-------------- Commande introuvable: "+commande)
                    print("")

        elif password == "help":
            print("")
            print("-------------- Commande disponible")
            print("")
            print(
                "help                  --------------      Obtenir une documentation des commandes disponible")
            print(
                "logout                --------------      Se deconnecter de l'application")
            print("")

        elif password == "clear":
            clear()

        elif password == "logout":
            print("")
            print("-------------- Deconnexion de l'application")
            print("")
            auth = False

        elif password == "":
            print("")
            print("-------------- Authentification echouer")
            print("")

        else:
            print("")
            print("-------------- Authentification echouer")
            print("")

    elif username == "help":
        print("")
        print("-------------- Commande disponible")
        print("")
        print("help                  --------------      Obtenir une documentation des commandes disponible")
        print("logout                --------------      Se deconnecter de l'application")
        print("")

    elif username == "clear":
        clear()

    elif username == "logout":
        print("")
        print("-------------- Deconnexion de l'application")
        print("")
        auth = False

    elif username == "":
        print("")
        print("-------------- Nom d'utilisateur obligatoire")
        print("")

    else:
        print("")
        print("-------------- Utilisateur introuvable: "+username)
        print("")
