import qcm

def import_file(x):
    """Permet d'importer le QCM

    Cette Fonction importe le QCM desiré 

    Args:
        input: Filename un nom de fichier 

    Returns:
            Le QCM desiré

    
    """
    filename = input("chosse file:")
    questions = qcm.build_questionnaire(filename)
    

def choix_cotation():
    """Permet de choisir un choix de Cotation

    Cette fontion permet de choisir une méthode de cotation parmi les suivantes: 1| Cool, 2| Sévère, 3| Anti-Hasard, 4| Toutes 

    Args:
        Un Entier entre 1 et 4 

    Returns:
            "C", étant la méthode de cotation choisie
    """


def main():
    
# 1) Integrer le QCM.
    import_file()


# 2 ) Choix de cotation:
        choix_cotation()

    

# 3 ) Shuffle QCM.


# 4 ) Afficher les questions du QCM


# 5) Correction du QCM.


# 6 )  Sortie du Feedback avec les cotations.




#if __name__ == "__main__":
main()
