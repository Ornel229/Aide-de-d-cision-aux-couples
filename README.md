# Assistant de lecture des résultats de porteur (drépanocytose)

Prototype pour le hackathon Hack2Skill : *comment aider les individus, les familles et les systèmes de santé à identifier, comprendre et réduire les risques de maladies héréditaires associés à la consanguinité, avec des technologies culturellement adaptées et respectueuses de la vie privée ?*

## Problème

Un dépistage prénuptial ou préconceptionnel n'est utile que si les personnes comprennent leur résultat, accèdent à un conseil adapté et décident librement. Une information génétique est complexe, probabiliste et partagée au sein des familles : mal expliquée, elle crée de l'anxiété, de la stigmatisation ou une certitude excessive.

## Solution

Une application web mobile (Streamlit) qui explique un résultat d'hémoglobine à un couple, en langage simple et non stigmatisant, et qui l'accompagne vers un conseil génétique. Maladie de démonstration : la drépanocytose (transmission autosomique récessive).

## Fonctions

| Onglet | Ce qu'il fait | Critère du défi |
|---|---|---|
| Résultats | Saisie du génotype de chaque partenaire (AA, AS, AC, Aβ, SS, SC, Sβ) ou « je ne sais pas encore » | Accès |
| Explication | Grille de scénarios, probabilité par grossesse, statut de porteur, messages clés (risque ≠ diagnostic, incertitude), lecture à voix haute | Explication des risques |
| Partage | Consentement explicite, partage choisi par personne et par élément, retrait à tout moment, journal des accès | Vie privée |
| Suite | Parcours traçable : résultats, explication, conseil recommandé, rendez-vous, test de confirmation, service spécialisé | Accès sécurisé aux services |
| Indicateurs | Quiz de compréhension, étapes réalisées, export CSV anonyme | Compréhension et accès mesurables |

Langues : français et anglais. Le fon, le yoruba et d'autres langues locales sont prévus à l'itération suivante (voir « Limites »).

## Choix de conception

- **Aucun jugement, aucune contrainte** : l'application explique des probabilités et ne recommande jamais de décision (mariage, grossesse). Le succès ne se mesure pas en annulations de mariage.
- **Minimisation des données** : aucune base de données, aucun fichier écrit. Tout vit dans la session du navigateur et disparaît à la fermeture.
- **Export anonyme** : le CSV contient seulement l'heure, le type d'événement, la langue et un détail technique (score, numéro d'étape). Jamais de nom ni de résultat.
- **Cas complexes** : toute situation avec un risque de forme de drépanocytose ou d'« autre combinaison » déclenche la recommandation d'un conseil génétique.
- **Calculs exacts** : les probabilités utilisent des fractions (pas d'arrondi), vérifiées par des tests.

## Architecture

```
app.py          Interface Streamlit (5 onglets, état de session, journal d'accès)
genetique.py    Moteur de scénarios : grille de Punnett, probabilités par catégorie
textes.py       Textes FR/EN et quiz (à valider par des professionnels et des locuteurs natifs)
test_genetique.py  Tests du moteur
```

Le moteur ne dépend d'aucune bibliothèque externe. Seule l'interface demande Streamlit.

## Lancer

```bash
pip install -r requirements.txt
streamlit run app.py
```

Tests du moteur : `python test_genetique.py`

## Indicateurs à suivre

- Compréhension : score au quiz (3 questions).
- Accès : part des utilisateurs qui prennent un rendez-vous de conseil et délai entre le résultat et l'orientation.
- Vie privée : nombre de partages accordés et retirés, aucune fuite de données dans les journaux.
- Équité : comparaison des scores et des étapes selon la langue (colonne `lang` de l'export).

## Limites et prochaine itération

- Les textes médicaux sont des brouillons : ils doivent être validés par un généticien ou un médecin avant tout usage réel.
- Le partage est simulé dans la session : une vraie version demanderait authentification, chiffrement et accès par rôle côté serveur.
- Lecture à voix haute via la synthèse vocale du navigateur : la qualité dépend de la langue installée sur l'appareil.
- Langues locales : traduction et enregistrements audio par des locuteurs natifs.
- Autres maladies récessives (bêta-thalassémie majeure, mucoviscidose, etc.) à ajouter au moteur.
- Ajout possible d'un assistant RAG limité à une base de sources médicales validées.

## Avertissement

Prototype pédagogique avec des données fictives. Il ne remplace ni un conseil génétique ni un avis médical, ne pose aucun diagnostic et n'oriente aucune décision personnelle.
