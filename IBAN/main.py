def lire_infos(fichier):
    with open(fichier, "r") as f:
        chiffres = []
        for ligne in f:
            ligne = ligne.strip()
            if ligne:
                morceaux = ligne.split()
                chiffres.append(morceaux[-1])

    if len(chiffres) < 4:
        raise ValueError("Fichier incomplet ou format inattendu")

    banque, agence, compte, idNational = chiffres[:4]
    return banque, agence, compte, idNational


def convertir_lettres(ch):
    """Convertit une chaine en remplacant A-Z par 10-35"""
    resultat = ""
    for c in ch:
        if c.isalpha():
            resultat += str(ord(c.upper()) - 55)
        else:
            resultat += c
    return resultat


def mod97(iban_numeric: str) -> int:
    reste = 0
    for digit in iban_numeric:
        reste = (reste * 10 + int(digit)) % 97
    return reste


def calculer_cle_iban(pays, bban):
    iban_prov = f"{pays}00{bban}"
    print("IBAN provisoire :", iban_prov)

    iban_rearr = iban_prov[4:] + iban_prov[:4]
    print("IBAN rearrange :", iban_rearr)

    iban_numerique = convertir_lettres(iban_rearr)
    print("IBAN numerique :", iban_numerique)

    reste = mod97(iban_numerique)
    print("Reste final :", reste)

    cle = 98 - reste
    print("Cle calculee :", cle)
    return f"{cle:02d}"


def genererat(banque, agence, compte, idNational, pays="FR"):
    bban = f"{banque}{agence}{compte}{idNational}"
    cle_iban = calculer_cle_iban(pays, bban)
    return f"{pays}{cle_iban}{bban}"


def charger_fichier(filepath):
    banque, agence, compte, idNational = lire_infos(filepath)
    iban = genererat(banque, agence, compte, idNational)
    return banque, agence, compte, idNational, iban


if __name__ == "__main__":
    import IBANGeneratorGUI

    IBANGeneratorGUI.run()

# ajouter une interface tres basic tkinter (generer iban depuis un fichier et mettre la cles par default a 14)
# genere la cle de controle tout seul
# https://www.iban.fr/calcul-chiffre-de-controle.html
# Accéder au Web Service publique de vérification d'IBAN
# https://fr.iban.com/validation-api#:~:text=L'API%20de%20validation%20IBAN%20V4%20vous%20permet%20de%20faire,des%20chiffres%20de%20contr%C3%B4le*%20valides
# https://ibanapi.com
# Form pour rendre https://forms.gle/wNtYYVC1nbacXA7e6
# curl "https://api.ibanapi.com/v1/validate/FR1420041010050500013M02606?api_key=261f79768b16828f01ba93b650631c6d2d17b550"
# curl "https://api.ibanapi.com/v1/validate/FR4230066104640002073130156?api_key=261f79768b16828f01ba93b650631c6d2d17b550"