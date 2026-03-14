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

label ev_lina_d1:
    scene bg bar
    with dissolve
    show lina happy at right

    lina "Alex ! Tu m'aides à ranger le bar ?"
    alex "Bien sûr."
    n "On range en silence, avec ses blagues nulles en fond sonore."
    n "Je me rends compte que je suis souriant depuis une heure."
    lina "T'aimes les calembours ?"
    alex "Pas vraiment."
    lina "Alors j'en fais pas."
    alex "T'en fais quand même."
    lina "Ouais mais je les prévenais."

    hide lina happy
    $ current_day += 1
    jump day_router

label ev_lina_d2:
    scene bg terrace
    with dissolve
    show lina happy at right

    if affinity_lina >= 30:
        n "Lina est sur la terrasse avec deux limonades. Elle en tend une sans que je demande."
        lina "T'avais l'air d'en avoir besoin."
        alex "Tu lis dans les pensées ?"
        lina "Non, juste dans les mines défaites."
        n "On parle jusqu'au coucher du soleil. De tout et de rien. De ses projets, des miens."
        lina "Alex... tu penses qu'on se reverra après cette semaine ?"
        alex "Si ça dépend de moi, oui."
        lina "Ça me va."
        n "Elle sourit, les yeux sur la mer. Pas sur moi. Mais le sourire est pour moi."
    else:
        n "Lina passe en coup de vent, un plateau sous le bras."
        lina "Bonne nuit, Alex !"
        alex "Bonne nuit."

    hide lina happy
    $ current_day += 1
    jump day_router

label ev_lina_d3:
    scene bg beach_soir
    with dissolve
    show lina swimsuit at right

    if affinity_lina >= 40:
        n "Lina m'attend sur la plage au crépuscule. Elle dessine quelque chose dans le sable du bout du pied."
        lina "T'arrives ! Je pensais que t'avais oublié."
        alex "T'avais pas dit qu'on avait rendez-vous."
        lina "Je t'ai pas dit, mais t'es là quand même. Donc ça compte."
        n "On marche au bord de l'eau. Elle enlève ses tongs et les porte à la main."
        lina "Tu sais ce que j'aime dans mon travail ici ?"
        alex "Quoi ?"
        lina "Les soirées. Quand les touristes sont pas là et qu'on est juste... nous."
        lina "C'est rare que 'nous' soit bien."
        alex "Je comprends."
        n "Elle me prend le bras, spontanément, comme si c'était la chose la plus naturelle du monde."
        n "Je la laisse faire. C'est effectivement la chose la plus naturelle du monde."
    else:
        lina "Bonne nuit !"
        alex "Bonne nuit, Lina."

    hide lina swimsuit
    $ current_day += 1
    jump day_router

label ev_lina_d4:
    scene bg bar
    with dissolve
    show lina happy at right

    if affinity_lina >= 50:
        lina "Fermeture du bar. Tu restes ?"
        alex "Si tu veux de la compagnie."
        lina "Je pose la question, donc oui."
        n "Les lumières du bar sont basses. Lina prépare deux cocktails sans demander ce que je veux."
        lina "Goûte."
        n "C'est parfait. Doux, fruité, avec juste ce qu'il faut."
        alex "C'est excellent."
        lina "Je sais. Je suis bonne dans mon job."
        alex "T'es bonne dans plein de choses."
        n "Elle s'arrête. Me regarde."
        lina "...Vraiment ?"
        alex "Vraiment."
        n "Le bar est silencieux. La mer bruisse dehors. Le moment suspend."
        lina "Alex. Est-ce que je peux te faire un câlin ?"
        alex "Euh— oui, bien sûr."
        n "Elle passe les bras autour de mes épaules et reste là un long moment."
        n "C'est inattendu. C'est parfait."
    elif affinity_lina >= 30:
        lina "Cocktail de fin de journée ?"
        alex "Avec plaisir."
        n "On passe une heure agréable. Les mots se font rares, mais c'est bien."
    else:
        n "Le bar est fermé. Je passe devant, Lina éteint les lumières."
        lina "Bonne nuit !"

    hide lina happy
    $ current_day += 1
    jump day_router

label ev_lina_d5:
    scene bg beach_soir
    with dissolve
    show lina swimsuit at right

    if affinity_lina >= 60:
        n "La plage de nuit. Lina est là, les pieds dans l'eau, les étoiles au-dessus."
        n "Elle se retourne en m'entendant."
        lina "Je savais que tu viendrais."
        alex "C'est devenu un rituel."
        lina "Les bons trucs deviennent des rituels."
        n "On s'assoit côte à côte. Les vagues arrivent jusqu'à nos chevilles."
        lina "Alex..."
        alex "Hm ?"
        lina "Tu me plais. Je voulais juste le dire clairement. Sans blague nulle."
        alex "Tu me plais aussi, Lina. Beaucoup."
        n "Elle rit — ce rire franc que j'adore — et pose sa tête sur mon épaule."

        if affinity_lina >= 75:
            lina "On va pas rester là toute la nuit, quand même ?"
            alex "On peut faire autre chose ?"
            lina "On peut. Si tu veux."
            n "Elle me prend la main. On rentre vers le resort sous les étoiles."
            n "Sa porte. Ses yeux qui me regardent avec quelque chose d'évident."
            lina "T'as le droit de refuser."
            alex "Je veux pas refuser."
            lina "...Bien."
            scene bg room
            with dissolve
            n "La nuit passe doucement, entre rires étouffés et murmures."
            n "Lina est exactement comme je l'imaginais : entière, spontanée, et terriblement sincère."
            $ seen_lina_h1 = True
            $ affinity_lina += 15
            n "Le matin arrive trop vite."
            show lina blush at right
            lina "...T'as dormi ?"
            alex "Un peu."
            lina "Moi aussi. Un peu."
            n "Elle me sourit, les cheveux encore défaits. C'est la plus belle version d'elle."
            hide lina blush
        else:
            n "On reste sur la plage à regarder les étoiles jusqu'à minuit."
            n "Pas grand-chose ne se passe. Mais c'est exactement ce qu'il fallait."
    elif affinity_lina >= 35:
        lina "Soirée plage ?"
        n "On marche, on parle. Rien de plus. Pour l'instant."
    else:
        n "Je croise Lina dans le couloir."
        lina "Bonne nuit !"

    hide lina happy
    $ current_day += 1
    jump day_router

label ev_lina_d6:
    scene bg bar
    with dissolve
    show lina happy at right

    if affinity_lina >= 60:
        lina "Dernier soir. Tu veux qu'on marque le coup ?"
        alex "Comment ?"
        lina "J'ai accès au bar. Et à des recettes de cocktails que j'ai jamais essayées."
        alex "On risque quoi ?"
        lina "Un cocktail raté, ou quelque chose d'extraordinaire."
        n "On passe la soirée à tester des mélanges improbables."
        n "Certains sont immondes. D'autres sont géniaux."
        n "Vers minuit, Lina pose la tête sur le comptoir, mi-fatiguée, mi-heureuse."
        lina "Alex. Je suis contente que t'aies pris ce job."
        alex "Moi aussi."
        if seen_lina_h1:
            lina "...Tu viens ?"
            alex "Oui."
            scene bg room
            with dissolve
            n "La deuxième nuit ensemble est encore mieux que la première."
            n "On connaît les silences de l'autre. C'est plus facile."
            $ affinity_lina += 10
    else:
        n "Lina range le bar. On échange quelques mots."
        lina "Bonne nuit, Alex."

    hide lina happy
    $ current_day += 1
    jump day_router

# ════════════════════════════════════════════════════════
# MINA – Soirées
# ════════════════════════════════════════════════════════

label ev_mina_d1:
    scene bg kitchen
    with dissolve
    show mina shy at right

    mina "Je... j'ai fait un dessert en trop. Si tu veux goûter."
    n "C'est un moelleux au chocolat encore tiède."
    n "Je ne dis rien pendant dix secondes. Je savoure."
    alex "Mina. C'est incroyable."
    mina "C'est juste un moelleux."
    alex "Non. C'est une œuvre d'art."
    n "Elle rougit et regarde ses mains."

    hide mina shy
    $ current_day += 1
    jump day_router

label ev_mina_d2:
    scene bg kitchen
    with dissolve
    show mina happy at right

    if affinity_mina >= 30:
        mina "Tu veux qu'on prépare quelque chose ensemble ce soir ?"
        alex "Tu m'apprendras ?"
        mina "Je vais essayer."
        n "On cuisine un risotto. Elle guide mes mains sur la casserole."
        n "Sa voix est douce, proche."
        mina "Voilà. Comme ça. T'as le geste naturellement."
        n "Je doute que ce soit vrai, mais j'apprécie qu'elle le dise."
    else:
        mina "Bonne nuit, Alex !"

    hide mina happy
    $ current_day += 1
    jump day_router

label ev_mina_d3:
    scene bg kitchen
    with dissolve
    show mina blush at right

    if affinity_mina >= 40:
        n "La cuisine après le service. Mina prépare sa ganache au chocolat."
        n "Je reste à regarder, assis sur le plan de travail."
        mina "Tu vas me porter malheur."
        alex "Les spectateurs portent malheur ?"
        mina "Parfois."
        alex "Et si je participe ?"
        n "Elle me tend une spatule couverte de chocolat fondu."
        mina "Goûte. Et dis-moi si c'est trop fort."
        n "Je goûte."
        alex "C'est parfait."
        mina "T'es sûr ?"
        n "Pour toute réponse, je lui montre la spatule."
        n "Elle rit, cache son rire derrière sa main, puis se ravise et rit vraiment."
        n "C'est la première fois que je la vois rire comme ça."
    else:
        mina "Le dessert est prêt, si tu veux."
        alex "Merci, Mina."

    hide mina blush
    $ current_day += 1
    jump day_router

label ev_mina_d4:
    scene bg kitchen
    with dissolve
    show mina happy at right

    if affinity_mina >= 50:
        mina "Ce soir, je teste la ganache spéciale."
        alex "Avec moi ?"
        mina "Si tu veux. Tu es mon meilleur cobaye."
        n "Elle prépare un assortiment de chocolats avec une précision exquise."
        n "Pour chaque pièce, elle me demande mon avis. Je prends le rôle au sérieux."
        mina "Celui-là."
        alex "...Il est fondant en bouche avec un goût de sel en fin."
        mina "Exactement."
        n "On se regarde. Elle est proche. Plus proche qu'en cuisine d'habitude."
        mina "Alex..."
        alex "Oui ?"
        mina "Je... merci d'être là. Pour goûter. Pour tout."
        n "Je pose ma main sur la sienne. Elle ne la retire pas."
    elif affinity_mina >= 30:
        n "On goûte les chocolats ensemble. Simple, doux, agréable."
    else:
        n "Mina range sa cuisine. Je passe dire bonne nuit."

    hide mina happy
    $ current_day += 1
    jump day_router

label ev_mina_d5:
    scene bg spring
    with dissolve
    show mina shy at right

    if affinity_mina >= 60:
        n "La source chaude, la nuit. Mina m'avait invité d'un texte mystérieux : {i}« Source chaude, 22h ? »{/i}"
        n "L'eau est à température parfaite. Le jardin sent le jasmin."
        mina "T'as trouvé ?"
        alex "C'est toi qui m'as montré l'endroit."
        mina "Je sais. Je voulais juste vérifier."
        n "On entre dans l'eau à tour de rôle. La chaleur monte doucement."
        mina "Alex. Est-ce que tu... est-ce que t'as envie de rester, ce soir ?"
        n "Sa voix est à peine plus qu'un murmure."
        alex "Si tu me le demandes."
        mina "Je te le demande."

        if affinity_mina >= 75:
            scene bg room
            with dissolve
            n "La nuit passe entre le silence de la source chaude et la douceur de sa chambre."
            n "Mina est douce et sincère. Elle murmure des choses en cuisine et en dehors."
            n "C'est intime d'une façon que je n'attendais pas."
            $ seen_mina_h1 = True
            $ affinity_mina += 15
            show mina blush at right
            n "Le lendemain matin, elle pose une tasse de café sur ma table de chevet."
            n "Sans un mot. Juste un sourire."
            mina "Le café est chaud."
            alex "Comme toujours."
            mina "Oui."
            hide mina blush
        else:
            n "On reste dans la source chaude à parler longtemps. Rien de plus."
            n "Mais ses mains frôlent les miennes dans l'eau."
    elif affinity_mina >= 35:
        n "On prend le dessert ensemble sur la terrasse."
        mina "Merci pour cette semaine, Alex."
    else:
        mina "Bonne nuit !"

    hide mina shy
    $ current_day += 1
    jump day_router

label ev_mina_d6:
    scene bg kitchen
    with dissolve
    show mina happy at right

    if affinity_mina >= 60:
        mina "Dernier dîner. J'ai préparé quelque chose de spécial."
        alex "Pour qui ?"
        mina "Pour toi. Qui d'autre ?"
        n "Le repas est extraordinaire. Six plats, chacun meilleur que le précédent."
        n "On finit avec un fondant au chocolat à se damner."
        alex "Mina. Si tu ouvres un restaurant, je suis le premier client."
        mina "...T'es sérieux ?"
        alex "Je suis sérieux."
        n "Elle me regarde longtemps."
        mina "Alex. Je veux pas que tu partes."
        alex "Moi non plus."
        if seen_mina_h1:
            n "Elle prend ma main et me guide hors de la cuisine."
            scene bg room
            with dissolve
            n "La dernière nuit est parfaite."
            n "Le chocolat, la chaleur, et elle."
            $ affinity_mina += 10
    else:
        n "Mina prépare un dessert spécial. On le mange ensemble en silence."

    hide mina happy
    $ current_day += 1
    jump day_router

# ════════════════════════════════════════════════════════
# SOFIA – Soirées
# ════════════════════════════════════════════════════════

label ev_sofia_d1:
    scene bg terrace
    with dissolve
    show sofia confident at right

    sofia "Tu t'es bien installé ?"
    alex "Très bien, merci."
    sofia "Bien. Demain 8h, petit-déjeuner commun."
    n "Elle va partir. Puis s'arrête."
    sofia "Alex. Tu travailles bien. Je voulais le dire."
    n "Et elle repart. Ce compliment vaut de l'or."

    hide sofia confident
    $ current_day += 1
    jump day_router

label ev_sofia_d2:
    scene bg terrace
    with dissolve
    show sofia soft at right

    if affinity_sofia >= 30:
        n "Sofia sur la terrasse, un verre de blanc à la main."
        n "Elle lève les yeux quand j'arrive."
        sofia "Tu veux t'asseoir ?"
        alex "Si j'y suis invité."
        sofia "Tu l'es."
        n "On parle. D'abord du resort, puis d'autre chose."
        sofia "Tu étudies quoi ?"
        alex "Architecture. Première année."
        sofia "Architecture..."
        sofia "Ce resort a été construit par mon grand-père. Il était autodidacte."
        sofia "Il aurait aimé que quelqu'un de ton âge s'intéresse à ces murs."
        n "Je regarde la bâtisse sous un angle nouveau."
    else:
        sofia "Bonne nuit, Alex."

    hide sofia soft
    $ current_day += 1
    jump day_router

label ev_sofia_d3:
    scene bg terrace
    with dissolve
    show sofia smirk at right

    if affinity_sofia >= 40:
        n "Sofia est là avec une bouteille de rouge ouverte et deux verres."
        sofia "Je ne bois jamais seule."
        alex "Tu pouvais appeler Lina."
        sofia "Lina boit du rosé sucré. Ça m'énerve."
        n "On boit. Elle me parle de son divorce — brièvement, sans amertume."
        sofia "C'était mieux pour nous deux. On le savait depuis longtemps."
        sofia "Ce resort est ma vie. Il n'y avait plus de place pour quelqu'un qui ne l'aimait pas."
        alex "Et quelqu'un qui l'aimerait ?"
        sofia "..."
        sofia "Ce serait différent."
        n "Elle me regarde — vraiment — et sourit légèrement."
    else:
        n "Je croise Sofia qui vérifie les volets de la terrasse."
        sofia "Bonne nuit."

    hide sofia smirk
    $ current_day += 1
    jump day_router

label ev_sofia_d4:
    scene bg terrace
    with dissolve
    show sofia soft at right

    if affinity_sofia >= 50:
        sofia "Alex. Soirée vin ?"
        alex "C'est devenu un rituel."
        sofia "Les bons trucs deviennent des rituels."
        n "Ce soir, elle est plus détendue. Le port altier s'est assoupli."
        n "Elle enlève ses chaussures et pose les pieds sur la rambarde."
        sofia "C'est ma vraie façon d'être, là."
        alex "Je préfère ça."
        sofia "Je sais. Et c'est pour ça que je me permets."
        n "Un moment s'écoule. Le vin est bon."
        sofia "Alex."
        alex "Hm."
        sofia "T'es jeune."
        alex "19 ans."
        sofia "J'en ai 29."
        alex "Je sais compter."
        sofia "Et ça te dérange pas ?"
        alex "Pas une seconde."
        n "Elle rit — un vrai rire, rare — et renverse presque son verre."
    elif affinity_sofia >= 30:
        n "Soirée vins. On parle peu, mais bien."
    else:
        n "Je croise Sofia dans le couloir."
        sofia "Bonne nuit."

    hide sofia soft
    $ current_day += 1
    jump day_router

label ev_sofia_d5:
    scene bg terrace
    with dissolve
    show sofia swimsuit at right

    if affinity_sofia >= 60:
        n "Sofia m'attend sur la terrasse après le dîner. Elle a changé de tenue."
        n "Robe légère. Plus détendue que je ne l'ai jamais vue."
        sofia "Je voulais parler. Vraiment parler."
        alex "Je t'écoute."
        sofia "Cette semaine... j'ai arrêté de compter les choses qui me manquaient."
        sofia "Depuis mon divorce, je gère. Je gère bien. Mais je gère seule."
        sofia "Et là, t'es arrivé, et j'ai arrêté de compter."
        n "Je ne dis rien. Certains mots n'ont pas besoin de réponse."
        sofia "Alex. Je sais que tu pars dans deux jours."
        alex "Je sais."
        sofia "Et je sais que t'as dix ans de moins que moi."
        alex "Je sais ça aussi."
        sofia "Alors pourquoi j'ai envie que tu restes ?"
        alex "Parce que c'est réciproque."

        if affinity_sofia >= 80:
            n "Elle se lève, pose sa main sur ma joue."
            sofia "Alex. Reste, ce soir."
            alex "Si tu veux de moi."
            sofia "Je te pose la question, donc oui."
            scene bg room
            with dissolve
            n "Sofia est précise dans tout ce qu'elle fait. Dans son travail, ses mots, et cette nuit."
            n "Elle sait ce qu'elle veut et me guide avec une assurance douce."
            n "C'est différent de ce que j'imaginais. Plus profond."
            $ seen_sofia_h1 = True
            $ affinity_sofia += 15
            show sofia soft at right
            n "Le matin, je me réveille et elle est là, dos tourné, regardant la mer par la fenêtre."
            sofia "Café ?"
            alex "Toujours."
            hide sofia soft
        else:
            n "On reste sur la terrasse jusqu'à minuit. Sa main dans la mienne."
            n "Pas plus. Pas besoin."
    elif affinity_sofia >= 35:
        n "Soirée tranquille sur la terrasse. Elle sourit plus que d'habitude."
    else:
        sofia "Bonne nuit, Alex."

    hide sofia swimsuit
    $ current_day += 1
    jump day_router

label ev_sofia_d6:
    scene bg terrace
    with dissolve
    show sofia soft at right

    if affinity_sofia >= 60:
        sofia "Avant-dernière soirée."
        alex "Je sais pas si je suis prêt pour demain."
        sofia "Moi non plus."
        n "On reste longtemps sans parler. Le vent chaud porte le son des vagues."
        sofia "Alex. Ce resort t'attendra si tu reviens."
        sofia "Et moi aussi."
        if seen_sofia_h1:
            n "Elle prend ma main et m'emmène à l'intérieur."
            scene bg room
            with dissolve
            n "La dernière nuit est lente et mélancolique et parfaite."
            n "On sait tous les deux que c'est la fin de quelque chose et le début d'autre chose."
            $ affinity_sofia += 10
    else:
        n "Sofia range la terrasse. On dit bonne nuit poliment."

    hide sofia soft
    $ current_day += 1
    jump day_router

# ════════════════════════════════════════════════════════
# CLARA – Soirées (jours 4 et 5 uniquement)
# ════════════════════════════════════════════════════════

label ev_clara_d4:
    scene bg terrace
    with dissolve
    show clara tsundere at right

    if affinity_clara >= 30:
        n "Clara est sur la terrasse avec son téléphone. Quand elle me voit, elle range très vite quelque chose."
        alex "Tu regardais quoi ?"
        clara "La météo."
        alex "Il fait beau."
        clara "Justement, ça m'étonnait."
        n "Silence."
        alex "Clara."
        clara "Quoi."
        alex "T'es sympa quand tu fais pas semblant d'être agaçante."
        clara "..."
        clara "...T'es pas mal non plus quand t'es pas trop d'accord avec toi-même."
        n "C'est probablement un compliment. Je le prends comme tel."
    else:
        n "Clara passe en me jetant un regard bref."
        clara "Bonne nuit."

    hide clara tsundere
    $ current_day += 1
    jump day_router

label ev_clara_d5:
    scene bg room
    with dissolve
    show clara blush at right

    if affinity_clara >= 50:
        n "Clara frappe à ma porte à 21h."
        n "Elle est en pyjama — ours imprimés — et a l'air de vivre la chose la plus difficile de sa vie."
        clara "J'ai... j'avais besoin d'un truc dans le couloir et t'étais là et..."
        alex "Clara. Tu peux juste dire que tu voulais passer."
        clara "Je voulais pas passer."
        alex "D'accord."
        clara "Je voulais juste... te voir. Un peu."
        n "Long silence."
        alex "Alors entre."
        n "On s'assoit sur le lit à regarder une série nulle sur mon ordinateur."
        n "Elle s'endort contre mon épaule à 22h30."
        n "Je ne bouge pas."

        if affinity_clara >= 65:
            n "Vers minuit, elle se réveille."
            n "Elle est à deux centimètres de mon visage et n'a pas l'air de s'en rendre compte immédiatement."
            n "Puis elle s'en rend compte."
            clara "...Je dormais ?"
            alex "Un peu."
            clara "..."
            clara "T'aurais pu me réveiller."
            alex "J'avais pas envie."
            n "Elle reste là. Ne s'éloigne pas."
            clara "Alex. Je vais partir demain matin."
            alex "Je sais."
            clara "Alors... je veux pas partir sans avoir..."
            n "Elle ne finit pas la phrase."
            n "Elle n'en a pas besoin."
            scene bg room
            with dissolve
            n "La nuit est courte et douce."
            n "Clara est déterminée dans tout ce qu'elle fait, y compris dans ce qu'elle ressent pour quelqu'un."
            n "Elle murmure {i}«c'était bien»{/i} juste avant de s'endormir."
            n "Je souris dans le noir."
            $ seen_clara_h1 = True
            $ affinity_clara += 15
    elif affinity_clara >= 30:
        n "Clara passe dire bonne nuit. Maladroitement mais sincèrement."
        clara "Bonne nuit, Alex."
        alex "Bonne nuit, Clara."
    else:
        n "Je n'ai pas revu Clara ce soir."

    hide clara blush
    $ current_day += 1
    jump day_router

label ev_clara_d6:
    scene bg resort
    with dissolve
    show clara shy at right

    n "Clara est partie ce matin."
    n "Elle m'a laissé un Post-it sur la porte : {i}«Rentre bien. — C»{/i}"
    n "Rien d'autre. Mais 'Rentre bien' de Clara, ça vaut beaucoup."
    n "Je le glisse dans ma poche."

    hide clara shy
    $ current_day += 1
    jump day_router
