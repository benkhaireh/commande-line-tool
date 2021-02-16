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
                  " à la ligne de command")
            print("")
            console = True

            while console:
                command = input("> ")

                if command == "help":
                    print("")
                    print("-------------- command disponible")
                    print("")
                    print(
                        "cmdsys                 --------------      Obtenir une documentation des commands disponible")
                    print(
                        "help                 --------------      Obtenir une documentation des commands disponible")
                    print(
                        "logout               --------------      Se deconnecter de la ligne de command")
                    print(
                        "exit                 --------------      Se deconnecter de l'application")
                    print("")

                elif command == "clear":
                    clear()
                elif command == "cmdsys":
                    systemcmd('help')

                elif command == "logout":
                    print("")
                    print("-------------- Deconnexion de la ligne de command.")
                    print("")
                    console = False

                elif command == "exit":
                    print("")
                    print("-------------- Deconnexion de la ligne de command.")
                    print("-------------- Deconnexion de l'application")
                    print("")
                    auth = False
                    console = False

                elif command == "":
                    continue

                else:
                    print("")
                    print("-------------- command introuvable: "+command)
                    print("")

        elif password == "help":
            print("")
            print("-------------- command disponible")
            print("")
            print(
                "help                  --------------      Obtenir une documentation des commands disponible")
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
        print("-------------- command disponible")
        print("")
        print("help                  --------------      Obtenir une documentation des commands disponible")
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
