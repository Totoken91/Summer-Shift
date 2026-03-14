# ════════════════════════════════════════════════════════
# SUMMER SHIFT – pointclick.rpy
# Écrans point & click (après-midis) + événements associés
# ════════════════════════════════════════════════════════
#
# Architecture :
#   label afternoon_X(day)  → boucle principale + appel screen
#   screen X_pc(day, visited) → hotspots cliquables
#   label pc_X_HOTSPOT_dY  → événement déclenché au clic
#
# Lieux : beach, pool, kitchen, terrace
# ════════════════════════════════════════════════════════

# ────────────────────────────────────────────────────────
# Style commun pour les hotspots
# ────────────────────────────────────────────────────────
style hotspot_button:
    background "#00000055"
    hover_background "#ffffff33"
    padding (10, 8, 10, 8)
    xminimum 140

style hotspot_button_text:
    color "#ffffff"
    hover_color "#ffe0b2"
    size 26
    xalign 0.5

# ════════════════════════════════════════════════════════
# PLAGE (Beach)
# ════════════════════════════════════════════════════════
screen beach_pc(day, visited):
    tag menu
    modal True

    add "bg beach"

    # HUD affinités
    frame:
        xpos 20 ypos 20
        background "#00000088"
        padding (12, 10)
        vbox:
            spacing 4
            text "❤ Lina  [affinity_lina]"  color "#FF9966" size 22
            text "❤ Mina  [affinity_mina]"  color "#FF99CC" size 22
            text "❤ Sofia [affinity_sofia]" color "#CC99FF" size 22
            if clara_available:
                text "❤ Clara [affinity_clara]" color "#99CCFF" size 22

    # Titre lieu
    text "🏖 PLAGE" xalign 0.5 ypos 30 size 36 color "#fff" outlines [(2,"#0005",0,0)]

    # ── Hotspots ──
    vbox:
        xpos 80 ypos 200
        spacing 16

        if "lina" not in visited:
            textbutton "💃 Parler à Lina":
                style "hotspot_button"
                action Return("lina")
        if "ball" not in visited:
            textbutton "🏐 Ballon de volley":
                style "hotspot_button"
                action Return("ball")
        if "sunscreen" not in visited:
            textbutton "🧴 Crème solaire":
                style "hotspot_button"
                action Return("sunscreen")
        if "waves" not in visited:
            textbutton "🌊 Aller dans l'eau":
                style "hotspot_button"
                action Return("waves")
        if "seashell" not in visited and day >= 2:
            textbutton "🐚 Coquillage bizarre":
                style "hotspot_button"
                action Return("seashell")
        if "clara_spy" not in visited and clara_available and day == 4:
            textbutton "👀 Quelqu'un derrière le parasol ?":
                style "hotspot_button"
                action Return("clara_spy")

    # Bouton sortie
    textbutton "➜ Terminer l'après-midi":
        xalign 0.95 yalign 0.95
        background "#00000088"
        hover_background "#ff990055"
        padding (14, 10)
        action Return("done")

label afternoon_beach(day):
    $ afternoon_visited = set()
    label .loop:
        call screen beach_pc(day, afternoon_visited)
        $ _r = _return
        if _r == "done":
            n "Je décide de rentrer me rafraîchir."
            return
        $ afternoon_visited.add(_r)
        call expression "pc_beach_" + _r + "_d" + str(day)
        jump afternoon_beach.loop

# ── Événements plage ─────────────────────────────────────

label pc_beach_lina_d1:
    show lina happy at right
    lina "Alex ! T'as mis de la crème ?"
    alex "Euh, pas encore."
    lina "Mon Dieu. Attends."
    n "Elle attrape un tube de crème et commence à l'appliquer sur mes épaules avec beaucoup d'enthousiasme et peu de précision."
    n "Une bonne partie atterrit sur son débardeur."
    lina "Ha. Voilà."
    alex "Tu en as mis autant sur toi que sur moi."
    lina "C'est de la protection bi-directionnelle."
    $ affinity_lina += 8
    hide lina happy
    return

label pc_beach_lina_d4:
    show lina swimsuit at right
    lina "Rematch de volley ?"
    alex "Toujours."
    n "La partie est serrée. Lina plonge, ripe dans le sable, se relève en riant."
    n "Son débardeur est couvert de sable. Elle s'en fiche."
    lina "Ton service est meilleur qu'avant."
    alex "J'apprends vite."
    lina "Ou je t'inspire."
    $ affinity_lina += 10
    hide lina swimsuit
    return

label pc_beach_ball_d1:
    n "Un ballon traîne près de l'eau. Je le récupère et me mets à jongler un peu."
    n "Pas terrible."
    n "Mais personne regarde."
    $ inventory.add("ball")
    return

label pc_beach_ball_d4:
    show clara tsundere at left
    n "Je ramasse le ballon. Clara est dans le coin, bras croisés."
    alex "Tu joues ?"
    clara "Je joue pas au volley."
    alex "J'ai pas dit volley."
    clara "..."
    clara "...Tu as raison. T'as dit joues."
    n "Elle attrape le ballon que je lui lance et le retourne sèchement."
    n "Très sèchement. J'ai à peine le temps de le réceptionner."
    clara "T'es nul."
    alex "Mais je m'améliore."
    $ affinity_clara += 8
    hide clara tsundere
    return

label pc_beach_sunscreen_d1:
    n "Un tube de crème solaire facteur 50 abandonné sur une chaise longue."
    n "Je le prends et l'applique correctement cette fois."
    n "La vue sur la mer est splendide."
    $ inventory.add("sunscreen")
    return

label pc_beach_sunscreen_d4:
    show mina shy at right
    n "Mina est assise à l'ombre, livre à la main, visiblement peu habituée à être sur la plage."
    mina "Oh ! Alex. Tu... tu veux la chaise ?"
    alex "Non, je voulais juste te proposer de la crème. T'as l'air de l'avoir oubliée."
    mina "Je... merci. C'est gentil."
    n "Elle me tend son épaule avec une timidité absolue."
    n "Ma main tremble un peu aussi. Je ne vais pas mentir."
    $ affinity_mina += 8
    hide mina shy
    return

label pc_beach_waves_d1:
    n "Je rentre dans l'eau jusqu'aux genoux. La mer est à température parfaite."
    n "Il n'y a rien d'autre à faire que d'apprécier ça en silence."
    n "Moment d'une qualité rare."
    return

label pc_beach_waves_d4:
    show sofia swimsuit at right
    n "Sofia entre dans l'eau à côté de moi. Elle n'a pas mis son paréo."
    n "Maillot une pièce bordeaux. Elle est magnifique et elle le sait sûrement, mais se comporte comme si ça n'avait aucune importance."
    sofia "L'eau est bonne aujourd'hui."
    alex "Très."
    sofia "Tu nages ?"
    alex "Je peux essayer."
    sofia "Essaie pas. Nage."
    n "On nage jusqu'au petit ponton et on revient en silence."
    n "Un silence éloquent."
    $ affinity_sofia += 8
    hide sofia swimsuit
    return

label pc_beach_seashell_d2:
    n "Un coquillage étrange, en spirale violet-blanc."
    n "Je le ramasse. Il est lourd et parfaitement intact."
    n "Je ne sais pas encore à qui je vais l'offrir."
    $ inventory.add("seashell")
    return

label pc_beach_seashell_d4:
    n "Le même coquillage violet-blanc traîne encore là."
    n "Ou peut-être un autre. Difficile à dire."
    n "Je le ramasse et pense à qui le mérite."
    if "seashell" not in inventory:
        $ inventory.add("seashell")
    return

label pc_beach_clara_spy_d4:
    show clara blush at right
    n "Un bruit derrière le grand parasol rayé. Je m'approche discrètement."
    n "Clara est là, téléphone à la main — mais l'objectif était clairement vers moi il y a deux secondes."
    alex "...Tu prenais une photo ?"
    clara "NON."
    alex "De quoi ?"
    clara "DE RIEN. De la mer."
    alex "La mer est derrière moi ?"
    clara "..."
    clara "Il y avait un oiseau."
    alex "Bien sûr."
    n "Elle est cramoisie. Je ne dis plus rien."
    n "Mais je souris."
    $ affinity_clara += 12
    hide clara blush
    return

# ════════════════════════════════════════════════════════
# PISCINE (Pool)
# ════════════════════════════════════════════════════════
screen pool_pc(day, visited):
    tag menu
    modal True

    add "bg pool"

    frame:
        xpos 20 ypos 20
        background "#00000088"
        padding (12, 10)
        vbox:
            spacing 4
            text "❤ Lina  [affinity_lina]"  color "#FF9966" size 22
            text "❤ Mina  [affinity_mina]"  color "#FF99CC" size 22
            text "❤ Sofia [affinity_sofia]" color "#CC99FF" size 22

    text "🏊 PISCINE" xalign 0.5 ypos 30 size 36 color "#fff" outlines [(2,"#0005",0,0)]

    vbox:
        xpos 80 ypos 200
        spacing 16

        if "lina_pool" not in visited:
            textbutton "🧹 Aider Lina à nettoyer la piscine":
                style "hotspot_button"
                action Return("lina_pool")
        if "sofia_pool" not in visited:
            textbutton "🪷 Sofia qui lit en bord de piscine":
                style "hotspot_button"
                action Return("sofia_pool")
        if "mina_pool" not in visited:
            textbutton "🍹 Mina apporte des boissons":
                style "hotspot_button"
                action Return("mina_pool")
        if "towel" not in visited:
            textbutton "🏖 Serviette oubliée":
                style "hotspot_button"
                action Return("towel")
        if "dive" not in visited:
            textbutton "💦 Plonger dans le grand bain":
                style "hotspot_button"
                action Return("dive")

    textbutton "➜ Terminer l'après-midi":
        xalign 0.95 yalign 0.95
        background "#00000088"
        hover_background "#00bcd455"
        padding (14, 10)
        action Return("done")

label afternoon_pool(day):
    $ afternoon_visited = set()
    label .loop:
        call screen pool_pc(day, afternoon_visited)
        $ _r = _return
        if _r == "done":
            n "Je rentre me changer."
            return
        $ afternoon_visited.add(_r)
        call expression "pc_pool_" + _r + "_d" + str(day)
        jump afternoon_pool.loop

# ── Événements piscine ───────────────────────────────────

label pc_pool_lina_pool_d2:
    show lina laugh at right
    lina "Alex ! T'arrives juste à temps."
    alex "Pour quoi ?"
    lina "J'ai besoin que quelqu'un tienne ça pendant que je—"
    n "Elle me tend un filet à long manche et commence à s'avancer dangereusement vers le bord."
    n "Prévisiblement, elle glisse."
    n "Imprévisiblement, elle m'attrape au vol et on tombe tous les deux."
    lina "{i}[[sous l'eau]{/i} PARDON !"
    n "L'eau est froide. On ressort en toussant."
    lina "...Je crois que la piscine est propre maintenant. L'eau a bougé."
    $ affinity_lina += 10
    hide lina laugh
    return

label pc_pool_lina_pool_d6:
    show lina swimsuit at right
    lina "On refait le coup de tomber dans la piscine ?"
    alex "C'est une invitation ?"
    lina "C'est statistiquement probable."
    n "On nage une heure. Lina perd trois paris. Elle rit à chaque fois."
    $ affinity_lina += 8
    hide lina swimsuit
    return

label pc_pool_sofia_pool_d2:
    show sofia confident at right
    n "Sofia est allongée sur un transat, livre ouvert sur la poitrine, lunettes de soleil."
    n "Elle entend mes pas sur le carrelage."
    sofia "Tu nages ?"
    alex "Je pensais, oui."
    sofia "Alors nage. Arrête de te justifier."
    n "Je plonge. Quand je refais surface, elle a posé son livre et me regarde."
    sofia "Pas mal."
    $ affinity_sofia += 8
    hide sofia confident
    return

label pc_pool_sofia_pool_d6:
    show sofia swimsuit at right
    n "Sofia est au bord, les pieds dans l'eau."
    n "Je m'assis à côté d'elle."
    sofia "Il ne reste qu'un jour."
    alex "Je sais."
    sofia "Est-ce que tu... reviendras ?"
    alex "Si tu me le demandes."
    sofia "Je te le demande."
    $ affinity_sofia += 10
    hide sofia swimsuit
    return

label pc_pool_mina_pool_d2:
    show mina happy at right
    n "Mina arrive avec un plateau de limonades maison et des petits gâteaux."
    mina "Je... je pensais que vous auriez soif avec la chaleur..."
    alex "Tu penses à tout."
    mina "Ou à peu, selon comment on voit les choses."
    n "On s'assoit au bord de la piscine et on boit les limonades ensemble."
    n "C'est parfait. Absolument parfait."
    $ affinity_mina += 8
    hide mina happy
    return

label pc_pool_mina_pool_d6:
    show mina blush at right
    n "Mina dépose le plateau et reste."
    n "Je lui propose de s'asseoir."
    mina "Je suis pas très piscine, d'habitude..."
    alex "Tu veux essayer ?"
    mina "...Peut-être juste les pieds."
    n "On reste assis, pieds dans l'eau, à ne rien dire de particulier."
    n "C'est exactement ce qu'il fallait."
    $ affinity_mina += 10
    hide mina blush
    return

label pc_pool_towel_d2:
    n "Une serviette oubliée, encore humide, pleine de sable."
    n "Je la secoue et la pose sur un transat propre."
    n "Bonne action du jour."
    $ inventory.add("towel")
    return

label pc_pool_towel_d6:
    n "Ma serviette. Je la retrouve là où je l'avais laissée."
    n "Ce resort a quelque chose de réconfortant — les objets restent là où on les pose."
    return

label pc_pool_dive_d2:
    n "Je prends de l'élan et je plonge."
    n "Trois secondes de silence parfait sous l'eau."
    n "Je remonte. Le ciel est bleu."
    n "C'est suffisant."
    return

label pc_pool_dive_d6:
    n "Je plonge une dernière fois."
    n "Sous l'eau, je pense à tout ce qui s'est passé cette semaine."
    n "La chaleur, les rires, les repas, les silences."
    n "Je remonte lentement."
    return

# ════════════════════════════════════════════════════════
# CUISINE (Kitchen)
# ════════════════════════════════════════════════════════
screen kitchen_pc(day, visited):
    tag menu
    modal True

    add "bg kitchen"

    frame:
        xpos 20 ypos 20
        background "#00000088"
        padding (12, 10)
        vbox:
            spacing 4
            text "❤ Lina  [affinity_lina]"  color "#FF9966" size 22
            text "❤ Mina  [affinity_mina]"  color "#FF99CC" size 22
            text "❤ Sofia [affinity_sofia]" color "#CC99FF" size 22

    text "🍳 CUISINE" xalign 0.5 ypos 30 size 36 color "#fff" outlines [(2,"#0005",0,0)]

    vbox:
        xpos 80 ypos 200
        spacing 16

        if "mina_cook" not in visited:
            textbutton "🍫 Aider Mina avec sa recette":
                style "hotspot_button"
                action Return("mina_cook")
        if "lina_snack" not in visited:
            textbutton "🥐 Lina qui grignote en cachette":
                style "hotspot_button"
                action Return("lina_snack")
        if "sofia_taste" not in visited:
            textbutton "🍷 Sofia qui goûte les vins":
                style "hotspot_button"
                action Return("sofia_taste")
        if "herbs" not in visited:
            textbutton "🌿 Herbes aromatiques":
                style "hotspot_button"
                action Return("herbs")
        if "chocolate" not in visited:
            textbutton "🍫 Tablette de chocolat mystérieuse":
                style "hotspot_button"
                action Return("chocolate")

    textbutton "➜ Terminer l'après-midi":
        xalign 0.95 yalign 0.95
        background "#00000088"
        hover_background "#fff9c455"
        padding (14, 10)
        action Return("done")

label afternoon_kitchen(day):
    $ afternoon_visited = set()
    label .loop:
        call screen kitchen_pc(day, afternoon_visited)
        $ _r = _return
        if _r == "done":
            n "Je quitte la cuisine avec l'estomac heureux."
            return
        $ afternoon_visited.add(_r)
        call expression "pc_kitchen_" + _r + "_d" + str(day)
        jump afternoon_kitchen.loop

# ── Événements cuisine ───────────────────────────────────

label pc_kitchen_mina_cook_d3:
    show mina happy at right
    mina "Oh ! Tu tombes bien."
    mina "J'ai besoin d'un avis honnête sur ce glaçage au chocolat."
    n "Elle trempe une cuillère dans le bol et me la tend."
    n "Le glaçage est riche, légèrement amer, absolument parfait."
    alex "C'est incroyable. Vraiment."
    mina "C'est trop sucré ?"
    alex "C'est parfait. Exactement comme il faut."
    n "Elle rougit. Son bonheur est sincère et touchant."
    mina "Si tu... si tu veux, tu peux rester goûter le résultat final ce soir ?"
    alex "Avec plaisir."
    $ affinity_mina += 10
    hide mina happy
    return

label pc_kitchen_lina_snack_d3:
    show lina laugh at right
    n "Lina est planquée derrière le réfrigérateur ouvert, en train de grignoter un croissant."
    n "Elle sursaute en m'entendant."
    lina "Je... je vérifiais les stocks !"
    alex "En mangeant le stock ?"
    lina "C'est une méthode de vérification empirique."
    alex "Je comprends pas."
    lina "Parfait. Viens, j'en ai un autre."
    n "On mange des croissants debout devant le frigo. C'est la meilleure chose de la journée."
    $ affinity_lina += 6
    hide lina laugh
    return

label pc_kitchen_sofia_taste_d3:
    show sofia smirk at right
    n "Sofia est penchée sur un présentoir de vins, verre à la main."
    sofia "Tu t'y connais en vin ?"
    alex "Pas vraiment."
    sofia "Goûte."
    n "Elle me tend son verre. C'est un rouge légèrement boisé."
    alex "C'est bon."
    sofia "C'est tout ce que tu as ?"
    alex "C'est bon... et ça me rappelle quelque chose que je saurai pas nommer."
    sofia "..."
    sofia "C'est la meilleure réponse que j'aie entendue."
    $ affinity_sofia += 8
    hide sofia smirk
    return

label pc_kitchen_herbs_d3:
    n "Un pot de basilic frais sur le rebord de la fenêtre."
    n "Je le sens. C'est l'été résumé en une odeur."
    n "Je le replace délicatement."
    return

label pc_kitchen_chocolate_d3:
    show mina blush at right
    n "Une tablette de chocolat noir 70% avec une étiquette manuscrite : {i}« Recette spéciale – NE PAS TOUCHER »{/i}."
    n "Je m'apprête à reposer."
    mina "Tu peux la prendre. C'est pour toi."
    alex "Hein ?"
    mina "Je... j'en avais commandé exprès pour une recette que je voulais tester avec toi."
    mina "Ce soir, si tu veux."
    n "Le ton de sa voix a changé. Plus doux. Presque un murmure."
    $ affinity_mina += 10
    hide mina blush
    return

# ════════════════════════════════════════════════════════
# TERRASSE / SOURCE CHAUDE
# ════════════════════════════════════════════════════════
screen terrace_pc(day, visited):
    tag menu
    modal True

    add "bg terrace"

    frame:
        xpos 20 ypos 20
        background "#00000088"
        padding (12, 10)
        vbox:
            spacing 4
            text "❤ Lina  [affinity_lina]"  color "#FF9966" size 22
            text "❤ Mina  [affinity_mina]"  color "#FF99CC" size 22
            text "❤ Sofia [affinity_sofia]" color "#CC99FF" size 22
            if clara_available:
                text "❤ Clara [affinity_clara]" color "#99CCFF" size 22

    text "🌿 TERRASSE" xalign 0.5 ypos 30 size 36 color "#fff" outlines [(2,"#0005",0,0)]

    vbox:
        xpos 80 ypos 200
        spacing 16

        if "sofia_massage" not in visited:
            textbutton "💆 Sofia propose un massage 'pro'":
                style "hotspot_button"
                action Return("sofia_massage")
        if "lina_hammock" not in visited:
            textbutton "🌴 Lina dans le hamac":
                style "hotspot_button"
                action Return("lina_hammock")
        if "spring" not in visited:
            textbutton "♨ Source chaude au fond du jardin":
                style "hotspot_button"
                action Return("spring")
        if "clara_roof" not in visited and clara_available:
            textbutton "🔭 Quelqu'un sur le toit ?":
                style "hotspot_button"
                action Return("clara_roof")
        if "sunset" not in visited:
            textbutton "🌅 Observer le coucher de soleil":
                style "hotspot_button"
                action Return("sunset")

    textbutton "➜ Terminer l'après-midi":
        xalign 0.95 yalign 0.95
        background "#00000088"
        hover_background "#ffe0b255"
        padding (14, 10)
        action Return("done")

label afternoon_terrace(day):
    $ afternoon_visited = set()
    label .loop:
        call screen terrace_pc(day, afternoon_visited)
        $ _r = _return
        if _r == "done":
            n "Je rentre me préparer pour le soir."
            return
        $ afternoon_visited.add(_r)
        call expression "pc_terrace_" + _r + "_d" + str(day)
        jump afternoon_terrace.loop

# ── Événements terrasse ──────────────────────────────────

label pc_terrace_sofia_massage_d5:
    show sofia soft at right
    sofia "Alex. Tu as l'air tendu."
    alex "C'est l'avant-dernier jour. Je suis nostalgique."
    sofia "Assieds-toi."
    n "Elle me désigne une chaise longue. Je m'exécute sans trop savoir ce qui se passe."
    sofia "Je suis formée en massage sportif. C'est professionnel."
    sofia "Ne lis rien là-dedans."
    alex "Bien sûr."
    n "Ses mains sont fermes et précises. Absolument professionnelles."
    n "Jusqu'au moment où elles s'attardent un peu plus longtemps que nécessaire sur mes épaules."
    n "Aucun des deux n'en fait mention."
    sofia "Mieux ?"
    alex "Beaucoup."
    $ affinity_sofia += 12
    hide sofia soft
    return

label pc_terrace_lina_hammock_d5:
    show lina laugh at right
    n "Lina se balance dans le hamac, les bras derrière la tête."
    lina "Alex ! Viens, y'a de la place."
    alex "Le hamac va pas craquer ?"
    lina "J'en sais rien. On peut tester."
    n "On teste. Le hamac tient. Mais c'est serré."
    n "On reste là vingt minutes à fixer le ciel et ne rien dire."
    n "C'est une des meilleures activités de la semaine."
    lina "...T'as mis de la crème aujourd'hui ?"
    alex "Oui."
    lina "Bien."
    $ affinity_lina += 8
    hide lina laugh
    return

label pc_terrace_spring_d5:
    show mina shy at right
    n "La source chaude est cachée derrière les bougainvilliers, au fond du jardin."
    n "Je m'approche. Mina est là — les pieds dans l'eau, yeux fermés."
    n "Elle ouvre les yeux en entendant mes pas."
    mina "Oh ! Je pensais que personne connaissait cet endroit."
    alex "Je l'ai trouvé par hasard. Je peux rester ?"
    mina "...Oui."
    n "On reste là en silence, les pieds dans l'eau chaude, le ciel qui vire à l'orange."
    n "Mina a l'air plus détendue que je l'ai jamais vue."
    mina "C'est mon endroit préféré ici."
    alex "Je comprends pourquoi."
    $ affinity_mina += 12
    hide mina shy
    return

label pc_terrace_clara_roof_d5:
    show clara tsundere at right
    n "Je lève les yeux. Clara est sur le toit, appuyée contre la cheminée."
    alex "Encore sur le toit ?"
    clara "Le toit, c'est calme."
    alex "Tu veux de la compagnie ?"
    clara "Non."
    n "Un silence."
    clara "...Tu peux monter si tu veux. L'échelle est derrière la remise."
    n "Je monte. On reste assis sur les tuiles chaudes à regarder la mer."
    clara "C'est mon endroit secret."
    alex "Je dirai rien."
    clara "Je sais."
    $ affinity_clara += 10
    hide clara tsundere
    return

label pc_terrace_sunset_d5:
    n "Le soleil touche l'horizon. Des oranges, des roses, des violets."
    n "Je m'assis sur les marches de la terrasse et je regarde."
    n "Il y a des moments dans la vie où on sait qu'on est exactement où il faut être."
    n "C'en est un."
    return
