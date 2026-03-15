# ════════════════════════════════════════════════════════
# SUMMER SHIFT – day3.rpy  |  Jour 3
# ════════════════════════════════════════════════════════
#
# STRUCTURE D'UNE JOURNÉE :
#   dayX_morning          → intro + menu (qui accompagner ?)
#   dayX_morning_FILLE    → mini-scène avec la fille choisie
#   dayX_afternoon_intro  → transition + appel au mode Point & Click
#   dayX_evening          → routage vers la scène du soir selon affinité
#
# LES PLACEHOLDERS (écrans blancs) :
#   Chaque `call screen art_placeholder("...")` affiche un fond blanc
#   avec la description de l'illustration à faire.
#   Le string passé en paramètre utilise \n pour les sauts de ligne.
#   Voir placeholders.rpy pour la doc complète.
#
# AJOUTER DES DIALOGUES PENDANT UN PLACEHOLDER :
#   Les dialogues vont APRÈS le call screen, pas dedans.
#   L'ordre est : placeholder → (joueur clique) → sprite → dialogues.
#   Exemple :
#
#     call screen art_placeholder("Description de l'image")
#     # ↑ fond blanc s'affiche, joueur clique pour passer
#
#     show zara happy at right   # sprite normal par-dessus le BG
#     zara "Salut !"             # dialogue classique
#     hide zara happy
#
# REMPLACER UN PLACEHOLDER PAR LE VRAI ART :
#   Supprimer la ligne `call screen art_placeholder("...")`
#   et écrire à la place :
#
#     show cg_nom_du_cg with dissolve
#     pause
#     hide cg_nom_du_cg
#
# ════════════════════════════════════════════════════════

label day3_morning:
    scene bg kitchen
    with dissolve

    n "{size=+6}{b}☀ Jour 3 – Matin{/b}{/size}"
    n "Troisième matin. La chaleur est déjà là à 7h30, collante, presque vivante. La fenêtre ouverte laisse entrer le bruit des vagues et une odeur saline mêlée de café."
    n "Ines est attablée, carnet ouvert, stylo en main. Débardeur fin, short en jean coupé très haut, cheveux relevés en chignon lâche, mèches collées à la nuque."

    show ines confident at right
    ines "Aujourd'hui on passe la vitesse supérieure. Les premiers vrais clients arrivent peut-être demain."
    ines "Vesna inventaire + prep. Zara terrasse & extérieurs. Moi chambres + bookings."
    ines "Toi… tu choisis ton camp. Ou ton poison."

    elio "Je peux aussi rester ici et te regarder cocher des cases ? C’est hypnotique."

    ines "Tente. Mais je mords quand on me ralentit."

    hide ines confident

    menu:
        "Rejoindre Zara sur la terrasse.":
            $ affinity_zara += 12
            jump day3_morning_zara
        "Aider Vesna en cuisine / stock.":
            $ affinity_vesna += 12
            jump day3_morning_vesna
        "Suivre Ines dans les chambres.":
            $ affinity_ines += 12
            jump day3_morning_ines


label day3_morning_zara:
    scene bg terrace
    with dissolve

    # ── PLACEHOLDER – remplacer plus tard par le vrai CG ──────────────
    # Format : call screen art_placeholder("ligne1\n• bullet\n• bullet")
    # Le \n crée un saut de ligne dans la description affichée.
    # Quand le vrai art arrive, supprimer ces 2 lignes et écrire :
    #   show cg_zara_terrace_d3 with dissolve
    #   pause
    #   hide cg_zara_terrace_d3
    call screen art_placeholder("Zara à genoux sur la terrasse ensoleillée\n• À quatre pattes, frotte une table basse\n• Short jean ultra-court retroussé très haut\n• Débardeur ample qui glisse sur une épaule\n• Gouttes de sueur sur clavicule et cou\n• Bronzage parfait, cheveux un peu en bataille\n• Sourire espiègle en levant les yeux vers Elio\n• Lumière dorée du matin, palmiers en arrière-plan\n• Carrelage clair qui reflète le soleil")
    # ↑ Le joueur clique → l'écran blanc disparaît → le BG reprend

    # ── DIALOGUES après le placeholder ────────────────────────────────
    # show / n / zara / elio etc. fonctionnent normalement ici.
    # Pour ajouter un dialogue PENDANT l'image (quand le vrai CG sera là)
    # il suffira de mettre des `n "..."` entre le show cg_ et le hide cg_.
    show zara happy at right
    n "Zara est à quatre pattes sur le carrelage déjà brûlant, short retroussé très haut. Le débardeur glisse régulièrement sur une épaule."
    n "Elle se redresse en m’entendant, passe le revers de la main sur son front → trace de poussière."

    zara "Elio ! Timing parfait. Les palmiers en pot là-haut… faut dépoussiérer les feuilles. Moi je passe pas."

    elio "Perchoir humain de luxe, c’est ça ?"

    zara "Perchoir mignon, grand… et avec une vue imprenable sur l’horizon. Ou autre chose."

    n "Elle se mordille la lèvre, faussement innocente."

    zara "T’as déjà choisi avec qui regarder le coucher de soleil ce soir ? Parce que moi… j’ai ma petite idée."

    hide zara happy
    jump day3_afternoon_intro


label day3_morning_vesna:
    scene bg kitchen
    with dissolve

    call screen art_placeholder("Vesna concentrée sur l’inventaire en cuisine\n• Debout sur un petit tabouret, penchée vers une étagère\n• Carnet dans une main, crayon derrière l’oreille\n• Tablier un peu sali (farine, chocolat)\n• T-shirt trop grand, short cycliste noir, lunettes\n• Mèche de cheveux noirs qui tombe sur la joue\n• Léger blush quand elle voit Elio entrer\n• Lumière douce venant de la fenêtre\n• Bocaux, conserves et ingrédients en arrière-plan")

    show vesna happy at right
    n "Vesna est perchée sur un tabouret, vérifie des dates sur des boîtes. Tablier par-dessus un t-shirt trop grand."

    vesna "Oh— Elio ! Je… j’avais pas entendu. Tu veux aider ?"

    elio "Seulement si tu promets de ne pas rougir à chaque contact de main."

    vesna "Je rougis pas… enfin… pas tout le temps."

    n "Nos doigts se croisent sur le stylo. Personne ne retire sa main tout de suite."

    vesna "… tu restes jusqu’à la fin de la semaine, hein ?"

    elio "Au moins. Peut-être plus si on me donne de bonnes raisons."

    vesna "… c’est déjà une bonne raison que tu sois là, non ?"

    hide vesna happy
    jump day3_afternoon_intro


label day3_morning_ines:
    scene bg room
    with dissolve

    call screen art_placeholder("Ines et Elio en train de faire le lit\n• Ines tire sur le drap avec précision\n• Kimono léger entrouvert, bretelle fine visible\n• Drap blanc tendu entre les deux mains d’Elio et Ines\n• Regard intense qui se croise au-dessus du tissu\n• Épaule et courbe de la nuque mises en valeur\n• Chambre lumineuse, lit défait à moitié refait\n• Tension palpable, ambiance chaude et intime")

    show ines confident at right
    n "Chambre 3. Ines tire sur les draps avec une précision chirurgicale. Son kimono en soie légère s’entrouvre à chaque mouvement."

    ines "Attrape l’autre côté. On gagne du temps à deux."

    elio "On forme une équipe dangereusement efficace."

    ines "Danger est un bien grand mot… mais je ne vais pas te contredire."

    n "On tend le drap. Nos regards se croisent au-dessus du tissu blanc. Elle ne détourne pas les yeux."

    ines "Ce soir, après le service… je serai sur la terrasse avec un verre. Si tu veux me rejoindre. Sans obligation."

    elio "Et si j’ai envie d’obligation ?"

    ines "Alors tu devras être très convaincant."

    hide ines confident
    jump day3_afternoon_intro


label day3_afternoon_intro:
    scene bg kitchen
    with dissolve

    n "{size=+6}{b}🍳 Jour 3 – Après-midi{/b}{/size}"
    n "La chaleur est devenue suffocante. Toutes les fenêtres ouvertes ne suffisent plus. L’odeur du chocolat fondu, du basilic écrasé et de la transpiration se mélange dans un cocktail étrange et entêtant."

    # (placeholder groupe optionnel plus tard si tu veux)
    # n """ [FULL ART GROUPE EN COURS] ... """

    call afternoon_kitchen(3)
    jump day3_evening


label day3_evening:
    scene bg terrace
    with dissolve

    $ _girl, _score = top_girl()

    if _score < 20:
        call screen art_placeholder("Coucher de soleil solo sur la terrasse\n• Elio seul avec un verre de rosé\n• Ciel orange et rose, mer en arrière-plan\n• Ambiance mélancolique mais paisible\n• Lumière chaude du crépuscule")

        n "{size=+6}{b}🌅 Jour 3 – Soir{/b}{/size}"
        n "Le soleil se couche dans des teintes orange et rose. Je reste seul sur la terrasse avec mon verre de rosé. C’était une belle journée quand même."
        $ current_day += 1
        jump day_router

    else:
        call screen art_placeholder("Coucher de soleil romantique sur la terrasse – [_girl]\n• La fille ayant le plus d’affinité est présente\n• Ambiance intime, lumière dorée/orange du crépuscule\n• Verres de vin, mer en fond, regards complices\n• Pose et tenue adaptées au personnage")

        n "{size=+6}{b}🌅 Jour 3 – Soir{/b}{/size}"

        if _girl == "zara":
            jump ev_zara_d3
        elif _girl == "vesna":
            jump ev_vesna_d3
        else:
            jump ev_ines_d3