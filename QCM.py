from qcm import build_questionnaire
import random

questions = []  # on initialise la liste de question


def import_file():
    """Permet d'importer le QCM

    Cette Fonction importe le QCM desiré

    Args:
        input: Filename un nom de fichier

    Returns:
            Le QCM desiré

    """
    while (
        True
    ):  # ici  je rajoute une while true si jamais l user se trompe lors qui choisit son fichier il a autant de chance qu il veut tant que son fichier n'a pas été trouvé
        try:
            filename = input("Choisir votre fichier:")
            questions = build_questionnaire(filename)
            print(
                "\033[91m"
                + "1|REPONDEZ UNIQUEMENT PAR LE NUMERO DE LA QUESTION ET NON LA REPONSE !\n2|ENTRER DEUX FOIS LA MÊME RÉPONSE VOUS PÉNALISERA OU PAS SELON LE CHOIX DE COTATION !\n PS: Vous êtes obligé de répondre autant de fois que le nombre de bonne réponses"
                + "\033[0m"
            )
            return questions
            break  # Sortir de la boucle si le fichier est trouvé avec succès
        except FileNotFoundError:
            print("Le fichier n'a pas été trouvé. Veuillez réessayer.")


def opti_quest(questions):
    """Permet de choisir un choix de Cotation

    Cette fontion permet de choisir une méthode de cotation parmi les suivantes: 1| Cool, 2| Sévère, 3| Anti-Hasard, 4| Toutes

    Args:
        Un Entier entre 1 et 4

    Returns:
        "C", étant la méthode de cotation choisie

    """
    t = input("Tapez j'accepte ou 1 pour accepter les règles du QCM:")
    y = t.lower()
    if y == "j'accepte" or y == "jaccepte" or y == "j accepte" or y == "1":
        print(
            "Choisissez votre méthode de cotation:\n1| Cool.\n2| Sévère.\n3| Anti-Hasard.\n4| Toutes."
        )  # Affiche les diffférents types de cotations
        cotation = input("Entrez votre méthode de cotation:")
        x = cotation.lower()
        # Initialisation des listes et des count
        list_feedback = []
        list_nbre_qst = []
        list_true = []
        liste_true2 = []
        list_false = []
        count_cool = 0
        count_svr = 0
        count_noluck = 0
        count_question = -1
        count_t = 0
        # Boucle de longueur égale au nombre de questions
        for i in range(len(questions)):
            random.shuffle(questions[i][1])
            print("-----", "\t", str(i + 1), "|", questions[i][0], "\t", "-----")
            compte = 0
            count_true = 0
            liste = []
            count_question += 1
            compte_false = 0
            # Boucle de longueur égale au nombre de réponses
            for l in range(len(questions[i][1])):
                print("\n", "\t", str(l + 1), "|", questions[i][1][l][0])
                if questions[i][1][l][1] is True:
                    compte += 1
                    list_true.append(count_true)
                    count_true += 1
                    count_t += 1
                else:
                    count_true += 1
                if questions[i][1][l][1] is False:
                    compte_false += 1
            list_false.append(compte_false)
            liste_true2.append(compte)

            for z in range(compte):
                answer = int(input("Entrez le n° de votre réponse:"))
                if answer in liste:
                    print("Vous avez déja entré cette réponse dommage...")
                elif questions[i][1][answer - 1][1] is True:
                    count_cool += 1
                    count_svr += 1
                    count_noluck += 1
                else:
                    count_svr -= 1
                    count_noluck -= liste_true2[i] / list_false[i]
                    list_feedback.append(answer)
                    list_nbre_qst.append(count_question)
                liste.append(answer)

        if x == "cool" or x == "1":
            print(
                "Selon la cotation cool votre notes est de:", count_cool, "/", count_t
            )

        elif (
            x == "severe" or x == "sévere" or x == "sevère" or x == "sévère" or x == "2"
        ):
            print(
                "Selon la cotation sévère votre notes est de:", count_svr, "/", count_t
            )

        elif x == "anti-hasard" or x == "3":
            print(
                "Selon la correction ANTI-TRICHE votre note est de:",
                count_noluck,
                "/",
                count_t,
            )

        elif x == "toutes" or x == "4":
            print(
                "Selon la cotation COOL votre notes est de:", count_cool, "/", count_t
            )
            print(
                "Selon la cotation SEVERE votre notes est de:", count_svr, "/", count_t
            )
            print(
                "Selon la correction ANTI-TRICHE votre note est de:",
                count_noluck,
                "/",
                count_t,
            )
        for t in range(len(list_feedback)):
            print("\n")
            print(
                "Vous vous êtes trompés à la question:\n",
                questions[list_nbre_qst[t]][0],
                "\t",
                "Vous avez entré",
                questions[list_nbre_qst[t]][1][list_feedback[t] - 1][0],
                "|",
                questions[list_nbre_qst[t]][1][list_feedback[t] - 1][2],
            )
    else:
        print("Veuillez accepter les règles du QCM pour répondre aux questions")


def main():
    # 1) Integrer le QCM qui est direcement faites lors du lancement de choix_cotation(questions)
    questions = import_file()
    # 2 ) Choix de cotation.
    opti_quest(questions)


if __name__ == "__main__":  # excutation du code
    main()
