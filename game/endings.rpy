# ════════════════════════════════════════════════════════
# SUMMER SHIFT – endings.rpy
# Fins : Bad / Normal / Good × 4 filles
# ════════════════════════════════════════════════════════

# ════════════════════════════════════════════════════════
# LINA
# ════════════════════════════════════════════════════════

label ending_zara_bad:
    scene bg beach
    with fade
    show zara happy at right

    n "Dernier jour. Le taxi attend."
    n "Zara agite la main depuis l'entrée du resort avec son grand sourire."
    zara "Hé ! Reviens nous voir !"
    elio "Promis."
    n "Je monte dans le taxi."
    n "On s'est bien entendus. C'était bien."
    n "Mais c'est resté là."
    n "Un bel été avec quelqu'un de bien."
    n "Je regarde le resort disparaître dans le rétroviseur."

    hide zara happy

    n " "
    n "{b}FIN – Route Zara (Amis){/b}"
    n "{i}Zara est restée dans ta mémoire comme un éclat de soleil – vif, chaud, et déjà loin.{/i}"
    return

label ending_zara_normal:
    scene bg beach
    with fade
    show zara happy at right

    n "Le taxi est là. Ma valise aussi."
    zara "...C'est l'heure ?"
    elio "Ouais."
    zara "C'était bien."
    elio "Très."
    n "On se regarde. Il y a quelque chose qu'on n'a pas tout à fait dit."
    zara "Elio. Est-ce que tu reviens ?"
    elio "Est-ce que tu veux que je revienne ?"
    zara "Je te pose la question, donc oui !"
    n "Je ris. Elle rit."
    n "Je l'embrasse — rapidement, honnêtement — et je monte dans le taxi."

    hide zara happy

    n " "
    n "{b}FIN – Route Zara (Promesse){/b}"
    n "{i}Zara t'a envoyé un message deux heures après ton départ. Il disait juste : 'Alors ?'{/i}"
    n "{i}Tu as répondu : 'Je reviens dans trois semaines.'{/i}"
    n "{i}Elle a répondu un seul emoji. Le plus grand sourire disponible.{/i}"
    return

label ending_zara_good:
    scene bg beach_soir
    with fade
    show zara swimsuit at right

    n "Le taxi ne vient qu'à 18h. Il est 15h."
    n "Zara m'a pris par la main et m'a emmené sur la plage."
    zara "Dernière session."
    elio "Dernier bain."
    zara "Dernier coucher de soleil aussi ?"
    elio "On verra s'il est à l'heure."

    n "On reste dans l'eau jusqu'à ce que le soleil commence à descendre."
    n "Elle nage vers moi et s'arrête à quelques centimètres."

    zara "Elio."
    elio "Zara."
    zara "Si tu reviens pas, je te retrouve."
    elio "C'est une menace ?"
    zara "Non. C'est une déloution d'intention."
    elio "Je reviens."
    zara "Je sais."

    n "On s'embrasse dans l'eau jusqu'à ce que le taxi klaxonne."
    n "Le chauffeur doit attendre cinq minutes."

    hide zara swimsuit

    n " "
    n "{b}FIN – Route Zara (Good End){/b}"
    n "{i}Zara a pris deux week-ends sur trois pour venir te voir à la ville cet automne.{/i}"
    n "{i}Elle a renversé deux cafés dans ton appartement. Tu as arrêté de compter.{/i}"
    n "{i}L'année suivante, vous êtes revenus à La Vague Dorée. Cette fois en couple officiel.{/i}"
    return

# ════════════════════════════════════════════════════════
# MINA
# ════════════════════════════════════════════════════════

label ending_vesna_bad:
    scene bg kitchen
    with fade
    show vesna shy at right

    n "Matin du départ. Je passe dire au revoir à Vesna."
    vesna "Je... j'ai préparé des sablés pour le train."
    elio "Tu n'aurais pas dû."
    vesna "Si. C'est ma façon de dire... bonne route."
    n "Je prends les sablés. On se fait une bise maladroite."
    n "Il y avait quelque chose entre nous que ni l'un ni l'autre n'a su formuler à temps."

    hide vesna shy

    n " "
    n "{b}FIN – Route Vesna (Amis){/b}"
    n "{i}Les sablés étaient parfaits. Tu les as mangés tous dans le train.{/i}"
    n "{i}Tu as pensé à elle à chaque bouchée.{/i}"
    return

label ending_vesna_normal:
    scene bg kitchen
    with fade
    show vesna happy at right

    n "Dernier matin. Vesna m'attend en cuisine avec un café et un sourire timide."
    vesna "Je voulais que ton dernier souvenir de cet endroit soit bon."
    elio "Tous mes souvenirs d'ici sont bons."
    vesna "Le café aide quand même."
    n "On boit côte à côte, en silence, regardant le jardin par la fenêtre."
    vesna "Elio."
    elio "Vesna."
    vesna "Je sais pas si on se reverra."
    elio "Moi si."
    vesna "...Comment tu peux savoir ?"
    elio "Parce que je veux que ça arrive."

    n "Elle me regarde longtemps. Puis elle hoche la tête, une fois, discrètement."

    hide vesna happy

    n " "
    n "{b}FIN – Route Vesna (Promesse){/b}"
    n "{i}Vesna t'a envoyé une photo trois jours après ton départ.{/i}"
    n "{i}Une assiette de sablés avec la légende : 'Test de la recette 47. Manque d'un avis.'{/i}"
    n "{i}Tu as pris le train le week-end suivant.{/i}"
    return

label ending_vesna_good:
    scene bg kitchen
    with fade
    show vesna happy at right

    n "Dernier matin. Vesna a cuisiné un vrai petit-déjeuner pour deux."
    n "Pas pour le resort. Pour nous."

    vesna "J'ai réfléchi à quelque chose."
    elio "Quoi ?"
    vesna "Mon restaurant. Celui que je voulais."
    vesna "Je crois que j'ai assez attendu."
    elio "Tu vas le faire ?"
    vesna "Je sais pas encore comment. Mais... oui."
    elio "Vesna."
    vesna "Quoi."
    elio "T'auras un client fidèle dès le premier jour."

    n "Elle pleure un peu. Elle s'en excuse. Je lui dis que c'est pas nécessaire."

    hide vesna happy
    show vesna blush at right

    vesna "Elio. Reste encore un peu ?"
    elio "Mon train est à 18h."
    vesna "Il est 8h du matin."
    elio "Alors j'ai le temps."

    hide vesna blush

    n " "
    n "{b}FIN – Route Vesna (Good End){/b}"
    n "{i}Le restaurant de Vesna a ouvert dix mois plus tard, dans une petite rue du centre.{/i}"
    n "{i}Le premier soir, la table du coin était réservée pour Elio.{/i}"
    n "{i}Il est arrivé avec des fleurs et un tablier (cadeau, au cas où elle aurait besoin d'aide).{/i}"
    n "{i}Elle a ri et l'a mis directement au travail.{/i}"
    return

# ════════════════════════════════════════════════════════
# SOFIA
# ════════════════════════════════════════════════════════

label ending_ines_bad:
    scene bg resort
    with fade
    show ines confident at right

    n "Dernier jour. Ines me serre la main fermement."
    ines "Tu as bien travaillé, Elio. Si tu cherches un job l'été prochain..."
    elio "Je reviendrai."
    ines "Je t'en serai reconnaissante."
    n "C'est professionnel, chaleureux, et rien de plus."
    n "Le taxi arrive. Je charge ma valise."

    hide ines confident

    n " "
    n "{b}FIN – Route Ines (Professionnel){/b}"
    n "{i}Tu es revenu l'été suivant comme employé.{/i}"
    n "{i}Ines était contente de te voir. Professionnellement parlant.{/i}"
    n "{i}Ça aussi, c'est une forme de fidélité.{/i}"
    return

label ending_ines_normal:
    scene bg terrace
    with fade
    show ines soft at right

    n "Dernier matin. Ines sur la terrasse, café à la main, regard sur la mer."
    n "Elle m'entend arriver et se tourne."

    ines "Je me disais justement..."
    elio "Quoi ?"
    ines "Que les étés qui comptent laissent une trace."
    ines "Celui-ci en laissera une."
    elio "Pour moi aussi."

    n "On reste là un moment, sans rien de plus."
    n "Le taxi klaxonne."
    n "Ines me pose la main sur le bras — une seconde, deux — et la retire."

    ines "Bonne route, Elio."
    elio "À bientôt, Ines."

    hide ines soft

    n " "
    n "{b}FIN – Route Ines (À bientôt){/b}"
    n "{i}Ines t'a envoyé un e-mail quatre jours plus tard.{/i}"
    n "{i}Objet : 'Réservation'. Corps : 'La chambre 3 est libre le premier week-end de septembre.'{/i}"
    n "{i}Tu as répondu : 'Je prends.'{/i}"
    return

label ending_ines_good:
    scene bg terrace
    with fade
    show ines soft at right

    n "Le matin du dernier jour. On est tous les deux debout avant les autres."
    n "Café, terrasse, mer."
    n "On n'a pas besoin de beaucoup de mots."

    ines "Elio."
    elio "Ines."
    ines "Tu sais que j'ai peur de peu de choses."
    elio "Je sais."
    ines "Toi, un peu."
    elio "Dans quel sens ?"
    ines "Dans le sens où tu pourrais compter. Et que ça fait longtemps que quelqu'un comptait pas vraiment."

    n "Je pose ma main sur la sienne."

    elio "Je compte. Et je reviendrai."
    ines "Je le saurais si c'était faux."
    elio "C'est pour ça que c'est vrai."

    n "Elle sourit — ce vrai sourire que j'ai mis quatre jours à obtenir."
    n "Le taxi arrive à 18h. Elle m'accompagne jusqu'à la porte."
    n "Elle m'embrasse — discrètement, avec élégance — et reste sur le seuil jusqu'à ce que le taxi disparaisse."

    hide ines soft

    n " "
    n "{b}FIN – Route Ines (Good End){/b}"
    n "{i}Ines n'est pas du genre à appeler tous les jours.{/i}"
    n "{i}Mais chaque vendredi soir, il y a un message. Court, précis, sincère.{/i}"
    n "{i}Et chaque troisième week-end du mois, il y a un trajet en train vers la côte.{/i}"
    n "{i}La chambre 3 t'attend toujours.{/i}"
    return

# ════════════════════════════════════════════════════════
# CLARA
# ════════════════════════════════════════════════════════

label ending_lou_bad:
    scene bg resort
    with fade

    n "Lou est repartie le matin du Jour 6."
    n "On s'est dit au revoir poliment."
    n "Elle avait l'air de vouloir dire autre chose."
    n "Moi aussi."
    n "Mais aucun de nous deux a eu le courage."

    n " "
    n "{b}FIN – Route Lou (Passés sans se croiser){/b}"
    n "{i}Tu as trouvé son profil par hasard sur les réseaux sociaux, six mois plus tard.{/i}"
    n "{i}Tu as hésité à suivre. Tu as suivi.{/i}"
    n "{i}Elle t'a suivi en retour deux heures après.{/i}"
    return

label ending_lou_normal:
    scene bg resort
    with fade
    show lou tsundere at right

    n "Lou part le Jour 6 au matin. Elle a ses bagages à la main."
    n "Je la rejoins dans l'entrée."

    lou "T'as pas à venir me dire au revoir."
    elio "Je sais. Je viens quand même."
    lou "..."
    lou "T'es chiant."
    elio "Oui."

    n "Un silence. Elle regarde ses pieds."

    lou "...C'était bien, cette semaine. Même si t'es là."
    elio "Je prends ça comme un compliment."
    lou "T'as bien fait."

    n "La voiture de Ines arrive. Lou monte. Se retourne une dernière fois."

    lou "Elio."
    elio "Lou."
    lou "...Rien. Bonne journée."

    hide lou tsundere

    n " "
    n "{b}FIN – Route Lou (Tsundere jusqu'au bout){/b}"
    n "{i}Lou t'a envoyé un mème trois jours plus tard sans aucun contexte.{/i}"
    n "{i}Tu as répondu avec un mème encore meilleur.{/i}"
    n "{i}C'est comme ça que ça a commencé.{/i}"
    return

label ending_lou_good:
    scene bg resort
    with fade
    show lou shy at right

    n "Lou part le Jour 6 à l'aube."
    n "Je l'entends bouger dans le couloir et me lève."

    lou "Je voulais pas te réveiller."
    elio "Je dormais pas."
    lou "..."
    lou "Moi non plus."

    n "On reste dans le couloir désert à ne rien faire."
    n "Puis elle se penche en avant et me serre dans ses bras — vite, maladroitement, sincèrement."

    lou "C'était une bonne semaine."
    elio "La meilleure de l'été."
    lou "...C'était ton seul été d'été ici."
    elio "Exactement."

    n "Elle rit dans mon épaule."
    n "Elle s'écarte. Ses yeux sont brillants mais elle refuse de l'admettre."

    lou "Quand tu repasses par là..."
    elio "Je te préviens."
    lou "Ouais. Fais ça."

    n "Le taxi de Ines l'emmène à 6h15."
    n "Je reste sur le seuil jusqu'à ce que les feux arrière disparaissent."

    hide lou shy

    n " "
    n "{b}FIN – Route Lou (Good End){/b}"
    n "{i}Lou t'a envoyé un message à 7h du matin depuis la voiture.{/i}"
    n "{i}Un simple : 'Ouais donc c'était bien.'{/i}"
    n "{i}Tu as répondu : 'Je sais.'{/i}"
    n "{i}Et vous avez parlé jusqu'à ce qu'elle arrive chez elle.{/i}"
    return
