# ════════════════════════════════════════════════════════
# SUMMER SHIFT – evening.rpy
# Scènes du soir — toutes filles, tous jours
# Affinité < 30 : brève rencontre
# Affinité 30-59 : flirtation légère
# Affinité ≥ 60 : scène intime (H légère)
# Affinité ≥ 80 : scène H complète
# Note : transition jour → day_router en fin de chaque bloc
# ════════════════════════════════════════════════════════

# ════════════════════════════════════════════════════════
# LINA – Soirées
# ════════════════════════════════════════════════════════

label ev_zara_d1:
    scene bg bar
    with dissolve
    show zara happy at right

    zara "Elio ! Tu m'aides à ranger le bar ?"
    elio "Bien sûr."
    n "On range en silence, avec ses blagues nulles en fond sonore."
    n "Je me rends compte que je suis souriant depuis une heure."
    zara "T'aimes les calembours ?"
    elio "Pas vraiment."
    zara "Alors j'en fais pas."
    elio "T'en fais quand même."
    zara "Ouais mais je les prévenais."

    hide zara happy
    $ current_day += 1
    jump day_router

label ev_zara_d2:
    scene bg terrace
    with dissolve
    show zara happy at right

    if affinity_zara >= 30:
        n "Zara est sur la terrasse avec deux limonades. Elle en tend une sans que je demande."
        zara "T'avais l'air d'en avoir besoin."
        elio "Tu lis dans les pensées ?"
        zara "Non, juste dans les mines défaites."
        n "On parle jusqu'au coucher du soleil. De tout et de rien. De ses projets, des miens."
        zara "Elio... tu penses qu'on se reverra après cette semaine ?"
        elio "Si ça dépend de moi, oui."
        zara "Ça me va."
        n "Elle sourit, les yeux sur la mer. Pas sur moi. Mais le sourire est pour moi."
    else:
        n "Zara passe en coup de vent, un plateau sous le bras."
        zara "Bonne nuit, Elio !"
        elio "Bonne nuit."

    hide zara happy
    $ current_day += 1
    jump day_router

label ev_zara_d3:
    scene bg beach_soir
    with dissolve
    show zara swimsuit at right

    if affinity_zara >= 40:
        n "Zara m'attend sur la plage au crépuscule. Elle dessine quelque chose dans le sable du bout du pied."
        zara "T'arrives ! Je pensais que t'avais oublié."
        elio "T'avais pas dit qu'on avait rendez-vous."
        zara "Je t'ai pas dit, mais t'es là quand même. Donc ça compte."
        n "On marche au bord de l'eau. Elle enlève ses tongs et les porte à la main."
        zara "Tu sais ce que j'aime dans mon travail ici ?"
        elio "Quoi ?"
        zara "Les soirées. Quand les touristes sont pas là et qu'on est juste... nous."
        zara "C'est rare que 'nous' soit bien."
        elio "Je comprends."
        n "Elle me prend le bras, spontanément, comme si c'était la chose la plus naturelle du monde."
        n "Je la laisse faire. C'est effectivement la chose la plus naturelle du monde."
    else:
        zara "Bonne nuit !"
        elio "Bonne nuit, Zara."

    hide zara swimsuit
    $ current_day += 1
    jump day_router

label ev_zara_d4:
    scene bg bar
    with dissolve
    show zara happy at right

    if affinity_zara >= 50:
        zara "Fermeture du bar. Tu restes ?"
        elio "Si tu veux de la compagnie."
        zara "Je pose la question, donc oui."
        n "Les lumières du bar sont basses. Zara prépare deux cocktails sans demander ce que je veux."
        zara "Goûte."
        n "C'est parfait. Doux, fruité, avec juste ce qu'il faut."
        elio "C'est excellent."
        zara "Je sais. Je suis bonne dans mon job."
        elio "T'es bonne dans plein de choses."
        n "Elle s'arrête. Me regarde."
        zara "...Vraiment ?"
        elio "Vraiment."
        n "Le bar est silencieux. La mer bruisse dehors. Le moment suspend."
        zara "Elio. Est-ce que je peux te faire un câlin ?"
        elio "Euh— oui, bien sûr."
        n "Elle passe les bras autour de mes épaules et reste là un long moment."
        n "C'est inattendu. C'est parfait."
    elif affinity_zara >= 30:
        zara "Cocktail de fin de journée ?"
        elio "Avec plaisir."
        n "On passe une heure agréable. Les mots se font rares, mais c'est bien."
    else:
        n "Le bar est fermé. Je passe devant, Zara éteint les lumières."
        zara "Bonne nuit !"

    hide zara happy
    $ current_day += 1
    jump day_router

label ev_zara_d5:
    scene bg beach_soir
    with dissolve
    show zara swimsuit at right

    if affinity_zara >= 60:
        n "La plage de nuit. Zara est là, les pieds dans l'eau, les étoiles au-dessus."
        n "Elle se retourne en m'entendant."
        zara "Je savais que tu viendrais."
        elio "C'est devenu un rituel."
        zara "Les bons trucs deviennent des rituels."
        n "On s'assoit côte à côte. Les vagues arrivent jusqu'à nos chevilles."
        zara "Elio..."
        elio "Hm ?"
        zara "Tu me plais. Je voulais juste le dire clairement. Sans blague nulle."
        elio "Tu me plais aussi, Zara. Beaucoup."
        n "Elle rit — ce rire franc que j'adore — et pose sa tête sur mon épaule."

        if affinity_zara >= 75:
            zara "On va pas rester là toute la nuit, quand même ?"
            elio "On peut faire autre chose ?"
            zara "On peut. Si tu veux."
            n "Elle me prend la main. On rentre vers le resort sous les étoiles."
            n "Sa porte. Ses yeux qui me regardent avec quelque chose d'évident."
            zara "T'as le droit de refuser."
            elio "Je veux pas refuser."
            zara "...Bien."
            scene bg room
            with dissolve
            n "La nuit passe doucement, entre rires étouffés et murmures."
            n "Zara est exactement comme je l'imaginais : entière, spontanée, et terriblement sincère."
            $ seen_zara_h1 = True
            $ affinity_zara += 15
            n "Le matin arrive trop vite."
            show zara blush at right
            zara "...T'as dormi ?"
            elio "Un peu."
            zara "Moi aussi. Un peu."
            n "Elle me sourit, les cheveux encore défaits. C'est la plus belle version d'elle."
            hide zara blush
        else:
            n "On reste sur la plage à regarder les étoiles jusqu'à minuit."
            n "Pas grand-chose ne se passe. Mais c'est exactement ce qu'il fallait."
    elif affinity_zara >= 35:
        zara "Soirée plage ?"
        n "On marche, on parle. Rien de plus. Pour l'instant."
    else:
        n "Je croise Zara dans le couloir."
        zara "Bonne nuit !"

    hide zara happy
    $ current_day += 1
    jump day_router

label ev_zara_d6:
    scene bg bar
    with dissolve
    show zara happy at right

    if affinity_zara >= 60:
        zara "Dernier soir. Tu veux qu'on marque le coup ?"
        elio "Comment ?"
        zara "J'ai accès au bar. Et à des recettes de cocktails que j'ai jamais essayées."
        elio "On risque quoi ?"
        zara "Un cocktail raté, ou quelque chose d'extraordinaire."
        n "On passe la soirée à tester des mélanges improbables."
        n "Certains sont immondes. D'autres sont géniaux."
        n "Vers minuit, Zara pose la tête sur le comptoir, mi-fatiguée, mi-heureuse."
        zara "Elio. Je suis contente que t'aies pris ce job."
        elio "Moi aussi."
        if seen_zara_h1:
            zara "...Tu viens ?"
            elio "Oui."
            scene bg room
            with dissolve
            n "La deuxième nuit ensemble est encore mieux que la première."
            n "On connaît les silences de l'autre. C'est plus facile."
            $ affinity_zara += 10
    else:
        n "Zara range le bar. On échange quelques mots."
        zara "Bonne nuit, Elio."

    hide zara happy
    $ current_day += 1
    jump day_router

# ════════════════════════════════════════════════════════
# MINA – Soirées
# ════════════════════════════════════════════════════════

label ev_vesna_d1:
    scene bg kitchen
    with dissolve
    show vesna shy at right

    vesna "Je... j'ai fait un dessert en trop. Si tu veux goûter."
    n "C'est un moelleux au chocolat encore tiède."
    n "Je ne dis rien pendant dix secondes. Je savoure."
    elio "Vesna. C'est incroyable."
    vesna "C'est juste un moelleux."
    elio "Non. C'est une œuvre d'art."
    n "Elle rougit et regarde ses mains."

    hide vesna shy
    $ current_day += 1
    jump day_router

label ev_vesna_d2:
    scene bg kitchen
    with dissolve
    show vesna happy at right

    if affinity_vesna >= 30:
        vesna "Tu veux qu'on prépare quelque chose ensemble ce soir ?"
        elio "Tu m'apprendras ?"
        vesna "Je vais essayer."
        n "On cuisine un risotto. Elle guide mes mains sur la casserole."
        n "Sa voix est douce, proche."
        vesna "Voilà. Comme ça. T'as le geste naturellement."
        n "Je doute que ce soit vrai, mais j'apprécie qu'elle le dise."
    else:
        vesna "Bonne nuit, Elio !"

    hide vesna happy
    $ current_day += 1
    jump day_router

label ev_vesna_d3:
    scene bg kitchen
    with dissolve
    show vesna blush at right

    if affinity_vesna >= 40:
        n "La cuisine après le service. Vesna prépare sa ganache au chocolat."
        n "Je reste à regarder, assis sur le plan de travail."
        vesna "Tu vas me porter malheur."
        elio "Les spectateurs portent malheur ?"
        vesna "Parfois."
        elio "Et si je participe ?"
        n "Elle me tend une spatule couverte de chocolat fondu."
        vesna "Goûte. Et dis-moi si c'est trop fort."
        n "Je goûte."
        elio "C'est parfait."
        vesna "T'es sûr ?"
        n "Pour toute réponse, je lui montre la spatule."
        n "Elle rit, cache son rire derrière sa main, puis se ravise et rit vraiment."
        n "C'est la première fois que je la vois rire comme ça."
    else:
        vesna "Le dessert est prêt, si tu veux."
        elio "Merci, Vesna."

    hide vesna blush
    $ current_day += 1
    jump day_router

label ev_vesna_d4:
    scene bg kitchen
    with dissolve
    show vesna happy at right

    if affinity_vesna >= 50:
        vesna "Ce soir, je teste la ganache spéciale."
        elio "Avec moi ?"
        vesna "Si tu veux. Tu es mon meilleur cobaye."
        n "Elle prépare un assortiment de chocolats avec une précision exquise."
        n "Pour chaque pièce, elle me demande mon avis. Je prends le rôle au sérieux."
        vesna "Celui-là."
        elio "...Il est fondant en bouche avec un goût de sel en fin."
        vesna "Exactement."
        n "On se regarde. Elle est proche. Plus proche qu'en cuisine d'habitude."
        vesna "Elio..."
        elio "Oui ?"
        vesna "Je... merci d'être là. Pour goûter. Pour tout."
        n "Je pose ma main sur la sienne. Elle ne la retire pas."
    elif affinity_vesna >= 30:
        n "On goûte les chocolats ensemble. Simple, doux, agréable."
    else:
        n "Vesna range sa cuisine. Je passe dire bonne nuit."

    hide vesna happy
    $ current_day += 1
    jump day_router

label ev_vesna_d5:
    scene bg spring
    with dissolve
    show vesna shy at right

    if affinity_vesna >= 60:
        n "La source chaude, la nuit. Vesna m'avait invité d'un texte mystérieux : {i}« Source chaude, 22h ? »{/i}"
        n "L'eau est à température parfaite. Le jardin sent le jasmin."
        vesna "T'as trouvé ?"
        elio "C'est toi qui m'as montré l'endroit."
        vesna "Je sais. Je voulais juste vérifier."
        n "On entre dans l'eau à tour de rôle. La chaleur monte doucement."
        vesna "Elio. Est-ce que tu... est-ce que t'as envie de rester, ce soir ?"
        n "Sa voix est à peine plus qu'un murmure."
        elio "Si tu me le demandes."
        vesna "Je te le demande."

        if affinity_vesna >= 75:
            scene bg room
            with dissolve
            n "La nuit passe entre le silence de la source chaude et la douceur de sa chambre."
            n "Vesna est douce et sincère. Elle murmure des choses en cuisine et en dehors."
            n "C'est intime d'une façon que je n'attendais pas."
            $ seen_vesna_h1 = True
            $ affinity_vesna += 15
            show vesna blush at right
            n "Le lendemain matin, elle pose une tasse de café sur ma table de chevet."
            n "Sans un mot. Juste un sourire."
            vesna "Le café est chaud."
            elio "Comme toujours."
            vesna "Oui."
            hide vesna blush
        else:
            n "On reste dans la source chaude à parler longtemps. Rien de plus."
            n "Mais ses mains frôlent les miennes dans l'eau."
    elif affinity_vesna >= 35:
        n "On prend le dessert ensemble sur la terrasse."
        vesna "Merci pour cette semaine, Elio."
    else:
        vesna "Bonne nuit !"

    hide vesna shy
    $ current_day += 1
    jump day_router

label ev_vesna_d6:
    scene bg kitchen
    with dissolve
    show vesna happy at right

    if affinity_vesna >= 60:
        vesna "Dernier dîner. J'ai préparé quelque chose de spécial."
        elio "Pour qui ?"
        vesna "Pour toi. Qui d'autre ?"
        n "Le repas est extraordinaire. Six plats, chacun meilleur que le précédent."
        n "On finit avec un fondant au chocolat à se damner."
        elio "Vesna. Si tu ouvres un restaurant, je suis le premier client."
        vesna "...T'es sérieux ?"
        elio "Je suis sérieux."
        n "Elle me regarde longtemps."
        vesna "Elio. Je veux pas que tu partes."
        elio "Moi non plus."
        if seen_vesna_h1:
            n "Elle prend ma main et me guide hors de la cuisine."
            scene bg room
            with dissolve
            n "La dernière nuit est parfaite."
            n "Le chocolat, la chaleur, et elle."
            $ affinity_vesna += 10
    else:
        n "Vesna prépare un dessert spécial. On le mange ensemble en silence."

    hide vesna happy
    $ current_day += 1
    jump day_router

# ════════════════════════════════════════════════════════
# SOFIA – Soirées
# ════════════════════════════════════════════════════════

label ev_ines_d1:
    scene bg terrace
    with dissolve
    show ines confident at right

    ines "Tu t'es bien installé ?"
    elio "Très bien, merci."
    ines "Bien. Demain 8h, petit-déjeuner commun."
    n "Elle va partir. Puis s'arrête."
    ines "Elio. Tu travailles bien. Je voulais le dire."
    n "Et elle repart. Ce compliment vaut de l'or."

    hide ines confident
    $ current_day += 1
    jump day_router

label ev_ines_d2:
    scene bg terrace
    with dissolve
    show ines soft at right

    if affinity_ines >= 30:
        n "Ines sur la terrasse, un verre de blanc à la main."
        n "Elle lève les yeux quand j'arrive."
        ines "Tu veux t'asseoir ?"
        elio "Si j'y suis invité."
        ines "Tu l'es."
        n "On parle. D'abord du resort, puis d'autre chose."
        ines "Tu étudies quoi ?"
        elio "Architecture. Première année."
        ines "Architecture..."
        ines "Ce resort a été construit par mon grand-père. Il était autodidacte."
        ines "Il aurait aimé que quelqu'un de ton âge s'intéresse à ces murs."
        n "Je regarde la bâtisse sous un angle nouveau."
    else:
        ines "Bonne nuit, Elio."

    hide ines soft
    $ current_day += 1
    jump day_router

label ev_ines_d3:
    scene bg terrace
    with dissolve
    show ines smirk at right

    if affinity_ines >= 40:
        n "Ines est là avec une bouteille de rouge ouverte et deux verres."
        ines "Je ne bois jamais seule."
        elio "Tu pouvais appeler Zara."
        ines "Zara boit du rosé sucré. Ça m'énerve."
        n "On boit. Elle me parle de son divorce — brièvement, sans amertume."
        ines "C'était mieux pour nous deux. On le savait depuis longtemps."
        ines "Ce resort est ma vie. Il n'y avait plus de place pour quelqu'un qui ne l'aimait pas."
        elio "Et quelqu'un qui l'aimerait ?"
        ines "..."
        ines "Ce serait différent."
        n "Elle me regarde — vraiment — et sourit légèrement."
    else:
        n "Je croise Ines qui vérifie les volets de la terrasse."
        ines "Bonne nuit."

    hide ines smirk
    $ current_day += 1
    jump day_router

label ev_ines_d4:
    scene bg terrace
    with dissolve
    show ines soft at right

    if affinity_ines >= 50:
        ines "Elio. Soirée vin ?"
        elio "C'est devenu un rituel."
        ines "Les bons trucs deviennent des rituels."
        n "Ce soir, elle est plus détendue. Le port altier s'est assoupli."
        n "Elle enlève ses chaussures et pose les pieds sur la rambarde."
        ines "C'est ma vraie façon d'être, là."
        elio "Je préfère ça."
        ines "Je sais. Et c'est pour ça que je me permets."
        n "Un moment s'écoule. Le vin est bon."
        ines "Elio."
        elio "Hm."
        ines "T'es jeune."
        elio "19 ans."
        ines "J'en ai 29."
        elio "Je sais compter."
        ines "Et ça te dérange pas ?"
        elio "Pas une seconde."
        n "Elle rit — un vrai rire, rare — et renverse presque son verre."
    elif affinity_ines >= 30:
        n "Soirée vins. On parle peu, mais bien."
    else:
        n "Je croise Ines dans le couloir."
        ines "Bonne nuit."

    hide ines soft
    $ current_day += 1
    jump day_router

label ev_ines_d5:
    scene bg terrace
    with dissolve
    show ines swimsuit at right

    if affinity_ines >= 60:
        n "Ines m'attend sur la terrasse après le dîner. Elle a changé de tenue."
        n "Robe légère. Plus détendue que je ne l'ai jamais vue."
        ines "Je voulais parler. Vraiment parler."
        elio "Je t'écoute."
        ines "Cette semaine... j'ai arrêté de compter les choses qui me manquaient."
        ines "Depuis mon divorce, je gère. Je gère bien. Mais je gère seule."
        ines "Et là, t'es arrivé, et j'ai arrêté de compter."
        n "Je ne dis rien. Certains mots n'ont pas besoin de réponse."
        ines "Elio. Je sais que tu pars dans deux jours."
        elio "Je sais."
        ines "Et je sais que t'as dix ans de moins que moi."
        elio "Je sais ça aussi."
        ines "Alors pourquoi j'ai envie que tu restes ?"
        elio "Parce que c'est réciproque."

        if affinity_ines >= 80:
            n "Elle se lève, pose sa main sur ma joue."
            ines "Elio. Reste, ce soir."
            elio "Si tu veux de moi."
            ines "Je te pose la question, donc oui."
            scene bg room
            with dissolve
            n "Ines est précise dans tout ce qu'elle fait. Dans son travail, ses mots, et cette nuit."
            n "Elle sait ce qu'elle veut et me guide avec une assurance douce."
            n "C'est différent de ce que j'imaginais. Plus profond."
            $ seen_ines_h1 = True
            $ affinity_ines += 15
            show ines soft at right
            n "Le matin, je me réveille et elle est là, dos tourné, regardant la mer par la fenêtre."
            ines "Café ?"
            elio "Toujours."
            hide ines soft
        else:
            n "On reste sur la terrasse jusqu'à minuit. Sa main dans la mienne."
            n "Pas plus. Pas besoin."
    elif affinity_ines >= 35:
        n "Soirée tranquille sur la terrasse. Elle sourit plus que d'habitude."
    else:
        ines "Bonne nuit, Elio."

    hide ines swimsuit
    $ current_day += 1
    jump day_router

label ev_ines_d6:
    scene bg terrace
    with dissolve
    show ines soft at right

    if affinity_ines >= 60:
        ines "Avant-dernière soirée."
        elio "Je sais pas si je suis prêt pour demain."
        ines "Moi non plus."
        n "On reste longtemps sans parler. Le vent chaud porte le son des vagues."
        ines "Elio. Ce resort t'attendra si tu reviens."
        ines "Et moi aussi."
        if seen_ines_h1:
            n "Elle prend ma main et m'emmène à l'intérieur."
            scene bg room
            with dissolve
            n "La dernière nuit est lente et mélancolique et parfaite."
            n "On sait tous les deux que c'est la fin de quelque chose et le début d'autre chose."
            $ affinity_ines += 10
    else:
        n "Ines range la terrasse. On dit bonne nuit poliment."

    hide ines soft
    $ current_day += 1
    jump day_router

# ════════════════════════════════════════════════════════
# CLARA – Soirées (jours 4 et 5 uniquement)
# ════════════════════════════════════════════════════════

label ev_lou_d4:
    scene bg terrace
    with dissolve
    show lou tsundere at right

    if affinity_lou >= 30:
        n "Lou est sur la terrasse avec son téléphone. Quand elle me voit, elle range très vite quelque chose."
        elio "Tu regardais quoi ?"
        lou "La météo."
        elio "Il fait beau."
        lou "Justement, ça m'étonnait."
        n "Silence."
        elio "Lou."
        lou "Quoi."
        elio "T'es sympa quand tu fais pas semblant d'être agaçante."
        lou "..."
        lou "...T'es pas mal non plus quand t'es pas trop d'accord avec toi-même."
        n "C'est probablement un compliment. Je le prends comme tel."
    else:
        n "Lou passe en me jetant un regard bref."
        lou "Bonne nuit."

    hide lou tsundere
    $ current_day += 1
    jump day_router

label ev_lou_d5:
    scene bg room
    with dissolve
    show lou blush at right

    if affinity_lou >= 50:
        n "Lou frappe à ma porte à 21h."
        n "Elle est en pyjama — ours imprimés — et a l'air de vivre la chose la plus difficile de sa vie."
        lou "J'ai... j'avais besoin d'un truc dans le couloir et t'étais là et..."
        elio "Lou. Tu peux juste dire que tu voulais passer."
        lou "Je voulais pas passer."
        elio "D'accord."
        lou "Je voulais juste... te voir. Un peu."
        n "Long silence."
        elio "Alors entre."
        n "On s'assoit sur le lit à regarder une série nulle sur mon ordinateur."
        n "Elle s'endort contre mon épaule à 22h30."
        n "Je ne bouge pas."

        if affinity_lou >= 65:
            n "Vers minuit, elle se réveille."
            n "Elle est à deux centimètres de mon visage et n'a pas l'air de s'en rendre compte immédiatement."
            n "Puis elle s'en rend compte."
            lou "...Je dormais ?"
            elio "Un peu."
            lou "..."
            lou "T'aurais pu me réveiller."
            elio "J'avais pas envie."
            n "Elle reste là. Ne s'éloigne pas."
            lou "Elio. Je vais partir demain matin."
            elio "Je sais."
            lou "Alors... je veux pas partir sans avoir..."
            n "Elle ne finit pas la phrase."
            n "Elle n'en a pas besoin."
            scene bg room
            with dissolve
            n "La nuit est courte et douce."
            n "Lou est déterminée dans tout ce qu'elle fait, y compris dans ce qu'elle ressent pour quelqu'un."
            n "Elle murmure {i}«c'était bien»{/i} juste avant de s'endormir."
            n "Je souris dans le noir."
            $ seen_lou_h1 = True
            $ affinity_lou += 15
    elif affinity_lou >= 30:
        n "Lou passe dire bonne nuit. Maladroitement mais sincèrement."
        lou "Bonne nuit, Elio."
        elio "Bonne nuit, Lou."
    else:
        n "Je n'ai pas revu Lou ce soir."

    hide lou blush
    $ current_day += 1
    jump day_router

label ev_lou_d6:
    scene bg resort
    with dissolve
    show lou shy at right

    n "Lou est partie ce matin."
    n "Elle m'a laissé un Post-it sur la porte : {i}«Rentre bien. — C»{/i}"
    n "Rien d'autre. Mais 'Rentre bien' de Lou, ça vaut beaucoup."
    n "Je le glisse dans ma poche."

    hide lou shy
    $ current_day += 1
    jump day_router
