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
    filename = input("Choose file:")
    questions = qcm.build_questionnaire(filename) #sérieuc ça marche juste comme ça ???????
    return questions
    

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
    x = cotation.lower() #Force l'input à être en minuscule pour éviter les erreurs 
    if x == "cool" or "1":
        cotation_cool()
    elif x == "severe" or "sévere" or "sevère" or "sévère" or "2":
        cotation_severe()
    elif x == "antihasard" or "anti-hasard" or "anti hasard" or "anti_hasard" or "3":
        cotation_antihasard()
    elif x == "toutes" or "4":
        cotation_tout()

# Besoin d'un return pour savoir au niveau du feedback quel cotation on a choisi ? 
               

def show_qr_shuffled():
    """Permet d'afficher les questions

    Cette fonction permet d'afficher les questions et les réponses possibles du QCM les réponses sont disposées aléatoirement

    Args:
        Questions 
        Réponses
    Return:
            Les questions et les réponses possibles
    
    """ 
    for i in range(len(questions)):
    print(questions[i][0])
    for l in range(len(questions[0][1])):
        print(l + 1, "|", questions[i][1][l][0])
        # naffiche que 3 questions 
    correction()
    

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
        count_cool == 0
        for i in range(len(questions):
            if input == list[i]:
                count_cool += 1
    def correction_severe():
        count_severe == 0
        for i in range(len(questions)
            if input == list[i]:
                count_severe += 1
            else:
                count_severe -= 1
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
    for i in range(len(questions)):
    print(questions[i][0])
    for l in range(len(questions[0][1])):
        print(questions[i][1][l][2])


def main():
    
# 1) Integrer le QCM.
    import_file()
# 2 ) Choix de cotation.
    choix_cotation()
# 4 ) Afficher les questions du QCM aléatoires
    show_qr_shuffled()
# 5) Correction du QCM.
    correction()
# 6 )  Sortie du Feedback avec les cotations.
    feedback()
#if __name__ == "__main__":
main()
