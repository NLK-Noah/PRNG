import qcm
import random

def import_file(x):
    """Permet d'importer le QCM

    Cette Fonction importe le QCM desiré 

    Args:
        input: Filename un nom de fichier 

    Returns:
            Le QCM desiré

    """
    
    filename = input("Choisir votre fichier:")
    questions = qcm.build_questionnaire(filename)
    print("REPONDEZ UNIQUEMENT PAR LE NUMERO DE LA QUESTION EST NON LA REPONSE !")
    

def choix_cotation():
    """Permet de choisir un choix de Cotation

    Cette fontion permet de choisir une méthode de cotation parmi les suivantes: 1| Cool, 2| Sévère, 3| Anti-Hasard, 4| Toutes 

    Args:
        Un Entier entre 1 et 4 

    Returns:
        "C", étant la méthode de cotation choisie

    """
    print("Choisissez votre méthode de cotation:\n1| Cool.\n2| Sévère.\n3| Anti-Hasard.\n4| Toutes.") #Affiche les diffférents types de cotations
    cotation = input("Entrez votre méthode de cotation:")
    x = cotation.lower() 
    if x == "cool" or "1":
        correction_cool()
    elif x == "severe" or "sévere" or "sevère" or "sévère" or "2":
        correction_severe()
    elif x == "antihasard" or "anti-hasard" or "anti hasard" or "anti_hasard" or "3":
        correction_antihasard()
    elif x == "toutes" or "4":
        correction_tout()
    

# Besoin d'un return pour savoir au niveau du feedback quel cotation on a choisi ? 
               

def show_qr_shuffle():
    """Permet d'afficher les questions

    Cette fonction permet d'afficher les questions et les réponses possibles du QCM les réponses sont disposées aléatoirement

    Args:
        Questions 
        Réponses
    Return:
            Les questions et les réponses possibles
    
    """ 
    list_answers = []
    count = 0
    # Boucle Qui Affiche les Questions et Shuffle leurs réponses
    for i in range(len(questions)):
        random.shuffle(questions[i][1])
        print("-----", "\t", str(i + 1), "|", questions[i][0], "\t", "-----")
        compte = 0
        liste = []
        # Boucle Qui Affiche les réponses et permet de savoir combien il y à de réponses correctes 
        for l in range(len(questions[i][1])):
            print("\n", "\t", str(l + 1), "|", questions[i][1][l][0])
            if questions[i][1][l][1] is True:
                compte += 1
        # Boucle qui permet de répondre autant de fois qu'il y a de réponses correctes
        for z in range(compte):
            answer = int(input("Entrez le n° de votre réponse:"))
            list_answers.append(answer)
            print(liste)
            if answer in liste:
                print("Vous avez déja entré cette réponse dommage...")
            elif questions[i][1][answer - 1][1] is True:
                count += 1
            else:
                choix_cotation()
            liste.append(answer)




    

def correction():
    """Permet d'avoir la cote reçue sur le QCM 
    
    Cette fonction permet de calculer le nombres de points obtenu par l'utilisateur selon son choix de cotatiion 

    Args:
        les réponses de l'utilisateur lors du QCM 
        les réponses correctes du QCM 
        les méthodes de correction 

    Return:
        les points obtenus par l'utilisateur lors du QCM selon son choix de cotation 
        
    """
    def correction_cool():
        count += 0
    def correction_severe():
        count -= 1
    def correction_anti_hasard():
         count_noluck == 0

    def correction_tout():
        correction_cool()
        print("Cotation 'Cool':",count_cool)
        correction_severe()
        print("Cotation 'Sévère':",count_severe)
        correction_anti_hasard()
        print("Cotation 'Anti_Hasard':",count_noluck)

    feedback()

def feedback():
    """Permet d'avoir un feedback

    Cette fonction permet d'afficher la cote selon la méthode choisie et des feedback sur les éventuelles erreurs

    Args:
        récupère les feedback dans le fichier qcm.py
        les  réponses aux questions et si y en a un qui en à bon et qui a un feedback 

    Returns:
        return le feedback de la question mauvaise 
            
    """
    print("")
    print("Session Feedback:")
    for i in range(len(questions)):
        print(str(i + 1), questions[i][0])
    for l in range(len(questions[i][1])):
        print(questions[i][1][l][2])
#On sait juste l'afficher

def main():
    
# 1) Integrer le QCM.
    import_file()
# 2 ) Choix de cotation.
    choix_cotation()
# 4 ) Afficher les questions du QCM aléatoires
    show_qr_shuffle()
# 5) Correction du QCM.
    correction()
# 6 )  Sortie du Feedback avec les cotations.
    feedback()
#if __name__ == "__main__":
main()
