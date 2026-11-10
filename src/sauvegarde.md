---
title: "Sauvegarde, restauration et données"
slug: sauvegarde
group: "Compte et données"
order: 15
description: "Sauvegarde automatique, code de récupération, changement d'iPhone, fichiers, hors ligne, vie privée"
notion: 4104095d0a7881308ef3f920fa51aae8
---
Cette page explique où sont tes données, comment elles sont sauvegardées, comment les retrouver sur un nouvel iPhone, et ce qui marche sans réseau.

<table-of-contents />

## Où sont tes données

Ton suivi s'appelle le journal : chaque série, chaque ressenti, chaque début et fin de séance y est noté avec sa date et son heure. Une saisie n'est jamais modifiée : une correction ajoute une nouvelle saisie, et la dernière fait foi.

Le journal et tes réglages sont enregistrés sur ton iPhone, dans l'appli. Sans sauvegarde, ils n'existent que là.

Si l'enregistrement échoue, l'appli affiche <b>Enregistrement impossible : sauvegarde ton journal depuis l'onglet Progrès.</b> Suis la procédure Sauvegarder dans un fichier, plus bas.

## La sauvegarde automatique

Elle est activée au départ. Après chaque séance terminée, une copie de ton journal et de tes réglages part sur le serveur de Steady. Steady vérifie aussi à chaque ouverture que la dernière copie est à jour.

L'appli le résume dans les réglages : <b>Après chaque séance, ton journal est copié sur le serveur de Steady. Rien d'autre n'y est envoyé.</b>

Dans <b>Réglages</b>, section <b>Sauvegarde</b> :

- l'interrupteur <b>Sauvegarde automatique</b> ;
- la date de la dernière copie, par exemple <b>Dernière : 06/11/2026 18:45</b>, ou <b>Pas encore sauvegardé</b> ;
- le bouton <b>Sauvegarder</b>, pour faire une copie tout de suite. L'appli affiche <b>Journal sauvegardé sur le serveur de Steady</b>, ou <b>Sauvegarde impossible : vérifie ta connexion.</b> ;
- ton code de récupération, avec <b>Copier</b> ;
- le bouton <b>Restaurer avec un code</b>.

Ces actions s'appliquent tout de suite, sans toucher <b>Enregistrer</b>.

Tu désactives <b>Sauvegarde automatique</b> : la copie gardée sur le serveur est supprimée et l'appli affiche <b>Sauvegarde automatique coupée, copie du serveur supprimée</b>.

## Le code de récupération

Le code de récupération est une longue suite de lettres et de chiffres, propre à ton iPhone. Il apparaît dans la section <b>Sauvegarde</b> après ta première copie automatique ou après l'activation des notifications. L'appli précise : <b>Code de récupération, pour restaurer ton suivi sur un nouvel iPhone. Ne le partage pas.</b>

Toute personne qui a ce code peut lire ton journal : garde-le pour toi.

Pour le noter :

1. Ouvre <b>Réglages</b>, section <b>Sauvegarde</b>.
2. Touche <b>Copier</b>. L'appli affiche <b>Code copié</b>.
3. Colle le code dans un endroit sûr, par exemple tes notes ou ton gestionnaire de mots de passe.

Si la copie échoue, l'appli affiche <b>Copie impossible : sélectionne le code à la main.</b> Touche le code pour le sélectionner, puis copie-le.

## Restaurer ton suivi sur un nouvel iPhone

1. Installe Steady sur le nouvel iPhone. Voir la page <mention url="https://app.notion.com/p/4104095d0a7881cbaa8ef7be79c7d001">Installer Steady sur l'iPhone</mention>.
2. Sur l'écran d'accueil de l'appli, touche <b>J'ai un code de récupération</b>. Si l'appli est déjà réglée, ouvre plutôt <b>Réglages</b>, section <b>Sauvegarde</b>, et touche <b>Restaurer avec un code</b>.
3. Dans <b>Restaurer ton suivi</b>, colle ton code.
4. Touche <b>Restaurer</b>.
5. Si ce nouvel iPhone a déjà un suivi, confirme avec <b>Remplacer</b>.

Résultat : l'appli affiche <b>Suivi restauré</b> avec le nombre de séances retrouvées, puis <b>Ma semaine</b>.

Après la restauration :

- ton journal et tes réglages sont ceux de la sauvegarde ;
- ton programme est recréé à partir de tes réglages et un nouveau cycle commence cette semaine ;
- les notifications sont désactivées : active-les à nouveau. Voir la page <mention url="https://app.notion.com/p/4104095d0a7881e98e1bce6fa537513e">Activer les notifications</mention>.

| Message | Que faire |
| --- | --- |
| <b>Code invalide : vérifie qu'il est complet.</b> | Recopie le code en entier |
| <b>Aucune sauvegarde pour ce code.</b> | Vérifie le code ; la sauvegarde automatique était peut-être coupée sur l'ancien iPhone |
| <b>Restauration impossible : vérifie ta connexion.</b> | Connecte-toi à internet et réessaie |
| <b>Sauvegarde illisible.</b> | La copie du serveur n'est pas lisible : utilise un fichier de sauvegarde si tu en as un |

## Sauvegarder dans un fichier

En plus de la sauvegarde automatique, tu peux enregistrer ton journal dans un fichier, par exemple dans iCloud Drive.

1. Ouvre l'onglet <b>Progrès</b>.
2. Descends jusqu'à la carte <b>Mes données</b>.
3. Touche <b>Sauvegarder</b>.
4. Dans la feuille de partage de l'iPhone, choisis où enregistrer le fichier (Fichiers, iCloud Drive, AirDrop...).

Résultat : un fichier nommé muscu-auto suivi de la date (par exemple muscu-auto-2026-11-06.json) est créé, et l'appli affiche <b>Journal sauvegardé</b>. Il contient ton journal et tes réglages.

La carte <b>Mes données</b> affiche la date de ta dernière sauvegarde, dans un fichier ou automatique, ou <b>Jamais sauvegardé.</b>

### Le rappel de sauvegarde

Sans aucune copie depuis 14 jours (ni fichier, ni sauvegarde automatique), la carte <b>Sauvegarde ton journal</b> apparaît sur <b>Ma semaine</b>. Tu la touches : la feuille de partage s'ouvre, comme avec <b>Sauvegarder</b>.

## Importer un fichier de sauvegarde

1. Ouvre l'onglet <b>Progrès</b>, carte <b>Mes données</b>.
2. Touche <b>Importer</b>.
3. Choisis ton fichier de sauvegarde.
4. Dans <b>Remplacer ton historique ?</b>, vérifie le nombre de saisies et touche <b>Remplacer</b>.

Résultat : ton journal est remplacé par celui du fichier et l'appli affiche <b>Historique importé</b>. Seul le journal est remplacé : tes réglages et ton programme ne changent pas.

Si le fichier n'est pas une sauvegarde de Steady, l'appli affiche <b>Fichier invalide : choisis une sauvegarde JSON de Steady.</b>

## Exporter en tableau

Le bouton <b>Exporter CSV</b> de la carte <b>Mes données</b> crée un fichier lisible dans un tableur (Numbers, Excel), avec une ligne par saisie du journal. Certaines valeurs sont des codes en anglais :

| Colonne | Contenu |
| --- | --- |
| horodatage | Date et heure de la saisie |
| type | Nature de la saisie, par exemple set (série), start (début de séance), end (fin de séance), feel (ressenti), tech (technique), pause, resume (reprise), cancel (abandon) |
| seance | Identifiant de la séance (sa date et son heure de début) |
| jour | Jour de la séance, ou Séance libre pour une séance hors programme |
| exercice\_id, exercice | Numéro et nom de l'exercice |
| serie | Numéro de la série |
| kg | Charge (0 au poids du corps) |
| repetitions | Répétitions ou secondes |
| mode | tempo (descente lente) ou pause, le cas échéant |
| technique\_ok | Réponse à <b>Technique propre ?</b> : true (oui) ou false (non) |
| ressenti | easy (facile), ok (bien), hard (dur) ou pain (douleur) |

## Utiliser Steady hors ligne

Sans réseau, le bandeau <b>Hors ligne</b> s'affiche : <b>Tes séances marchent et tes saisies restent sur l'iPhone. L'écran projeté, la sauvegarde et les vidéos attendent le réseau.</b> Au retour du réseau, l'appli affiche <b>De retour en ligne</b>.

| Fonctionne sans réseau | A besoin du réseau |
| --- | --- |
| Programme, séance, saisie des séries | Vidéos des exercices |
| Minuteur de repos et bips | Écran projeté et miroir |
| Images, muscles et consignes des fiches | Caméra, la première fois seulement |
| Onglet <b>Progrès</b>, export, fichier de sauvegarde | Sauvegarde automatique et restauration |
|  | Activation et réglage des notifications |
|  | Mise à jour de l'appli |

Tes saisies hors ligne sont gardées sur l'iPhone. La sauvegarde automatique se rattrape à la prochaine ouverture avec du réseau.

## Ta vie privée, simplement

| Quoi | Où ça va |
| --- | --- |
| Ton journal et tes réglages | Sur ton iPhone. Une copie sur le serveur de Steady si la sauvegarde automatique est active |
| Tes notifications | Le serveur garde ce qu'il faut pour te prévenir à l'heure : tes jours, ton heure de séance, le nom des séances, la date de ta dernière série, ton fuseau horaire et l'heure de fin du repos en cours |
| La séance projetée | Elle passe par le serveur de Steady pour aller à l'écran. Le dernier état affiché est gardé, pour qu'un écran rechargé le retrouve |
| L'image des caméras | Le comptage se fait sur l'appareil. Aucune image n'est envoyée au serveur. Avec le miroir, la vidéo de l'iPhone va directement à l'écran. L'outil de suivi du corps est téléchargé une fois depuis internet |
| Les vidéos des exercices | Elles sont lues depuis le site [wger.de](http://wger.de) |
| <b>Me filmer</b> | La vidéo n'est pas enregistrée |
| <b>Copier pour Claude</b> | Le texte est seulement copié : c'est toi qui choisis de le coller |

Le serveur de Steady est hébergé chez Cloudflare.
