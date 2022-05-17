###################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Projet synthèse POO
###  Nom: Philippe Bertrand
###  Description du fichier: Définition de la classe Admin
####################################################################################

class Admin:
    """
    Classe d'objet Admin
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, pNomAdmin = "Admin123", pMdpAdmin = "MotDePasseAdmin123"):
        """

        :param pNomAdmin:
        :param pMdpAdmin:
        """

        self.AdminNom = pNomAdmin #Identifiant Admin
        self.MotDePasse = pMdpAdmin #Mot de passe admin


    #Méthode str n'est pas nécessaire

    #Méthode accesseur
    def __getAdminNom(self) -> str:
        """
        Méthode accesseur pour lire la valeur de l'attribut AdminNom
        :return:
        """

        return self.AdminNom

    #Méthode mutateur
    def __setAdminNom(self, pNomAdmin:str) -> None:
        """
        Méthode mutateur de l'attribut AdminNom:
        AdminNom est obligatoirement (Admin123)
        :param pNomAdmin:
        :return:
        """

        if pNomAdmin == "Admin123":
            self.AdminNom = pNomAdmin

    #Propriétés pour le nom d'admin
    NomDeAdmin = property(__getAdminNom, __setAdminNom)

    #Méthode accesseur
    def __getMotDePasse(self) -> str :
        """
        Méthode accesseur pour lire la valeur de l'attribut MotDePasse
        :return:
        """

        return self.MotDePasse

    #Méthode mutateur
    def __setMotDePasse(self, pMdpAdmin : str) -> None:
        """
        Méthode mutateur de l'attribut MotDePasse
        MotDePasse est obligatoirement (MotDePasseAdmin123)
        :param pMdpAdmin:
        :return:
        """
        if pMdpAdmin == "MotDePasseAdmin123":
            self.MotDePasse = pMdpAdmin

    #Propriétés pour le mot de passe d'admin
    AdminMdp = property(__getMotDePasse, __setMotDePasse)
