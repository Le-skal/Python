# Rapport synthétique — Trois projets Python

## Vue d’ensemble

Ce rapport présente trois projets Python distincts, en mettant l’accent sur leur **méthodologie**, leurs **résultats**, ainsi qu’une **analyse et des commentaires**.
Chaque projet illustre des compétences appliquées en **analyse de données**, **algorithmique** et **automatisation web**.

---

## **Projet 1 : Analyseur et visualiseur d’ADN**

### **Méthodologie**

* **Bibliothèques utilisées :** `matplotlib`
* **Objectif :** Analyser des séquences d’ADN afin de compter les paires de bases complémentaires et de les représenter graphiquement.
* **Procédure :**

  1. Lecture des séquences d’ADN depuis un fichier texte (`ADN/DNAFile.txt`).
  2. Parcours de chaque séquence pour compter :

     * Les paires `CG` ou `GC`
     * Les paires `AT` ou `TA`
  3. Calcul des pourcentages relatifs de chaque type de paire.
  4. Génération d’un graphique en barres comparant les comptages.

### **Résultats**

* **Exemple de sortie console :**

  ```text
  DNA: ATGCCGTA
    CG/GC count: 2, AT/TA count: 1, total pairs: 3
    CG/GC %: 66.67%, AT/TA %: 33.33%
  ```
* **Visualisation :**
  Un graphique en barres présentant, pour chaque séquence, le nombre de paires `CG/GC` et `AT/TA`.

### **Commentaires / Analyse**

* **Forces :**

  * Algorithme simple et efficace basé sur l’analyse de chaînes de caractères.
  * Représentation graphique claire et lisible.
  * Gestion robuste des caractères invalides et des divisions par zéro.

* **Axes d’amélioration :**

  * Intégrer le **taux de contenu GC**, indicateur biologique pertinent.
  * Ajouter des **analyses statistiques** ou comparatives entre séquences.
  * Mettre en place une **gestion d’erreurs** si le fichier source est manquant.

---

## **Projet 2 : Générateur et validateur d’IBAN**

### **Méthodologie**

* **Bibliothèques utilisées :** Bibliothèques standard de Python.
* **Objectif :** Générer des IBAN valides (International Bank Account Number) à partir d’informations bancaires.
* **Procédure :**

  1. Lecture des informations depuis un fichier texte : `banque`, `agence`, `compte`, `idNational`.
  2. Conversion des lettres en chiffres selon la règle (`A → 10`, `B → 11`, etc.).
  3. Construction d’un IBAN provisoire et réarrangement selon la norme IBAN.
  4. Calcul de la **clé de contrôle** à l’aide de l’algorithme **mod97**.
  5. Génération de l’IBAN complet sous la forme :
     `FR<clé><banque><agence><compte><idNational>`

### **Résultats**

```text
IBAN provisoire : FR00XXXXXXXXXXXXXX
IBAN rearrange : XXXXXXXXXXXXFR00
Reste final : 42
Clé calculée : 56
IBAN final : FR56XXXXXXXXXXXXXX
```

Le projet peut être étendu pour effectuer la **vérification automatique** des IBAN à l’aide d’API publiques telles que [ibanapi.com](https://ibanapi.com) ou [iban.fr](https://www.iban.fr).

### **Commentaires / Analyse**

* **Forces :**

  * Implémentation correcte de l’algorithme **mod97**, utilisé dans la norme IBAN.
  * Structure de code claire et modulaire (lecture, conversion, calcul).
  * Préparation à une intégration graphique via une interface **Tkinter**.

* **Axes d’amélioration :**

  * Vérifier le **format du fichier d’entrée** et la validité des champs.
  * Intégrer une **validation en ligne** à l’aide d’une API externe.
  * Finaliser l’**interface graphique** mentionnée dans le code.

---

## **Projet 3 : Scraper de restaurants (Yellow Pages)**

### **Méthodologie**

* **Bibliothèques utilisées :** `selenium`, `BeautifulSoup`, `csv`, `time`, `random`
* **Objectif :** Automatiser l’extraction d’informations sur les restaurants de *YellowPages.com* (région de Los Angeles).
* **Procédure :**

  1. Lancement d’un navigateur Chrome via Selenium.
  2. Parcours des pages listant les restaurants.
  3. Extraction des informations principales à l’aide de BeautifulSoup :

     * Nom du restaurant
     * Catégories
     * Note YP (déduite des classes CSS)
     * Numéro de téléphone
     * Statut d’ouverture
  4. Enregistrement des résultats dans un fichier CSV.

### **Résultats**

* **Fichier de sortie :** `la_restaurants.csv`
* **Colonnes principales :**

  | Nom       | Catégories           | Note YP | Téléphone      | Statut            |
  | --------- | -------------------- | ------- | -------------- | ----------------- |
  | The Grill | American, Steakhouse | 4.5     | (213) 555-9876 | Ouvert maintenant |

### **Commentaires / Analyse**

* **Forces :**

  * Combinaison efficace de **Selenium** (navigation) et **BeautifulSoup** (analyse HTML).
  * Délai aléatoire intégré pour limiter les risques de blocage.
  * Export structuré et exploitable en CSV.

* **Axes d’amélioration :**

  * Ajouter une **gestion des exceptions** en cas d’éléments manquants ou d’erreurs réseau.
  * Activer le **mode sans interface graphique (headless)** pour de meilleures performances.
  * Respecter les **bonnes pratiques de scraping** (vérification du fichier `robots.txt`).

---

## **Synthèse générale**

| Projet                   | Domaine               | Méthodologie                      | Résultat            | Points forts                   | Axes d’amélioration                      |
| ------------------------ | --------------------- | --------------------------------- | ------------------- | ------------------------------ | ---------------------------------------- |
| **Analyseur ADN**        | Bio-informatique      | Analyse de motifs + visualisation | Graphique en barres | Visualisation claire et simple | Ajouter taux GC et gestion d’erreurs     |
| **Générateur IBAN**      | Fintech / Algorithmes | Traitement de chaînes + mod97     | IBAN complet        | Calcul exact et conforme       | Ajouter validation API et interface      |
| **Scraper Yellow Pages** | Automatisation Web    | Selenium + BeautifulSoup          | Fichier CSV         | Extraction structurée          | Gestion d’erreurs et éthique du scraping |

---

## **Conclusion**

Ces trois projets illustrent des compétences solides en :

* **Programmation algorithmique** (checksum mod97, analyse de séquences)
* **Automatisation et extraction de données web**
* **Analyse et visualisation de données**

Chaque script est autonome et fonctionnel, démontrant une bonne maîtrise de l’écosystème Python et de ses applications concrètes.
Les prochaines étapes pourraient inclure :

* Une **gestion d’erreurs** plus robuste
* Une **documentation et des tests unitaires**
* L’intégration d’**API externes** ou d’interfaces graphiques pour une utilisation plus interactive

