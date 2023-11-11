from qcm import build_questionnaire
import random

questions = []


def import_file():
    """Permet d'importer le QCM

    Cette Fonction importe le QCM desiré

    Args:
        input: Filename un nom de fichier

    Returns:
            Le QCM desiré

    """
    filename = input("Choisir votre fichier:")
    questions = build_questionnaire(filename)
    print(
        "REPONDEZ UNIQUEMENT PAR LE NUMERO DE LA QUESTION EST NON LA REPONSE !\nENTRER DEUX FOIS LA MÊME RÉPONSE VOU PÉNALISERA !"
    )
    return questions


def choix_cotation():
    """Permet de choisir un choix de Cotation

    Cette fontion permet de choisir une méthode de cotation parmi les suivantes: 1| Cool, 2| Sévère, 3| Anti-Hasard, 4| Toutes

    Args:
        Un Entier entre 1 et 4

    Returns:
        "C", étant la méthode de cotation choisie

    """

    print(
        "Choisissez votre méthode de cotation:\n1| Cool.\n2| Sévère.\n3| Anti-Hasard.\n4| Toutes."
    )  # Affiche les diffférents types de cotations
    cotation = str(input("Entrez votre méthode de cotation:"))
    x = cotation.lower()

    if x == "cool" or x == "1":
        list_answers = []
        count_cool = 0
        for i in range(len(questions)):
            random.shuffle(questions[i][1])
            print("-----", "\t", str(i + 1), "|", questions[i][0], "\t", "-----")
            compte = 0
            liste = []
            for l in range(len(questions[i][1])):
                print("\n", "\t", str(l + 1), "|", questions[i][1][l][0])
                if questions[i][1][l][1] is True:
                    compte += 1
            for z in range(compte):
                answer = int(input("Entrez le n° de votre réponse:"))
                list_answers.append(answer)
                print(liste)
                if answer in liste:
                    print("Vous avez déja entré cette réponse dommage...")
                elif questions[i][1][answer - 1][1] is True:
                    count_cool += 1
                elif questions[i][1][answer - 1][1] is False:
                    count_cool -= 1
                liste.append(answer)
        print(count_cool)
    elif x == "severe" or x == "sévere" or x == "sevère" or x == "sévère" or x == "2":
        list_answers = []
        count_svr = 0
        for i in range(len(questions)):
            random.shuffle(questions[i][1])
            print("-----", "\t", str(i + 1), "|", questions[i][0], "\t", "-----")
            compte = 0
            liste = []
            for l in range(len(questions[i][1])):
                print("\n", "\t", str(l + 1), "|", questions[i][1][l][0])
                if questions[i][1][l][1] is True:
                    compte += 1
            for z in range(compte):
                answer = int(input("Entrez le n° de votre réponse:"))
                list_answers.append(answer)
                print(liste)
                if answer in liste:
                    print("Vous avez déja entré cette réponse dommage...")
                elif questions[i][1][answer - 1][1] is True:
                    count_svr += 1
                elif questions[i][1][answer - 1][1] is False:
                    count_svr -= 1
                liste.append(answer)
        print(count_svr)
    elif x == "toutes" or x == "4":
        list_answers = []
        count_cool = 0
        count_svr = 0
        for i in range(len(questions)):
            random.shuffle(questions[i][1])
            print("-----", "\t", str(i + 1), "|", questions[i][0], "\t", "-----")
            compte = 0
            liste = []
            for l in range(len(questions[i][1])):
                print("\n", "\t", str(l + 1), "|", questions[i][1][l][0])
                if questions[i][1][l][1] is True:
                    compte += 1
            for z in range(compte):
                answer = int(input("Entrez le n° de votre réponse:"))
                list_answers.append(answer)
                print(liste)
                if answer in liste:
                    print("Vous avez déja entré cette réponse dommage...")
                if questions[i][1][answer - 1][1] is True:
                    count_cool += 1
                    count_svr += 1
                else:
                    count_svr -= 1
                liste.append(answer)
        print(count_cool)
        print(count_svr)


# On sait juste l'afficher


def main():
    # 1) Integrer le QCM.
    import_file()
    # 2 ) Choix de cotation.
    choix_cotation()


if __name__ == "__main__":
    main()
