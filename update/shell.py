import os

# Clear function


def clearfun():
    os.system('cls' if os.name == 'nt' else 'clear')

# System function


def systemfun(cmd):
    os.system(cmd)

logo = '''
|             |                   | / |                         |
| __          | __   __   ___     |/  |____    ___    o     __  |____ 
|/  \ \__/    |/  \ |__| |   |    |\  |    |  |   \   | |/ |__| |    |
|___/   /     |___/ |___ |   |    | \ |    |  |____\  | |  |___ |    |
       /                                      
'''

clearfun()
console = True
print(logo)
while console:
    command = input("> ")
    if(command == "clear"):
        clearfun()
        print(logo)
    elif(command == "syscmd"):
        auth = True
        print("")
        print("------------------------------------------------------------------")
        print("S'authentifier à la ligne de commande système")
        print("------------------------------------------------------------------")
        print("")
        while auth:
            username = input("Nom d'utilisateur: ")
            if username == "benkhaireh":
                password = input("Mot de passe: ")
                if password == "root":
                    print("")
                    print("------------------------------------------------------------------")
                    print("Bienvenu "+username+" à la ligne de commande système")
                    print("------------------------------------------------------------------")
                    print("")
                    syscmd = True
                    while syscmd:
                        sys = input(username+"@syscmd:~$ ")
                        if(sys == "exit"):
                            print("")
                            print("------------------------------------------------------------------")
                            print("Deconnexion de la ligne de commande système")
                            print("------------------------------------------------------------------")
                            print("")
                            print("------------------------------------------------------------------")
                            print("S'authentifier à la ligne de commande système")
                            print("------------------------------------------------------------------")
                            print("")
                            syscmd = False
                        elif(sys == "help"):
                            print("")
                            print("----------------------        Commande disponible")
                            print("------------------------------------------------------------------")
                            print("helpsys                       Obtenir une documentation des commandes disponible pour votre système")
                            print("help                          Obtenir une documentation des commandes disponible")
                            print("exit                          Se deconnecter à la ligne de commande système")
                            print("------------------------------------------------------------------")
                        elif(sys == "helpsys"):
                            systemfun("help")
                        else:
                            if(sys != "help"):
                                systemfun(sys)
                elif password == "help":
                    print("")
                    print("----------------------     Commande disponible")
                    print("------------------------------------------------------------------")
                    print("help                       Obtenir une documentation des commandes disponible")
                    print(
                        "logout                     Ignorer la connexion à la ligne de commande")
                    print("------------------------------------------------------------------")

                elif password == "clear":
                    clearfun()
                    print(logo)

                elif password == "logout":
                    print("")
                    print("------------------------------------------------------------------")
                    print("Ignoration de la connexion à la ligne de commande système")
                    print("------------------------------------------------------------------")
                    print("")
                    auth = False

                elif password == "":
                    print("")
                    print("------------------------------------------------------------------")
                    print("Authentification echouer à la ligne de commande système")
                    print("------------------------------------------------------------------")
                    print("")
                else:
                    print("")
                    print("------------------------------------------------------------------")
                    print("Authentification echouer à la ligne de commande système")
                    print("------------------------------------------------------------------")
                    print("")
            elif username == "help":
                print("")
                print("----------------------     Commande disponible")
                print("------------------------------------------------------------------")
                print(
                    "help                       Obtenir une documentation des commandes disponible")
                print(
                    "logout                     Ignorer la connexion à la ligne de commande")
                print("------------------------------------------------------------------")

            elif username == "clear":
                clearfun()
                print(logo)

            elif username == "logout":
                print("")
                print("------------------------------------------------------------------")
                print("Ignoration de la connexion à la ligne de commande système")
                print("------------------------------------------------------------------")
                print("")
                auth = False

            elif username == "":
                print("")
                print("------------------------------------------------------------------")
                print("Nom d'utilisateur obligatoire")
                print("")
                print("------------------------------------------------------------------")

            else:
                print("")
                print("------------------------------------------------------------------")
                print("Utilisateur introuvable: "+username)
                print("")
                print("------------------------------------------------------------------")
    elif(command == "exit"):
        print("")
        print("------------------------------------------------------------------")
        print("Deconnexion de l'application")
        print("------------------------------------------------------------------")
        print("")
        console = False
    elif command == "help":
        print("")
        print("----------------------     Commande disponible")
        print("------------------------------------------------------------------")
        print(
            "help                       Obtenir une documentation des commandes disponible")
        print("exit                       Se deconnecter de l'application")
        print("syscmd                     Se connecter à la ligne de commande système")
        print("------------------------------------------------------------------")
        print("")
    else:
        print(command+": introuvable")
