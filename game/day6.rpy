# ════════════════════════════════════════════════════════
# SUMMER SHIFT – day6.rpy
# Jours 6 et 7 (dernier jour → fin)
# ════════════════════════════════════════════════════════

# ════════════════════════════════════════════════════════
# JOUR 6
# ════════════════════════════════════════════════════════
label day6_morning:
    scene bg resort
    with dissolve

    n "{size=+6}{b}☀ Jour 6 – Matin{/b}{/size}"
    n "Avant-veille du départ. Je me réveille avec une drôle de sensation dans la poitrine."
    n "Le resort s'est transformé, quelque part. Ou peut-être que c'est moi."

    show sofia confident at right

    sofia "Bonne nouvelle : deux familles arrivent demain pour le week-end."
    sofia "Le resort va enfin avoir des clients normaux."
    alex "Et nous, on va devoir travailler ?"
    sofia "Comme des professionnels."
    sofia "Mais aujourd'hui... aujourd'hui est encore tranquille."

    hide sofia confident

    n "Une journée tranquille. La dernière vraiment libre."

    menu:
        "Proposer à Lina une session de volley revanche.":
            $ affinity_lina += 10
            jump day6_morning_lina
        "Apporter à Mina du chocolat acheté au village (pour sa prochaine recette).":
            $ affinity_mina += 10
            jump day6_morning_mina
        "Aider Sofia à préparer l'arrivée des clients de demain.":
            $ affinity_sofia += 10
            jump day6_morning_sofia

label day6_morning_lina:
    scene bg beach
    with dissolve
    show lina laugh at right

    n "Lina est déjà sur la plage, balle à la main, sourire malicieux."

    lina "Je savais que tu viendrais !"
    alex "J'ai une réputation à racheter."
    lina "Tu étais pas {i}si{/i} nul."
    alex "C'est gentil."
    lina "Mais quand même un peu."
    alex "Voilà."

    n "On joue deux heures. Je gagne un set. Elle en gagne trois."
    n "Elle danse une petite victoire ridicule, les bras en l'air, les pieds dans le sable."
    n "C'est la chose la plus adorable que j'ai vue de la semaine."

    lina "Tu pars après-demain ?"
    alex "Oui."
    lina "C'est con."
    alex "Je trouve aussi."
    lina "..."
    lina "Allez ! Dernier set !"

    hide lina laugh
    jump day6_afternoon_intro

label day6_morning_mina:
    scene bg kitchen
    with dissolve
    show mina blush at right

    n "Je reviens du village avec deux tablettes de chocolat noir et une de chocolat blanc."
    n "Mina les regarde comme si je lui avais apporté un trésor."

    mina "Oh ! C'est... c'était pas nécessaire."
    alex "Je sais. Mais tu avais mentionné vouloir tester une ganache et..."
    mina "T'as retenu ça ?"
    alex "Je retiens tout ce qui concerne la nourriture. C'est une priorité."

    n "Elle rit, et pour une fois elle ne cache pas son sourire."

    mina "Alors... si tu veux... je pourrais préparer quelque chose ce soir. Pour toi."
    mina "Rien de compliqué. Juste... pour remercier."
    alex "J'accepte avec plaisir."

    n "Il y a une chaleur dans la cuisine qui n'est pas seulement due aux fourneaux."

    hide mina blush
    jump day6_afternoon_intro

label day6_morning_sofia:
    scene bg room
    with dissolve
    show sofia soft at right

    n "On prépare les chambres ensemble. Sofia est plus détendue que d'habitude."

    sofia "Quand tu reviendras à la mer, tu penseras à cet endroit ?"
    alex "Probablement. Pourquoi ?"
    sofia "Je me demandais juste si on laissait une impression durable ou si on était juste un été parmi d'autres."
    alex "Sofia."
    sofia "Hm."
    alex "Cet été ne ressemblera à aucun autre."
    sofia "..."
    sofia "Tu es trop jeune pour dire des choses pareilles avec autant d'assurance."
    alex "Et toi tu es trop élégante pour les balayer d'un revers de main."

    n "Elle me regarde — vraiment cette fois, pas pour jauger — et sourit doucement."

    sofia "Va m'aider avec le lit de la chambre 7. Il coince."

    hide sofia soft
    jump day6_afternoon_intro

# ── Après-midi Jour 6 – Piscine (dernier P&C) ───────────
label day6_afternoon_intro:
    scene bg pool
    with dissolve

    n "{size=+6}{b}🏊 Jour 6 – Après-midi{/b}{/size}"
    n "Dernière vraie après-midi libre. Piscine, soleil, et la douce mélancolie des fins d'été."

    call afternoon_pool(6)

    jump day6_evening

# ── Soir Jour 6 ──────────────────────────────────────────
label day6_evening:
    scene bg terrace
    with dissolve

    n "{size=+6}{b}🌅 Jour 6 – Soir{/b}{/size}"
    n "Le soleil se couche sur l'avant-dernière soirée."

    $ _girl, _score = top_girl()

    if _score < 40:
        n "Je passe la soirée seul sur la terrasse."
        n "Je me rends compte que j'aurais pu être plus courageux cette semaine."
        $ current_day += 1
        jump day_router
    elif _girl == "lina":
        jump ev_lina_d6
    elif _girl == "mina":
        jump ev_mina_d6
    elif _girl == "sofia":
        jump ev_sofia_d6
    else:
        jump ev_clara_d6

# ════════════════════════════════════════════════════════
# JOUR 7 – DERNIER JOUR
# ════════════════════════════════════════════════════════
label day7_morning:
    scene bg resort
    with dissolve

    n "{size=+6}{b}☀ Jour 7 – Dernier matin{/b}{/size}"
    n "Je me réveille avec le sentiment bizarre d'un dernier jour."
    n "Mon train est à 18h. J'ai toute la matinée et l'après-midi."

    n "Le resort accueille ses premiers vrais clients de la semaine."
    n "Tout le monde est en mouvement. Sourires professionnels. Efficacité."
    n "Et moi, quelque part entre tout ça, j'ai besoin de dire au revoir à quelqu'un."

    menu:
        "Trouver Lina avant la cohue.":
            $ affinity_lina += 5
            jump day7_morning_lina
        "Aller voir Mina en cuisine une dernière fois.":
            $ affinity_mina += 5
            jump day7_morning_mina
        "Frapper à la porte du bureau de Sofia.":
            $ affinity_sofia += 5
            jump day7_morning_sofia

label day7_morning_lina:
    show lina happy at right
    lina "Hé. T'as pas l'air bien pour quelqu'un qui passe une bonne journée."
    alex "Je suis triste de partir."
    lina "Ha. Moi aussi je suis triste que tu partes."
    lina "C'est quand même la preuve que c'était bien."
    alex "Ouais."
    lina "...Alex ?"
    alex "Hm."
    lina "Si jamais tu repasses par là... tu viens me dire bonjour ?"
    alex "C'est une promesse."
    hide lina happy
    jump day7_afternoon

label day7_morning_mina:
    show mina shy at right
    mina "Tu pars ce soir."
    alex "Oui."
    mina "Je... j'ai préparé quelque chose pour le voyage."
    n "Elle me tend une boîte soigneusement emballée."
    mina "Des sablés au citron. Pour la route."
    n "Je ne sais pas quoi dire. Alors je prends la boîte, et je la regarde dans les yeux."
    alex "Mina. C'était une semaine extraordinaire."
    mina "Pour moi aussi."
    hide mina shy
    jump day7_afternoon

label day7_morning_sofia:
    show sofia soft at right
    sofia "Alex. Entre."
    n "Son bureau est rangé. La fenêtre donne sur la mer."
    sofia "Comment tu te sens ?"
    alex "Nostalgique. Et je suis même pas encore parti."
    sofia "C'est bon signe. Ça veut dire que ça valait quelque chose."
    alex "Sofia..."
    sofia "Je sais."
    n "Elle se lève et me tend la main. Formelle, presque. Puis elle change d'avis et pose la main sur mon épaule."
    sofia "Merci d'avoir été là, Alex. Vraiment."
    hide sofia soft
    jump day7_afternoon

# ── Après-midi Jour 7 – Moment décisif ──────────────────
label day7_afternoon:
    scene bg beach
    with dissolve

    n "{size=+6}{b}🌊 Jour 7 – Après-midi{/b}{/size}"
    n "Les dernières heures. Je marche sur la plage, valise pas encore bouclée."
    n "Et là, la personne qui compte le plus ce moment vient me rejoindre."

    $ _girl, _score = top_girl()

    if _score < 30:
        jump ending_router   # Pas assez d'affinité → fin sans route

    if _girl == "lina":
        jump day7_final_lina
    elif _girl == "mina":
        jump day7_final_mina
    elif _girl == "sofia":
        jump day7_final_sofia
    else:
        jump day7_final_clara

# ── Scènes finales Jour 7 ────────────────────────────────
label day7_final_lina:
    show lina swimsuit at right
    lina "Je savais que tu serais là."
    alex "Tu m'espionnais ?"
    lina "Je t'observais. C'est différent."
    alex "Dans quel sens ?"
    lina "Dans le sens où c'est mignon quand c'est moi qui le fais."
    n "On s'assoit dans le sable. La mer est calme."
    lina "Alex. Je veux pas que tu partes sans qu'on... enfin."
    alex "Sans qu'on quoi ?"
    lina "Sans qu'on soit honnêtes."
    lina "Cette semaine, c'était pas juste un job d'été. Pour moi."
    alex "Pour moi non plus."
    n "Elle se tourne vers moi. Ses yeux sont sérieux pour la première fois depuis une semaine."
    lina "Alors ?"
    jump ending_lina_check

label day7_final_mina:
    show mina happy at right
    n "Mina apparaît sur la plage, les chaussures à la main."
    mina "Je... je voulais te parler avant que tu partes."
    alex "Je t'écoute."
    mina "Cette semaine... tu m'as fait me sentir moins seule. En cuisine, ici, partout."
    mina "Et je sais que c'est bête de dire ça à quelqu'un qui part ce soir."
    alex "C'est pas bête du tout."
    mina "Alex... est-ce que tu... tu reviendras ?"
    n "Je la regarde. Elle est sincère, vulnérable, magnifique dans la lumière du soir."
    jump ending_mina_check

label day7_final_sofia:
    show sofia swimsuit at right
    n "Sofia est déjà là, les pieds dans l'eau, le regard vers l'horizon."
    sofia "J'avais besoin d'air."
    alex "Moi aussi."
    sofia "Alors on est pareils."
    n "Un long silence. Le bon genre."
    sofia "Je pensais qu'un été finirait comme ils finissent tous."
    sofia "Juste... du travail, des gens qui passent, et puis c'est tout."
    alex "Et là ?"
    sofia "Et là, j'ai envie que tu restes."
    sofia "Ce qui est nouveau pour moi."
    jump ending_sofia_check

label day7_final_clara:
    show clara shy at right
    n "Clara est là, appuyée contre un rocher, l'air de rien."
    clara "...T'as besoin de compagnie ou quoi ?"
    alex "Un peu, oui."
    clara "Bien. Parce que moi aussi. Mais c'est pas pareil."
    alex "C'est pas pareil comment ?"
    clara "C'est pas pareil parce que... moi je reste et toi tu pars."
    clara "Alors c'est pas du tout pareil."
    n "Elle croise les bras. Tsundere jusqu'au bout."
    n "Mais ses joues sont roses."
    jump ending_clara_check

# ── Vérification affinité → fin ──────────────────────────
label ending_lina_check:
    if affinity_lina >= 80:
        jump ending_lina_good
    elif affinity_lina >= 50:
        jump ending_lina_normal
    else:
        jump ending_lina_bad

label ending_mina_check:
    if affinity_mina >= 80:
        jump ending_mina_good
    elif affinity_mina >= 50:
        jump ending_mina_normal
    else:
        jump ending_mina_bad

label ending_sofia_check:
    if affinity_sofia >= 80:
        jump ending_sofia_good
    elif affinity_sofia >= 50:
        jump ending_sofia_normal
    else:
        jump ending_sofia_bad

label ending_clara_check:
    if affinity_clara >= 60:
        jump ending_clara_good
    elif affinity_clara >= 35:
        jump ending_clara_normal
    else:
        jump ending_clara_bad

# ── Fin sans route principale ────────────────────────────
label ending_router:
    scene bg resort
    with fade
    n "Mon taxi arrive à 18h."
    n "Je charge ma valise. Je regarde le resort une dernière fois."
    n "Tout le monde m'a dit au revoir professionnellement, chaleureusement."
    n "Mais rien de plus."
    n "Je repense à la semaine. Aux choix que j'aurais pu faire différemment."
    n "L'été est fini."
    n "{b}FIN{/b}"
    return
