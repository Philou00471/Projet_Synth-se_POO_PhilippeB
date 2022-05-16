###################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet synthèse POO
###  Nom: Philippe Bertrand
###  Description du fichier: Définition de la classe TypeEmploie
####################################################################################


#Création de la classe TypeEmploie
class TypeEmploie:
    """
    Classe parent TypeEmploie
    """
    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, pNoEmploye = "X-1111", pNom = "ABC", pPrenom = "XYZ"):

        self.__NumeroEmploye = pNoEmploye
        self.NomEmploye = pNom
        self.PrenomEmploye = pPrenom

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    def __str__(self):
        """
        Méthode spéciale pour l'affichage d'un objet TypeEmploie()
        :return: Chaine: Chaine d'affichage
        """
        Chaine = "\nNo. Employé: " + str(self.__NumeroEmploye)
        Chaine += "\nNom :        " + self.NomEmploye
        Chaine += "\nPrénom :     " + self.PrenomEmploye

        return Chaine

    ############################################
    #####  MÉTHODES D'ACCÈS ET PROPRIÉTÉS  #####
    ############################################

    #Méthode accesseur pour l'objet NoEmp
    def __getNoEmp(self) -> object:
        """
        Méthode d'accès Accesseur pour lire la valeur de l'attribut __NumeroEmploye.
        Doit être du texte
        :return: object
        """
        return self.__NumeroEmploye

    def __setNoEmp(self, pNoEmploye : object) -> None:

        self.__NumeroEmploye = pNoEmploye

    NumEmploye = property(__getNoEmp,__setNoEmp)

#################################################################################################
#################################################################################################

#Classe Enfant T_TempsPlein

class T_TempsPlein(TypeEmploie):
    """
    Classe enfant T_TempsPlein
    Correspond au type d'emploie de l'employé
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, pNoEmploye= "X-1111", pNom="ABC", pPrenom="XYZ"):

        TypeEmploie.__init__(self,pNoEmploye, pNom, pPrenom)
        self.__TypeEmploie = "Temps plein"

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    def __str__(self):
        """
        Méthode spéciale pour l'affichage d'un objet T_TempsPlein
        :return: Chaine: Chaine d'affichage
        """
        Chaine = TypeEmploie.__str__(self)
        Chaine += "\nType emploie :       " + self.__TypeEmploie

        return Chaine

    ############################################
    #####  MÉTHODES D'ACCÈS ET PROPRIÉTÉS  #####
    ############################################
    #Méthode accesseur
    def __getTypEmp(self) -> str:
        """
        Méthode accesseur pour lire la valeur de l'attribut TypEmp
        :return: string
        """
        return self.__TypeEmploie

    #Propriétés de TypeEmploie
    TypeEmploie = property(__getTypEmp)

#################################################################################################
#################################################################################################

#Création de la classe T_TempsPartiel hérité de la classe TypeEmploie
class T_TempsPartiel(TypeEmploie):
    """
    Classe enfant T_TempsPartiel
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, pNoEmploye="X-1111", pNom="ABC", pPrenom="XYZ"):

        TypeEmploie.__init__(self,pNoEmploye, pNom, pPrenom)
        self.__TypeEmploie = "Temps partiel"

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    def __str__(self):
        """
        Méthode spéciale pour l'affichage d'un objet T_TempsPartiel
        :return: Chaine: Chaine d'affichage
        """
        Chaine = TypeEmploie.__str__(self)
        Chaine += "\nType emploie :       " + self.__TypeEmploie

        return Chaine

    #Méthode accesseur
    def __getTypEmp(self) -> str:
        """
        Méthode accesseur pour lire la valeur de l'attribut TypEmp
        :return: string
        """
        return self.__TypeEmploie

    #Propriétés TypeEmploie
    TypeEmploie = property (__getTypEmp)

#Création de la classe T_SurAppel en héritage de la classe TypeEmploie
class T_SurAppel(TypeEmploie):
    """
    Classe enfant T_SurAppel
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, pNoEmploye="X-1111", pNom="ABC", pPrenom="XYZ"):
        TypeEmploie.__init__(self, pNoEmploye, pNom, pPrenom)
        self.__TypeEmploie = "Sur appel"

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    def __str__(self):
        """
        Méthode spéciale pour l'affichage d'un objet T_TempsSurAppel
        :return: Chaine: Chaine d'affichage
        """
        Chaine = TypeEmploie.__str__(self)
        Chaine += "\nType emploie :       " + self.__TypeEmploie

        return Chaine

    ############################################
    #####  MÉTHODES D'ACCÈS ET PROPRIÉTÉS  #####
    ############################################
    #Méthode accesseur
    def __getTypEmp(self) -> str:
        """
        Méthode accesseur pour lire la valeur de l'attribut TypEmp
        :return: string
        """
        return self.__TypeEmploie

    #Propriétés TypeEmploie
    TypeEmploie = property (__getTypEmp)

    def CalculerImpot(self) -> float:

        Impot = 0.00

        if TypeEmploie == "Temps plein":
            self.Impot = 0.40
        if TypeEmploie == "Temps partiel":
            self.Impot = 0.20
        if TypeEmploie == "Sur appel":
            self.Impot = 0.10

        return(Impot)



def main():

 while True:
        # Validation pour le numéro de l'employé. Seul les numéros avec 1 lettre + 1 tiret + 4 chiffres sont acceptés
        No_ = input("Veuillez donner le numéro de l'employé :")
        TypeEmploie.NumeroEmploye = No_
        if TypeEmploie.NumeroEmploye != No_:
            print("Erreur de validation du numéro de l'employé. Recommencez...")
        else:
            print("Numéro de l'employé validé !")
            break

if __name__ == "__main__":
        main()



