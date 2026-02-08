def create_inscription(D):
    user = {"nom" : "",
            "prenom" : "",
            "addresse" : "",
            "mail": "",
            "mdp": ""}
    print("Veillez entrer  vos informations d'inscription : \n")
    user["nom"] = str(input("Veuillez entrer votre nom : \n"))
    user["prenom"]  = str(input("Veuillez entrer votre prenom : \n"))
    user["addresse"]  = str(input("Veuillez entrer votre adresse : \n"))
    mail = input("Veuillez renseigner votre adresse mail :\n")
    while mail_existe(D, mail):
        mail = input(f"L'adresse e-mail {mail} est déjà utilisée dans notre système, veuillez changer :\n")
    user["mail"] = mail
    mdp = str(input("Veuillez définir un mot de passe : \n"))
    mdptemp = str(input("Confirmation du mot de passe : \n"))
    while mdp != mdptemp:
        mdptemp = str(input("Mot de passe incorrect, veuillez réessayer : \n"))
    user["mdp"] = mdp
    if not D:
        D[0] = user
    else:
        D[max(D.keys())+1] = user
    print("Inscription réussie !\n")

def connexion(D):
    print("Veillez entrer  vos informations de connexion : \n")
    mail = str(input("Veuillez renseigner votre adresse mail : \n"))
    mdp = str(input("Veuillez renseigner votre mot de passe : \n"))
    for user in D.values():
        if user["mail"] == mail:
            if user["mdp"] == mdp:
                print("Connexion réussie !")
                print(f"Bienvenue {user['prenom']} {user['nom']}")
                return True
            else:
                print("Mot de passe incorrect.")
        else:
            print("Mail inconnu.")
    return False


def mail_existe(D, mail):
    for user in D.values():
        if user["mail"] == mail:
            return True
    return False

users = {}
choix =""
while choix != "QUIT":
    print("Bonjour veuillez vous identendifier/vous inscrire\n")
    print("1.S'inscrire --- 2.Se connecter\n")
    choix = input("Votre choix ")
    match choix:
        case "1":
            create_inscription(users)
        case "2":
            if connexion(users):
                break

        case _:
            print("Choix invalide")