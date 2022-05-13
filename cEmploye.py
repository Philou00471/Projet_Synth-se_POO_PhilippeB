###################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet synthèse POO
###  Nom: Philippe Bertrand
###  Description du fichier: Définition de la classe Employe
####################################################################################


#Classe d'objet Employe
import cEmploye as E



class Employe :
    """
    Classe d'objet Employe
    """
    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, pNoEmp = "X-1111", pPrenom = "ABC", pNom = "DEF", pTel = "111-111-1111", pFonction = "ABC", pTauxHoraire = 0.00):
        """
        Constructeur de la classe Employe
        :param pNoEmp: Type Texte
        :param pPrenom: Type Texte
        :param pNom: Type texte
        :param pTel: Type texte
        :param pFonction: Type texte
        :param pTauxHoraire: Numéro réel
        """
        self.__NumeroEmploye = pNoEmp
        self.PrenomEmploye = pPrenom
        self.NomEmploye = pNom
        self.__TelEmploye = pTel
        self.__Fonction = pFonction
        self.__TauxHoraire = pTauxHoraire

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
        Méthode spéciale pour l'affichage d'un objet Employe()
        :return: Chaine : Chaine d'affichage
        """
        Chaine = ("*" * 45)
        Chaine += "\nNo. Employé : " + self.__NumeroEmploye
        Chaine += "\nPrénom  : " + self.PrenomEmploye
        Chaine += "\nNom : " + self.NomEmploye
        Chaine +=  "\nNuméro téléphone : " + self.__TelEmploye
        Chaine += "\nFonction : " + self.__Fonction
        Chaine += "\nTaux horaire : {:.2f} $".format(self.__TauxHoraire)


        return Chaine

    ############################################
    #####  MÉTHODES D'ACCÈS ET PROPRIÉTÉS  #####
    ############################################

    #####################################################
    #Propriétés pour le numéro de l'employé

    #Accesseur pour NumeroEmploye

    def __getNoEmp(self) -> str:
        """
        Méthode d'accès Accesseur pour lire la valeur de l'attribut __NumeroEmploye.
        Doit être du texte
        :return: string
        """
        return self.__NumeroEmploye

    #Mutateur pour NumeroEmploye

    def __setNoEmp(self, pNoEmp: str) -> None:
        """
        Méthode d'accès mutateur pour assigner la valeur de l'attribut __NumeroEmploye
        -Le numéro du client doit avoir le format suivant :
        :param pNoEmp: No de l'employé
        :return: None
        """
        Valide = True

        if len(pNoEmp) == 6: #La longueur du NoEmp doit être 6
            for i in range (0, len(pNoEmp)):
                if i in [0]: #Si l'index 0 n'est pas dans la chaine de caractères = erreur
                    if pNoEmp[i].upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        Valide = False
                        break
                if i in [1]: #Si l'index 1 n'est pas un tiret = erreur
                    if pNoEmp[i] not in "-":
                        Valide = False
                        break
                if i in [2,3,4,5]: #Si les index 2,3,4,5 ne sont pas des chiffres entre 0 et 9 = erreur
                    if pNoEmp[i] not in "1234567890":
                        Valide = False
        #Tout autres réponses non-conforme est fausse aussi
        else :
            Valide = False

        # Si la validation est bonne on enregistre

        if Valide == True:
            self.__NumeroEmploye = pNoEmp

    #Propriétés pour le numéro de l'employé
    NumEmploye = property(__getNoEmp ,__setNoEmp)

    #Méthode accesseur pour l'attribut
    def __getTel(self) -> str:
        """
        Méthode d'accès Accesseur pour lire la valeur de l'attribut __NumeroEmploye.
        Doit être du texte
        :return: string
        """
        return self.__TelEmploye

    #Méthode mutateur pour l'attribut TelEmployé
    def __setTel(self, pTel:str) -> None:
        """
        Le numéro de téléphone de l'employé doit être composé avec cette structure:
        3 chiffres + tiret + 3 chiffres + tiret + 4 chiffres
        :param pTel: str: Rentré par l'employé
        :return:
        """
        Valide = True

        if len(pTel) == 12: #La longueur du NoTel doit être de 12
            for i in range(0, len(pTel)):
                if i in [0,1,2,4,5,6,8,9,10,11]: #Si l'index des nombres suivants n'est pas un nombre entre 0 et 9 = erreur
                    if pTel[i] not in "0123456789":
                        Valide = False
                        break
                if i in [3,7,]: #Si l'index de 3 et 7 n'est pas un tiret = erreur
                    if pTel[i] not in "-":
                        Valide = False
                        break
        #Tous autres résultats est refusé
        else:
            Valide = False
        #Si le numéro est conforme aux validations
        if Valide == True:
            self.__TelEmploye = pTel

    #Propriétés pour le numéro de téléphone

    TelEmploye = property(__getTel, __setTel)

    #Méthode accesseur de l'attribut Fonction
    def __getFonction(self) -> str:
        """
        Méthode d'accesseur pour lire la valeur de l'attribut Fonction
        :return:
        """
        return self.__Fonction

    #Méthode mutateur pour l'attribut Fonction

    def __setFonction(self, pFonction : str) -> None:
        """
        La valeur rentré par le client doit être :
        -Superviseur
        -Directeur
        -Comptabilité
        -Gestion
        -Marketing
        :param pFonction:
        :return:
        """
        #Création d'une liste avec tous les choix de fonctions
        lsFonctions = ["Superviseur", "Directeur", "Comptabilité", "Gestion", "Marketing"]
        #Si la fonction donné est dans la liste = vrai
        if pFonction in lsFonctions:
             self.__Fonction = pFonction
    #Propriétés pour la fonction de l'employé
    FonctionEmploye = property(__getFonction, __setFonction)

    #Méthode accesseur TauxHoraire
    def __getTauxHoraire(self) -> float:
        """
        Méthode accesseur de l'attribut TauxHoraire
        :return:
        """
        return self.__TauxHoraire

    #Méthode mutateur de TauxHoraire

    def __setTauxHoraire(self, pTauxHoraire : float)-> None:
        """
        Méthode mutateur de l'attribut TauxHoraire.
        :param pTauxHoraire:
        :return:
        """
        if pTauxHoraire > 0 and pTauxHoraire <= 150:
            self.__TauxHoraire = pTauxHoraire

    TauxHoraire = property(__getTauxHoraire, __setTauxHoraire)


def main():
#Création de la liste lsEmployes
 lsEmployes = []

#Instanciation d'objets
 lsEmployes.append(E.Employe("H-2345","Philippe","Bertrand", "819-827-4693","Marketing", 60.00))
 lsEmployes.append(E.Employe("P-2567", "Jean", "Lasalle", "819-856-4111", "Superviseur", 120.00))
 lsEmployes.append(E.Employe("W-5555", "Marine", "Lepen", "819-856-0002", "Directeur", 55.55))
 lsEmployes.append(E.Employe("K-6395", "Emmanuel", "Macron", "819-427-4569", "Comptabilité", 51.99))
 lsEmployes.append(E.Employe("L-2789", "Jean-Luc", "Mélenchon", "810-555-5555", "Gestion", 149.00))

 Employe_ = Employe()

 #Application pour les tests unitaires
 while True:

     print("Menu Test pour la classe Employe")
     print("1. Afficher la liste des employés")
     print("2. Ajouter un employé avec les validations de valeur")
     print("3. Quitter")
     Choix = input("Veuillez faire un choix :")

#Test pour l'affichage des employés. Si le str() fonctionne
     if Choix == "1":
       for objEmploye in lsEmployes:
        print(objEmploye)
     if Choix == "2":
         while True:
             #Validation pour le numéro de l'employé. Seul les numéros avec 1 lettre + 1 tiret + 4 chiffres sont acceptés
             No_ = input("Veuillez donner le numéro de l'employé :")
             Employe_.NumEmploye = No_
             if Employe_.NumEmploye != No_:
                 print("Erreur de validation du numéro de l'employé. Recommencez...")
             else:
                 print("Numéro de l'employé validé !")
                 break
         #Aucune validation a faire pour le nom et pronom
         Employe_.NomEmploye = input("Veuillez donner le nom de l'employé :")
         Employe_.PrenomEmploye = input("Veuillez donner le prénom de l'employé :")

         #Validation pour le numéro de téléphone de l'employé.
         #Seul les numéros de téléphone avec 3 chiffres + 1 tiret + 3 chiffres + 1 tiret + 4 chiffres sont acceptés
         while True:
             Tel_ = input("Veuillez donner le numéro de téléphone de l'employé :")
             Employe_.TelEmploye = Tel_
             if Employe_.TelEmploye != Tel_:
                 print("Erreur de validation du numéro de téléphone de l'employé. Recommencez...")
             else:
                 print("Numéro de téléphone de l'employé validé !")
                 break
         #Validation pour la fonction de l'employé.
         #Seul les 5 fonctions disponibles dans la liste lsFonctions sont acceptés
         while True:
             Fonction_ = input("Veuillez donner la fonction de l'employé :")
             Employe_.FonctionEmploye = Fonction_
             if Employe_.FonctionEmploye != Fonction_:
                 print("Erreur de validation de la fonction de l'employé. Recommencez...")
             else:
                 print("La fonction de l'employé est validé !")
                 break

         #Validation pour le taux horaire de l'employé. Seuls les taux horaires entre 0 exclu et 150 inclu sont acceptés.
         while True:
             TauxHoraire_ = int(input("Veuillez donner le taux horaire de l'employé :"))
             Employe_.TauxHoraire = TauxHoraire_
             if Employe_.TauxHoraire != TauxHoraire_:
                 print("Erreur de validation du taux horaire de l'employé. Recommencez...")
             else:
                 print("Taux horaire de l'employé validé !")
                 break
     #Ajout des informations du nouveau employé dans la liste lsEmployes
     lsEmployes.append(Employe_)

     if Choix == "3":
         print("Fin des tests")
         break

if __name__ == "__main__":
    main()