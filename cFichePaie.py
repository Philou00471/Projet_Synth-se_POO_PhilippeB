###################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet synthèse POO
###  Nom: Philippe Bertrand
###  Description du fichier: Définition de la classe FichePaie
####################################################################################

import cFichePaie as F
import cEmploye as E
import datetime as DT
import cTypeEmploie as T
class FichePaie:
    """
    Classe d'objet FichePaie
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, pInfosEmploye = E.Employe(),pNoFiche = "" ,pDate = DT.datetime.now(), pNbHeures = -1, pBrut = 0.00,pTypEmploye = T.T_TempsPartiel() ,pImpot = 0.00, pNet = 0.00):
        """

        :param pInfosEmploye: Association texte
        :param pNoFiche: Texte
        :param pDate: Date
        :param pNbHeures: int
        :param pBrut: float
        :param pTypEmploye: Association texte
        :param pImpot: float
        :param pNet: float
        """


        self.__InformationEmploye = pInfosEmploye
        self.__NumeroFiche = pNoFiche
        self.__Date = pDate
        self.__NombreHeures = pNbHeures
        self.__SalaireBrut = pBrut
        self.__TypeEmploye = pTypEmploye
        self.__Impot = pImpot
        self.__SalaireNet = pNet

    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        """
        Méthode d'affichage spéciale pour une fiche de paie d'un employé
        :return: Chaine : Chaine d'affichage
        """
        Chaine ="-----------------------------------------------Information sur l'employé-----------------------------------------------"
        Chaine +="\nNuméro de la fiche de paie : {}            Date : {}\n".format(self.__NumeroFiche, self.__Date.strftime("%A le %d %B %Y"))
        Chaine +="\nNuméro de l'employé : " + self.__InformationEmploye.NumEmploye
        Chaine +="\nPrénom de l'employé : " + self.__InformationEmploye.PrenomEmploye
        Chaine +="\nNom de l'employé : " + self.__InformationEmploye.NomEmploye
        Chaine +="\nTaux horaire : " + str(self.__InformationEmploye.TauxHoraire) + "\n"

        Chaine += ("*" * 45)
        Chaine +="\n-----------------------------------------------Calcul de la paye-------------------------------------------------------"
        Chaine +="\nNombre d'heures : " + str(self.__NombreHeures)
        Chaine +="\nSalaire brut :                                    {:>7.2f} $\n".format(self.__SalaireBrut)
        Chaine +="Impôt :                                           {:>7.2f} %\n".format(self.__Impot)
        Chaine +="Salaire Net :                                     {:>7.2f} $\n".format(self.__SalaireNet)
        Chaine += ("*" * 60)
        return Chaine

    ############################################
    #####  MÉTHODES D'ACCÈS ET PROPRIÉTÉS  #####
    ############################################

    #Méthode accesseur de l'objet InfosEmploye

    def __getInfoEmploye(self) -> object:

         return self.__InformationEmploye

    #Méthode mutateur de l'objet InfosEmploye
    def __setInfoEmploye(self, pInfosEmploye: object) -> None:
        """
        Aucune validation à faire Le mutateur est nécessaire pour s'assurer
        de recevoir un objet pour l'attribut __InformationEmploye
        :param pInfosEmploye:  object : objet de type InfosEmploye
        :return:
        """

        self.__InformationEmploye = pInfosEmploye
    #Propriété pour InfosEmoploye
    InfEmploye = property(__getInfoEmploye, __setInfoEmploye)

    #Méthode accesseur pour l'attribut NoFiche
    def __getNoFiche(self) -> str:

        return self.__NumeroFiche

    #Méthode mutateur pour l'attribut NoFiche
    def __setNoFiche(self, pNoFiche : str) -> None:
        """
        La longueur du numéro de la fiche de paie doit être de 10 caractères.
        5 lettres et 5 chiffres qu'ont change simultanément par exemple: A2B4C5D6E1
        :param pNoFiche: string Numéro de la fiche
        :return:
        """
        Valide = True

        if len(pNoFiche) == 10:
            for i in range(0, len(pNoFiche)):
                if i in [0,2,4,6,8]:
                    if pNoFiche[i].upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        Valide = False
                        break
                if i in [1,3,5,7,9]:
                    if pNoFiche[i].upper() not in "0123456789":
                        Valide = False
        # Tout autres réponses non-conforme est fausse aussi
        else:
            Valide = False

        # Si la validation est bonne on enregistre
        if Valide == True:
            self.__NumeroFiche = pNoFiche

    #Propriété pour numerofiche
    NumeroFiche = property(__getNoFiche, __setNoFiche)

    #Méthode accesseur pour l'attribut Date
    def __getDateFiche(self) -> DT.datetime:

        return self.__Date
    #Méthode mutateur pour l'attribut Date
    def __setDateFiche(self, pDate: DT.datetime) -> None:
        """
        La date de la fiche de paie ne peut être inférieur à la date d'aujourd'hui,
        mais peut être supérieure.
        :param: pDateFiche : Date de la fiche
        :param pDate:
        :return:
        """
        if pDate >= DT.datetime.now():
            self.__Date = pDate

    #Propriété pour Date
    DateFiche = property(__getDateFiche,__setDateFiche)

    #Méthode accesseur pour l'attribut Nbheures
    def __getNbHeures(self) -> int:

        return self.__NombreHeures

    #Méthode mutateur pour l'attribut NbHeures
    def __setNbHeures(self, pNbHeures : int):
        """
        Le nombre d'heures doit être plus grand que 0
        :param pNbHeures:
        :return:
        """
        if pNbHeures > 0:
            self.__NombreHeures = pNbHeures

    #Propriété pour NombreHeures
    NombreHeures = property(__getNbHeures, __setNbHeures)

    #Méthode accesseur pour l'attribut SalaireBrut
    def __getBrut(self) -> float:

        return self.__SalaireBrut

    #Propriété SalaireBrut
    SalaireBrut = property(__getBrut)

    #Méthode accesseur pour l'objet typeEmploye
    def __getTypEmploye(self) -> object:
        return self.__TypeEmploye

    def __setTypEmploye(self,pTypEmploye) ->None:

        self.__TypeEmploye = pTypEmploye

    TypeEmploye = property(__getTypEmploye, __setTypEmploye)

    #Méthode accesseur pour l'attribut Impot
    def __getImpot(self) -> float:

        return self.__Impot

    #Propriété Impot
    Impot = property(__getImpot)

    #Méthode accesseur pour l'attribut SalaireNet
    def __getNet(self) -> float:

        return self.__SalaireNet

    #Propriété SalaireNet
    SalaireNet = property(__getNet)

#Définition de la méthode CalculerPaie
    def CalculerPaie(self) -> None:
    #Condition de l'impot selon le type d'emploie de l'employé
        if self.__TypeEmploye.TypeEmploie == "Temps plein":
            self.__Impot = 0.40
        if self.__TypeEmploye.TypeEmploie == "Temps partiel":
            self.__Impot = 0.30
        if self.__TypeEmploye.TypeEmploie == "Sur appel":
            self.__Impot = 0.20

        SousTotal = self.__NombreHeures * E.Employe.TauxHoraire

        MontantImpot = SousTotal  * self.__Impot

        MontantTotal = self.__SalaireBrut - MontantImpot

        self.__SalaireNet = MontantTotal

def main():

   lsFiche = []

   lsInfosEmploye = []

   lsInfosEmploye.append(E.Employe("H-2345","Philippe","Bertrand", "819-827-4693","Marketing", 60.00))

   lsFiche.append(F.FichePaie(lsInfosEmploye[0], "ABC",))

   FichePaie.DateFiche = DT.datetime.now()
   FichePaie.NumeroFiche = lsFiche[0]

   for objFiche in lsFiche:
       print(objFiche)

if __name__ == "__main__":
    main()

