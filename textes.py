"""Textes de l'application (français / anglais).

À faire valider par un professionnel de santé et par des locuteurs natifs
avant tout usage réel. Langues locales (fon, yoruba...) prévues à l'itération suivante.
"""

TEXTS = {
    "fr": {
        "lang_name": "Français",
        "page_title": "Lire un résultat de porteur",
        "title": "Comprendre ses résultats : drépanocytose",
        "subtitle": "Une explication claire, privée et sans jugement, pour les couples et les familles.",
        "disclaimer": (
            "Prototype pédagogique avec des données fictives. Il ne remplace ni un conseil génétique ni "
            "un avis médical. Il ne pose aucun diagnostic et n'oriente aucune décision personnelle."
        ),
        "welcome_body": (
            "**Comment ça marche ?**\n\n"
            "1. Indiquez le résultat de chaque partenaire (onglet *Résultats*).\n"
            "2. Lisez l'explication, avec lecture à voix haute si vous préférez (onglet *Explication*).\n"
            "3. Choisissez vous-même avec qui partager, et quoi (onglet *Partage*).\n"
            "4. Suivez les prochaines étapes (onglet *Suite*).\n\n"
            "Rien n'est enregistré : tout disparaît quand vous fermez la page."
        ),
        "tabs": ["Accueil", "Résultats", "Explication", "Partage", "Suite"],
        "res_title": "Les résultats",
        "res_help": "Le résultat vient d'un test sanguin (électrophorèse de l'hémoglobine). Si vous ne l'avez pas encore, choisissez « Je ne sais pas encore ».",
        "partner_a": "Partenaire 1",
        "partner_b": "Partenaire 2",
        "geno": {
            "?": "Je ne sais pas encore",
            "AA": "AA : pas de gène drépanocytaire",
            "AS": "AS : porteur (trait drépanocytaire)",
            "AC": "AC : porteur de l'hémoglobine C",
            "AT": "Aβ : porteur de bêta-thalassémie",
            "SS": "SS : drépanocytose",
            "SC": "SC : drépanocytose",
            "ST": "Sβ : drépanocytose (S/bêta-thalassémie)",
        },
        "status": {
            "AA": "Aucun gène de la drépanocytose détecté.",
            "AS": "Porteur : en général en bonne santé, mais peut transmettre le gène S.",
            "AC": "Porteur de l'hémoglobine C : en général en bonne santé, peut transmettre ce gène.",
            "AT": "Porteur d'un gène de bêta-thalassémie : en général en bonne santé, peut le transmettre.",
            "SS": "Vit avec une forme de drépanocytose : un suivi médical spécialisé est recommandé.",
            "SC": "Vit avec une forme de drépanocytose : un suivi médical spécialisé est recommandé.",
            "ST": "Vit avec une forme de drépanocytose : un suivi médical spécialisé est recommandé.",
        },
        "exp_title": "L'explication",
        "exp_unknown": (
            "Il manque au moins un résultat. Le test se fait par une prise de sang (électrophorèse de "
            "l'hémoglobine) dans un laboratoire ou un centre de santé. Revenez ici avec les deux résultats."
        ),
        "status_label": "Statut",
        "punnett_title": "Ce que peut être un enfant, à chaque grossesse",
        "punnett_caption": "Chaque parent transmet l'une de ses deux lettres, au hasard : 1 chance sur 2 chacune.",
        "cat": {
            "non_porteur": "Non porteur",
            "porteur": "Porteur (trait)",
            "drepano": "Forme de drépanocytose",
            "autre": "Autre combinaison (à voir avec un spécialiste)",
        },
        "cat_short": {
            "non_porteur": "Non porteur",
            "porteur": "Porteur",
            "drepano": "Drépanocytose",
            "autre": "Autre",
        },
        "each_pregnancy": "À chaque grossesse, pour ce couple :",
        "key_title": "À retenir",
        "key_messages": [
            "Être porteur n'est pas être malade : un porteur est en général en bonne santé.",
            "Le risque vaut pour chaque grossesse. Il ne s'additionne pas et n'est pas « épuisé » par les enfants précédents.",
            "Un risque n'est pas un diagnostic : seul un examen de l'enfant peut le confirmer.",
            "Un conseiller en génétique peut présenter les options disponibles. La décision vous appartient.",
        ],
        "uncertainty": (
            "Ces chiffres sont des probabilités moyennes. Ils ne disent pas ce qui arrivera pour une "
            "grossesse en particulier, et la gravité varie d'une personne à l'autre."
        ),
        "listen": "Écouter l'explication",
        "quiz_title": "Testez votre compréhension",
        "quiz_check": "Vérifier mes réponses",
        "quiz_answer_all": "Répondez aux 3 questions.",
        "quiz_result": "Score : {score}/3",
        "share_title": "Partager, seulement si vous le voulez",
        "share_intro": (
            "Vous décidez qui voit quoi. Rien n'est partagé sans votre accord explicite, et vous pouvez "
            "retirer l'accès à tout moment. Chaque action est notée dans le journal ci-dessous."
        ),
        "share_name": "Prénom ou surnom de la personne",
        "share_name_help": "Évitez les noms complets : un prénom suffit.",
        "share_role": "Rôle",
        "roles": {"partner": "Partenaire", "family": "Membre de la famille", "counsellor": "Conseiller en génétique"},
        "share_scope": "Ce que vous partagez",
        "scopes": {
            "status": "Mon statut (génotype)",
            "summary": "Le résumé du risque du couple",
            "notify": "Seulement une notification (aucun détail)",
        },
        "share_consent": "Je consens explicitement à ce partage.",
        "share_add": "Ajouter ce partage",
        "share_missing": "Indiquez un prénom, au moins un élément à partager, et cochez votre consentement.",
        "share_active": "Partages actifs",
        "share_none": "Aucun partage pour l'instant.",
        "share_revoke": "Retirer l'accès",
        "audit_title": "Journal des accès",
        "audit_cols": {"ts": "Date", "action": "Action", "who": "Personne", "role": "Rôle", "scope": "Éléments"},
        "audit_actions": {"granted": "Accès accordé", "revoked": "Accès retiré"},
        "next_title": "Les prochaines étapes",
        "counsel_yes": (
            "Un conseil génétique est recommandé : un généticien ou un médecin formé peut confirmer les "
            "résultats et présenter les options disponibles, sans orienter votre décision."
        ),
        "counsel_no": (
            "Dans ce scénario, aucun enfant n'aurait une forme de drépanocytose. Un conseil reste possible "
            "pour toute question."
        ),
        "counsel_wait": "Complétez les résultats des deux partenaires pour voir les étapes adaptées.",
        "steps": [
            "Résultats saisis",
            "Explication lue",
            "Conseil génétique recommandé",
            "Rendez-vous de conseil pris",
            "Test de confirmation réalisé (si conseillé)",
            "Orientation vers un service spécialisé (si besoin)",
        ],
        "step_done_on": "fait le {ts}",
        "indicators_title": "Indicateurs (cette session)",
        "ind_quiz": "Compréhension (quiz)",
        "ind_steps": "Étapes réalisées",
        "ind_shares": "Partages actifs",
        "ind_export": "Télécharger les indicateurs anonymes (CSV)",
        "ind_note": "L'export ne contient ni nom, ni résultat : seulement la langue, les étapes et le score.",
        "audio_label": "Lecture à voix haute",
    },
    "en": {
        "lang_name": "English",
        "page_title": "Reading a carrier result",
        "title": "Understanding your results: sickle cell disease",
        "subtitle": "A clear, private and judgement-free explanation for couples and families.",
        "disclaimer": (
            "Educational prototype with fictional data. It does not replace genetic counselling or "
            "medical advice. It makes no diagnosis and does not steer any personal decision."
        ),
        "welcome_body": (
            "**How it works**\n\n"
            "1. Enter each partner's result (*Results* tab).\n"
            "2. Read the explanation, with read-aloud if you prefer (*Explanation* tab).\n"
            "3. Choose who to share with, and what (*Sharing* tab).\n"
            "4. Follow the next steps (*Next* tab).\n\n"
            "Nothing is saved: everything disappears when you close the page."
        ),
        "tabs": ["Home", "Results", "Explanation", "Sharing", "Next"],
        "res_title": "The results",
        "res_help": "The result comes from a blood test (haemoglobin electrophoresis). If you don't have it yet, choose “I don't know yet”.",
        "partner_a": "Partner 1",
        "partner_b": "Partner 2",
        "geno": {
            "?": "I don't know yet",
            "AA": "AA: no sickle cell gene",
            "AS": "AS: carrier (sickle cell trait)",
            "AC": "AC: haemoglobin C carrier",
            "AT": "Aβ: beta-thalassaemia carrier",
            "SS": "SS: sickle cell disease",
            "SC": "SC: sickle cell disease",
            "ST": "Sβ: sickle cell disease (S/beta-thalassaemia)",
        },
        "status": {
            "AA": "No sickle cell gene detected.",
            "AS": "Carrier: usually in good health, but can pass on the S gene.",
            "AC": "Haemoglobin C carrier: usually in good health, can pass on this gene.",
            "AT": "Beta-thalassaemia carrier: usually in good health, can pass on this gene.",
            "SS": "Lives with a form of sickle cell disease: specialised medical follow-up is recommended.",
            "SC": "Lives with a form of sickle cell disease: specialised medical follow-up is recommended.",
            "ST": "Lives with a form of sickle cell disease: specialised medical follow-up is recommended.",
        },
        "exp_title": "The explanation",
        "exp_unknown": (
            "At least one result is missing. The test is a blood sample (haemoglobin electrophoresis) "
            "taken at a laboratory or health centre. Come back here with both results."
        ),
        "status_label": "Status",
        "punnett_title": "What a child could be, in each pregnancy",
        "punnett_caption": "Each parent passes on one of their two letters at random: a 1 in 2 chance each.",
        "cat": {
            "non_porteur": "Not a carrier",
            "porteur": "Carrier (trait)",
            "drepano": "Form of sickle cell disease",
            "autre": "Other combination (see a specialist)",
        },
        "cat_short": {
            "non_porteur": "Not a carrier",
            "porteur": "Carrier",
            "drepano": "Sickle cell disease",
            "autre": "Other",
        },
        "each_pregnancy": "In each pregnancy, for this couple:",
        "key_title": "Key points",
        "key_messages": [
            "Being a carrier is not being ill: a carrier is usually in good health.",
            "The risk applies to each pregnancy. It does not add up and is not “used up” by earlier children.",
            "A risk is not a diagnosis: only testing the child can confirm it.",
            "A genetic counsellor can explain the available options. The decision is yours.",
        ],
        "uncertainty": (
            "These figures are average probabilities. They do not say what will happen in any one "
            "pregnancy, and severity varies from person to person."
        ),
        "listen": "Listen to the explanation",
        "quiz_title": "Check your understanding",
        "quiz_check": "Check my answers",
        "quiz_answer_all": "Answer all 3 questions.",
        "quiz_result": "Score: {score}/3",
        "share_title": "Share only if you want to",
        "share_intro": (
            "You decide who sees what. Nothing is shared without your explicit consent, and you can "
            "withdraw access at any time. Every action is recorded in the log below."
        ),
        "share_name": "First name or nickname of the person",
        "share_name_help": "Avoid full names: a first name is enough.",
        "share_role": "Role",
        "roles": {"partner": "Partner", "family": "Family member", "counsellor": "Genetic counsellor"},
        "share_scope": "What you share",
        "scopes": {
            "status": "My status (genotype)",
            "summary": "The couple's risk summary",
            "notify": "Notification only (no details)",
        },
        "share_consent": "I explicitly consent to this sharing.",
        "share_add": "Add this sharing",
        "share_missing": "Enter a first name, at least one item to share, and tick your consent.",
        "share_active": "Active sharing",
        "share_none": "No sharing yet.",
        "share_revoke": "Withdraw access",
        "audit_title": "Access log",
        "audit_cols": {"ts": "Date", "action": "Action", "who": "Person", "role": "Role", "scope": "Items"},
        "audit_actions": {"granted": "Access granted", "revoked": "Access withdrawn"},
        "next_title": "Next steps",
        "counsel_yes": (
            "Genetic counselling is recommended: a geneticist or trained doctor can confirm the results "
            "and explain the available options, without steering your decision."
        ),
        "counsel_no": (
            "In this scenario, no child would have a form of sickle cell disease. Counselling is still "
            "available for any question."
        ),
        "counsel_wait": "Complete both partners' results to see the relevant steps.",
        "steps": [
            "Results entered",
            "Explanation read",
            "Genetic counselling recommended",
            "Counselling appointment booked",
            "Confirmation test done (if advised)",
            "Referral to a specialised service (if needed)",
        ],
        "step_done_on": "done on {ts}",
        "indicators_title": "Indicators (this session)",
        "ind_quiz": "Understanding (quiz)",
        "ind_steps": "Steps completed",
        "ind_shares": "Active sharing",
        "ind_export": "Download anonymous indicators (CSV)",
        "ind_note": "The export contains no name and no result: only language, steps and score.",
        "audio_label": "Read aloud",
    },
}

QUIZ = {
    "fr": [
        {"q": "Une personne AS est-elle malade ?",
         "options": ["Oui, toujours", "Non, en général elle est porteuse sans être malade", "On ne peut pas savoir"],
         "answer": 1},
        {"q": "Couple AS × AS : quel est le risque d'un enfant SS à chaque grossesse ?",
         "options": ["0 %", "25 %", "100 %"],
         "answer": 1},
        {"q": "Un risque est-il un diagnostic ?",
         "options": ["Oui", "Non"],
         "answer": 1},
    ],
    "en": [
        {"q": "Is an AS person ill?",
         "options": ["Yes, always", "No, usually a carrier who is not ill", "Impossible to know"],
         "answer": 1},
        {"q": "AS × AS couple: what is the chance of an SS child in each pregnancy?",
         "options": ["0%", "25%", "100%"],
         "answer": 1},
        {"q": "Is a risk a diagnosis?",
         "options": ["Yes", "No"],
         "answer": 1},
    ],
}
