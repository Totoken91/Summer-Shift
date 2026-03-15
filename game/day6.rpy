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

    show ines confident at right

    ines "Bonne nouvelle : deux familles arrivent demain pour le week-end."
    ines "Le resort va enfin avoir des clients normaux."
    elio "Et nous, on va devoir travailler ?"
    ines "Comme des professionnels."
    ines "Mais aujourd'hui... aujourd'hui est encore tranquille."

    hide ines confident

    n "Une journée tranquille. La dernière vraiment libre."

    menu:
        "Proposer à Zara une session de volley revanche.":
            $ affinity_zara += 10
            jump day6_morning_zara
        "Apporter à Vesna du chocolat acheté au village (pour sa prochaine recette).":
            $ affinity_vesna += 10
            jump day6_morning_vesna
        "Aider Ines à préparer l'arrivée des clients de demain.":
            $ affinity_ines += 10
            jump day6_morning_ines

label day6_morning_zara:
    scene bg beach
    with dissolve
    show zara laugh at right

    n "Zara est déjà sur la plage, balle à la main, sourire malicieux."

    zara "Je savais que tu viendrais !"
    elio "J'ai une réputation à racheter."
    zara "Tu étais pas {i}si{/i} nul."
    elio "C'est gentil."
    zara "Mais quand même un peu."
    elio "Voilà."

    n "On joue deux heures. Je gagne un set. Elle en gagne trois."
    n "Elle danse une petite victoire ridicule, les bras en l'air, les pieds dans le sable."
    n "C'est la chose la plus adorable que j'ai vue de la semaine."

    zara "Tu pars après-demain ?"
    elio "Oui."
    zara "C'est con."
    elio "Je trouve aussi."
    zara "..."
    zara "Allez ! Dernier set !"

    hide zara laugh
    jump day6_afternoon_intro

label day6_morning_vesna:
    scene bg kitchen
    with dissolve
    show vesna blush at right

    n "Je reviens du village avec deux tablettes de chocolat noir et une de chocolat blanc."
    n "Vesna les regarde comme si je lui avais apporté un trésor."

    vesna "Oh ! C'est... c'était pas nécessaire."
    elio "Je sais. Mais tu avais mentionné vouloir tester une ganache et..."
    vesna "T'as retenu ça ?"
    elio "Je retiens tout ce qui concerne la nourriture. C'est une priorité."

    n "Elle rit, et pour une fois elle ne cache pas son sourire."

    vesna "Alors... si tu veux... je pourrais préparer quelque chose ce soir. Pour toi."
    vesna "Rien de compliqué. Juste... pour remercier."
    elio "J'accepte avec plaisir."

    n "Il y a une chaleur dans la cuisine qui n'est pas seulement due aux fourneaux."

    hide vesna blush
    jump day6_afternoon_intro

label day6_morning_ines:
    scene bg room
    with dissolve
    show ines soft at right

    n "On prépare les chambres ensemble. Ines est plus détendue que d'habitude."

    ines "Quand tu reviendras à la mer, tu penseras à cet endroit ?"
    elio "Probablement. Pourquoi ?"
    ines "Je me demandais juste si on laissait une impression durable ou si on était juste un été parmi d'autres."
    elio "Ines."
    ines "Hm."
    elio "Cet été ne ressemblera à aucun autre."
    ines "..."
    ines "Tu es trop jeune pour dire des choses pareilles avec autant d'assurance."
    elio "Et toi tu es trop élégante pour les balayer d'un revers de main."

    n "Elle me regarde — vraiment cette fois, pas pour jauger — et sourit doucement."

    ines "Va m'aider avec le lit de la chambre 7. Il coince."

    hide ines soft
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
    elif _girl == "zara":
        jump ev_zara_d6
    elif _girl == "vesna":
        jump ev_vesna_d6
    elif _girl == "ines":
        jump ev_ines_d6
    else:
        jump ev_lou_d6

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
        "Trouver Zara avant la cohue.":
            $ affinity_zara += 5
            jump day7_morning_zara
        "Aller voir Vesna en cuisine une dernière fois.":
            $ affinity_vesna += 5
            jump day7_morning_vesna
        "Frapper à la porte du bureau de Ines.":
            $ affinity_ines += 5
            jump day7_morning_ines

label day7_morning_zara:
    show zara happy at right
    zara "Hé. T'as pas l'air bien pour quelqu'un qui passe une bonne journée."
    elio "Je suis triste de partir."
    zara "Ha. Moi aussi je suis triste que tu partes."
    zara "C'est quand même la preuve que c'était bien."
    elio "Ouais."
    zara "...Elio ?"
    elio "Hm."
    zara "Si jamais tu repasses par là... tu viens me dire bonjour ?"
    elio "C'est une promesse."
    hide zara happy
    jump day7_afternoon

label day7_morning_vesna:
    show vesna shy at right
    vesna "Tu pars ce soir."
    elio "Oui."
    vesna "Je... j'ai préparé quelque chose pour le voyage."
    n "Elle me tend une boîte soigneusement emballée."
    vesna "Des sablés au citron. Pour la route."
    n "Je ne sais pas quoi dire. Alors je prends la boîte, et je la regarde dans les yeux."
    elio "Vesna. C'était une semaine extraordinaire."
    vesna "Pour moi aussi."
    hide vesna shy
    jump day7_afternoon

label day7_morning_ines:
    show ines soft at right
    ines "Elio. Entre."
    n "Son bureau est rangé. La fenêtre donne sur la mer."
    ines "Comment tu te sens ?"
    elio "Nostalgique. Et je suis même pas encore parti."
    ines "C'est bon signe. Ça veut dire que ça valait quelque chose."
    elio "Ines..."
    ines "Je sais."
    n "Elle se lève et me tend la main. Formelle, presque. Puis elle change d'avis et pose la main sur mon épaule."
    ines "Merci d'avoir été là, Elio. Vraiment."
    hide ines soft
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

    if _girl == "zara":
        jump day7_final_zara
    elif _girl == "vesna":
        jump day7_final_vesna
    elif _girl == "ines":
        jump day7_final_ines
    else:
        jump day7_final_lou

# ── Scènes finales Jour 7 ────────────────────────────────
label day7_final_zara:
    show zara swimsuit at right
    zara "Je savais que tu serais là."
    elio "Tu m'espionnais ?"
    zara "Je t'observais. C'est différent."
    elio "Dans quel sens ?"
    zara "Dans le sens où c'est mignon quand c'est moi qui le fais."
    n "On s'assoit dans le sable. La mer est calme."
    zara "Elio. Je veux pas que tu partes sans qu'on... enfin."
    elio "Sans qu'on quoi ?"
    zara "Sans qu'on soit honnêtes."
    zara "Cette semaine, c'était pas juste un job d'été. Pour moi."
    elio "Pour moi non plus."
    n "Elle se tourne vers moi. Ses yeux sont sérieux pour la première fois depuis une semaine."
    zara "Alors ?"
    jump ending_zara_check

label day7_final_vesna:
    show vesna happy at right
    n "Vesna apparaît sur la plage, les chaussures à la main."
    vesna "Je... je voulais te parler avant que tu partes."
    elio "Je t'écoute."
    vesna "Cette semaine... tu m'as fait me sentir moins seule. En cuisine, ici, partout."
    vesna "Et je sais que c'est bête de dire ça à quelqu'un qui part ce soir."
    elio "C'est pas bête du tout."
    vesna "Elio... est-ce que tu... tu reviendras ?"
    n "Je la regarde. Elle est sincère, vulnérable, magnifique dans la lumière du soir."
    jump ending_vesna_check

label day7_final_ines:
    show ines swimsuit at right
    n "Ines est déjà là, les pieds dans l'eau, le regard vers l'horizon."
    ines "J'avais besoin d'air."
    elio "Moi aussi."
    ines "Alors on est pareils."
    n "Un long silence. Le bon genre."
    ines "Je pensais qu'un été finirait comme ils finissent tous."
    ines "Juste... du travail, des gens qui passent, et puis c'est tout."
    elio "Et là ?"
    ines "Et là, j'ai envie que tu restes."
    ines "Ce qui est nouveau pour moi."
    jump ending_ines_check

label day7_final_lou:
    show lou shy at right
    n "Lou est là, appuyée contre un rocher, l'air de rien."
    lou "...T'as besoin de compagnie ou quoi ?"
    elio "Un peu, oui."
    lou "Bien. Parce que moi aussi. Mais c'est pas pareil."
    elio "C'est pas pareil comment ?"
    lou "C'est pas pareil parce que... moi je reste et toi tu pars."
    lou "Alors c'est pas du tout pareil."
    n "Elle croise les bras. Tsundere jusqu'au bout."
    n "Mais ses joues sont roses."
    jump ending_lou_check

# ── Vérification affinité → fin ──────────────────────────
label ending_zara_check:
    if affinity_zara >= 80:
        jump ending_zara_good
    elif affinity_zara >= 50:
        jump ending_zara_normal
    else:
        jump ending_zara_bad

label ending_vesna_check:
    if affinity_vesna >= 80:
        jump ending_vesna_good
    elif affinity_vesna >= 50:
        jump ending_vesna_normal
    else:
        jump ending_vesna_bad

label ending_ines_check:
    if affinity_ines >= 80:
        jump ending_ines_good
    elif affinity_ines >= 50:
        jump ending_ines_normal
    else:
        jump ending_ines_bad

label ending_lou_check:
    if affinity_lou >= 60:
        jump ending_lou_good
    elif affinity_lou >= 35:
        jump ending_lou_normal
    else:
        jump ending_lou_bad

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
