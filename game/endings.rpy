# ════════════════════════════════════════════════════════
# SUMMER SHIFT – endings.rpy
# Fins : Bad / Normal / Good × 4 filles
# ════════════════════════════════════════════════════════

# ════════════════════════════════════════════════════════
# LINA
# ════════════════════════════════════════════════════════

label ending_lina_bad:
    scene bg beach
    with fade
    show lina happy at right

    n "Dernier jour. Le taxi attend."
    n "Lina agite la main depuis l'entrée du resort avec son grand sourire."
    lina "Hé ! Reviens nous voir !"
    alex "Promis."
    n "Je monte dans le taxi."
    n "On s'est bien entendus. C'était bien."
    n "Mais c'est resté là."
    n "Un bel été avec quelqu'un de bien."
    n "Je regarde le resort disparaître dans le rétroviseur."

    hide lina happy

    n " "
    n "{b}FIN – Route Lina (Amis){/b}"
    n "{i}Lina est restée dans ta mémoire comme un éclat de soleil – vif, chaud, et déjà loin.{/i}"
    return

label ending_lina_normal:
    scene bg beach
    with fade
    show lina happy at right

    n "Le taxi est là. Ma valise aussi."
    lina "...C'est l'heure ?"
    alex "Ouais."
    lina "C'était bien."
    alex "Très."
    n "On se regarde. Il y a quelque chose qu'on n'a pas tout à fait dit."
    lina "Alex. Est-ce que tu reviens ?"
    alex "Est-ce que tu veux que je revienne ?"
    lina "Je te pose la question, donc oui !"
    n "Je ris. Elle rit."
    n "Je l'embrasse — rapidement, honnêtement — et je monte dans le taxi."

    hide lina happy

    n " "
    n "{b}FIN – Route Lina (Promesse){/b}"
    n "{i}Lina t'a envoyé un message deux heures après ton départ. Il disait juste : 'Alors ?'{/i}"
    n "{i}Tu as répondu : 'Je reviens dans trois semaines.'{/i}"
    n "{i}Elle a répondu un seul emoji. Le plus grand sourire disponible.{/i}"
    return

label ending_lina_good:
    scene bg beach_soir
    with fade
    show lina swimsuit at right

    n "Le taxi ne vient qu'à 18h. Il est 15h."
    n "Lina m'a pris par la main et m'a emmené sur la plage."
    lina "Dernière session."
    alex "Dernier bain."
    lina "Dernier coucher de soleil aussi ?"
    alex "On verra s'il est à l'heure."

    n "On reste dans l'eau jusqu'à ce que le soleil commence à descendre."
    n "Elle nage vers moi et s'arrête à quelques centimètres."

    lina "Alex."
    alex "Lina."
    lina "Si tu reviens pas, je te retrouve."
    alex "C'est une menace ?"
    lina "Non. C'est une déclaration d'intention."
    alex "Je reviens."
    lina "Je sais."

    n "On s'embrasse dans l'eau jusqu'à ce que le taxi klaxonne."
    n "Le chauffeur doit attendre cinq minutes."

    hide lina swimsuit

    n " "
    n "{b}FIN – Route Lina (Good End){/b}"
    n "{i}Lina a pris deux week-ends sur trois pour venir te voir à la ville cet automne.{/i}"
    n "{i}Elle a renversé deux cafés dans ton appartement. Tu as arrêté de compter.{/i}"
    n "{i}L'année suivante, vous êtes revenus à La Vague Dorée. Cette fois en couple officiel.{/i}"
    return

# ════════════════════════════════════════════════════════
# MINA
# ════════════════════════════════════════════════════════

label ending_mina_bad:
    scene bg kitchen
    with fade
    show mina shy at right

    n "Matin du départ. Je passe dire au revoir à Mina."
    mina "Je... j'ai préparé des sablés pour le train."
    alex "Tu n'aurais pas dû."
    mina "Si. C'est ma façon de dire... bonne route."
    n "Je prends les sablés. On se fait une bise maladroite."
    n "Il y avait quelque chose entre nous que ni l'un ni l'autre n'a su formuler à temps."

    hide mina shy

    n " "
    n "{b}FIN – Route Mina (Amis){/b}"
    n "{i}Les sablés étaient parfaits. Tu les as mangés tous dans le train.{/i}"
    n "{i}Tu as pensé à elle à chaque bouchée.{/i}"
    return

label ending_mina_normal:
    scene bg kitchen
    with fade
    show mina happy at right

    n "Dernier matin. Mina m'attend en cuisine avec un café et un sourire timide."
    mina "Je voulais que ton dernier souvenir de cet endroit soit bon."
    alex "Tous mes souvenirs d'ici sont bons."
    mina "Le café aide quand même."
    n "On boit côte à côte, en silence, regardant le jardin par la fenêtre."
    mina "Alex."
    alex "Mina."
    mina "Je sais pas si on se reverra."
    alex "Moi si."
    mina "...Comment tu peux savoir ?"
    alex "Parce que je veux que ça arrive."

    n "Elle me regarde longtemps. Puis elle hoche la tête, une fois, discrètement."

    hide mina happy

    n " "
    n "{b}FIN – Route Mina (Promesse){/b}"
    n "{i}Mina t'a envoyé une photo trois jours après ton départ.{/i}"
    n "{i}Une assiette de sablés avec la légende : 'Test de la recette 47. Manque d'un avis.'{/i}"
    n "{i}Tu as pris le train le week-end suivant.{/i}"
    return

label ending_mina_good:
    scene bg kitchen
    with fade
    show mina happy at right

    n "Dernier matin. Mina a cuisiné un vrai petit-déjeuner pour deux."
    n "Pas pour le resort. Pour nous."

    mina "J'ai réfléchi à quelque chose."
    alex "Quoi ?"
    mina "Mon restaurant. Celui que je voulais."
    mina "Je crois que j'ai assez attendu."
    alex "Tu vas le faire ?"
    mina "Je sais pas encore comment. Mais... oui."
    alex "Mina."
    mina "Quoi."
    alex "T'auras un client fidèle dès le premier jour."

    n "Elle pleure un peu. Elle s'en excuse. Je lui dis que c'est pas nécessaire."

    hide mina happy
    show mina blush at right

    mina "Alex. Reste encore un peu ?"
    alex "Mon train est à 18h."
    mina "Il est 8h du matin."
    alex "Alors j'ai le temps."

    hide mina blush

    n " "
    n "{b}FIN – Route Mina (Good End){/b}"
    n "{i}Le restaurant de Mina a ouvert dix mois plus tard, dans une petite rue du centre.{/i}"
    n "{i}Le premier soir, la table du coin était réservée pour Alex.{/i}"
    n "{i}Il est arrivé avec des fleurs et un tablier (cadeau, au cas où elle aurait besoin d'aide).{/i}"
    n "{i}Elle a ri et l'a mis directement au travail.{/i}"
    return

# ════════════════════════════════════════════════════════
# SOFIA
# ════════════════════════════════════════════════════════

label ending_sofia_bad:
    scene bg resort
    with fade
    show sofia confident at right

    n "Dernier jour. Sofia me serre la main fermement."
    sofia "Tu as bien travaillé, Alex. Si tu cherches un job l'été prochain..."
    alex "Je reviendrai."
    sofia "Je t'en serai reconnaissante."
    n "C'est professionnel, chaleureux, et rien de plus."
    n "Le taxi arrive. Je charge ma valise."

    hide sofia confident

    n " "
    n "{b}FIN – Route Sofia (Professionnel){/b}"
    n "{i}Tu es revenu l'été suivant comme employé.{/i}"
    n "{i}Sofia était contente de te voir. Professionnellement parlant.{/i}"
    n "{i}Ça aussi, c'est une forme de fidélité.{/i}"
    return

label ending_sofia_normal:
    scene bg terrace
    with fade
    show sofia soft at right

    n "Dernier matin. Sofia sur la terrasse, café à la main, regard sur la mer."
    n "Elle m'entend arriver et se tourne."

    sofia "Je me disais justement..."
    alex "Quoi ?"
    sofia "Que les étés qui comptent laissent une trace."
    sofia "Celui-ci en laissera une."
    alex "Pour moi aussi."

    n "On reste là un moment, sans rien de plus."
    n "Le taxi klaxonne."
    n "Sofia me pose la main sur le bras — une seconde, deux — et la retire."

    sofia "Bonne route, Alex."
    alex "À bientôt, Sofia."

    hide sofia soft

    n " "
    n "{b}FIN – Route Sofia (À bientôt){/b}"
    n "{i}Sofia t'a envoyé un e-mail quatre jours plus tard.{/i}"
    n "{i}Objet : 'Réservation'. Corps : 'La chambre 3 est libre le premier week-end de septembre.'{/i}"
    n "{i}Tu as répondu : 'Je prends.'{/i}"
    return

label ending_sofia_good:
    scene bg terrace
    with fade
    show sofia soft at right

    n "Le matin du dernier jour. On est tous les deux debout avant les autres."
    n "Café, terrasse, mer."
    n "On n'a pas besoin de beaucoup de mots."

    sofia "Alex."
    alex "Sofia."
    sofia "Tu sais que j'ai peur de peu de choses."
    alex "Je sais."
    sofia "Toi, un peu."
    alex "Dans quel sens ?"
    sofia "Dans le sens où tu pourrais compter. Et que ça fait longtemps que quelqu'un comptait pas vraiment."

    n "Je pose ma main sur la sienne."

    alex "Je compte. Et je reviendrai."
    sofia "Je le saurais si c'était faux."
    alex "C'est pour ça que c'est vrai."

    n "Elle sourit — ce vrai sourire que j'ai mis quatre jours à obtenir."
    n "Le taxi arrive à 18h. Elle m'accompagne jusqu'à la porte."
    n "Elle m'embrasse — discrètement, avec élégance — et reste sur le seuil jusqu'à ce que le taxi disparaisse."

    hide sofia soft

    n " "
    n "{b}FIN – Route Sofia (Good End){/b}"
    n "{i}Sofia n'est pas du genre à appeler tous les jours.{/i}"
    n "{i}Mais chaque vendredi soir, il y a un message. Court, précis, sincère.{/i}"
    n "{i}Et chaque troisième week-end du mois, il y a un trajet en train vers la côte.{/i}"
    n "{i}La chambre 3 t'attend toujours.{/i}"
    return

# ════════════════════════════════════════════════════════
# CLARA
# ════════════════════════════════════════════════════════

label ending_clara_bad:
    scene bg resort
    with fade

    n "Clara est repartie le matin du Jour 6."
    n "On s'est dit au revoir poliment."
    n "Elle avait l'air de vouloir dire autre chose."
    n "Moi aussi."
    n "Mais aucun de nous deux a eu le courage."

    n " "
    n "{b}FIN – Route Clara (Passés sans se croiser){/b}"
    n "{i}Tu as trouvé son profil par hasard sur les réseaux sociaux, six mois plus tard.{/i}"
    n "{i}Tu as hésité à suivre. Tu as suivi.{/i}"
    n "{i}Elle t'a suivi en retour deux heures après.{/i}"
    return

label ending_clara_normal:
    scene bg resort
    with fade
    show clara tsundere at right

    n "Clara part le Jour 6 au matin. Elle a ses bagages à la main."
    n "Je la rejoins dans l'entrée."

    clara "T'as pas à venir me dire au revoir."
    alex "Je sais. Je viens quand même."
    clara "..."
    clara "T'es chiant."
    alex "Oui."

    n "Un silence. Elle regarde ses pieds."

    clara "...C'était bien, cette semaine. Même si t'es là."
    alex "Je prends ça comme un compliment."
    clara "T'as bien fait."

    n "La voiture de Sofia arrive. Clara monte. Se retourne une dernière fois."

    clara "Alex."
    alex "Clara."
    clara "...Rien. Bonne journée."

    hide clara tsundere

    n " "
    n "{b}FIN – Route Clara (Tsundere jusqu'au bout){/b}"
    n "{i}Clara t'a envoyé un mème trois jours plus tard sans aucun contexte.{/i}"
    n "{i}Tu as répondu avec un mème encore meilleur.{/i}"
    n "{i}C'est comme ça que ça a commencé.{/i}"
    return

label ending_clara_good:
    scene bg resort
    with fade
    show clara shy at right

    n "Clara part le Jour 6 à l'aube."
    n "Je l'entends bouger dans le couloir et me lève."

    clara "Je voulais pas te réveiller."
    alex "Je dormais pas."
    clara "..."
    clara "Moi non plus."

    n "On reste dans le couloir désert à ne rien faire."
    n "Puis elle se penche en avant et me serre dans ses bras — vite, maladroitement, sincèrement."

    clara "C'était une bonne semaine."
    alex "La meilleure de l'été."
    clara "...C'était ton seul été d'été ici."
    alex "Exactement."

    n "Elle rit dans mon épaule."
    n "Elle s'écarte. Ses yeux sont brillants mais elle refuse de l'admettre."

    clara "Quand tu repasses par là..."
    alex "Je te préviens."
    clara "Ouais. Fais ça."

    n "Le taxi de Sofia l'emmène à 6h15."
    n "Je reste sur le seuil jusqu'à ce que les feux arrière disparaissent."

    hide clara shy

    n " "
    n "{b}FIN – Route Clara (Good End){/b}"
    n "{i}Clara t'a envoyé un message à 7h du matin depuis la voiture.{/i}"
    n "{i}Un simple : 'Ouais donc c'était bien.'{/i}"
    n "{i}Tu as répondu : 'Je sais.'{/i}"
    n "{i}Et vous avez parlé jusqu'à ce qu'elle arrive chez elle.{/i}"
    return
