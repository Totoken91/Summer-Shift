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
            text "❤ Zara  [affinity_zara]"  color "#FF9966" size 22
            text "❤ Vesna  [affinity_vesna]"  color "#FF99CC" size 22
            text "❤ Ines [affinity_ines]" color "#CC99FF" size 22
            if lou_available:
                text "❤ Lou [affinity_lou]" color "#99CCFF" size 22

    # Titre lieu
    text "🏖 PLAGE" xalign 0.5 ypos 30 size 36 color "#fff" outlines [(2,"#0005",0,0)]

    # ── Hotspots ──
    vbox:
        xpos 80 ypos 200
        spacing 16

        if "zara" not in visited:
            textbutton "💃 Parler à Zara":
                style "hotspot_button"
                action Return("zara")
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
        if "lou_spy" not in visited and lou_available and day == 4:
            textbutton "👀 Quelqu'un derrière le parasol ?":
                style "hotspot_button"
                action Return("lou_spy")

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

label pc_beach_zara_d1:
    show zara happy at right
    zara "Elio ! T'as mis de la crème ?"
    elio "Euh, pas encore."
    zara "Mon Dieu. Attends."
    n "Elle attrape un tube de crème et commence à l'appliquer sur mes épaules avec beaucoup d'enthousiasme et peu de précision."
    n "Une bonne partie atterrit sur son débardeur."
    zara "Ha. Voilà."
    elio "Tu en as mis autant sur toi que sur moi."
    zara "C'est de la protection bi-directionnelle."
    $ affinity_zara += 8
    hide zara happy
    return

label pc_beach_zara_d4:
    show zara swimsuit at right
    zara "Rematch de volley ?"
    elio "Toujours."
    n "La partie est serrée. Zara plonge, ripe dans le sable, se relève en riant."
    n "Son débardeur est couvert de sable. Elle s'en fiche."
    zara "Ton service est meilleur qu'avant."
    elio "J'apprends vite."
    zara "Ou je t'inspire."
    $ affinity_zara += 10
    hide zara swimsuit
    return

label pc_beach_ball_d1:
    n "Un ballon traîne près de l'eau. Je le récupère et me mets à jongler un peu."
    n "Pas terrible."
    n "Mais personne regarde."
    $ inventory.add("ball")
    return

label pc_beach_ball_d4:
    show lou tsundere at left
    n "Je ramasse le ballon. Lou est dans le coin, bras croisés."
    elio "Tu joues ?"
    lou "Je joue pas au volley."
    elio "J'ai pas dit volley."
    lou "..."
    lou "...Tu as raison. T'as dit joues."
    n "Elle attrape le ballon que je lui lance et le retourne sèchement."
    n "Très sèchement. J'ai à peine le temps de le réceptionner."
    lou "T'es nul."
    elio "Mais je m'améliore."
    $ affinity_lou += 8
    hide lou tsundere
    return

label pc_beach_sunscreen_d1:
    n "Un tube de crème solaire facteur 50 abandonné sur une chaise longue."
    n "Je le prends et l'applique correctement cette fois."
    n "La vue sur la mer est splendide."
    $ inventory.add("sunscreen")
    return

label pc_beach_sunscreen_d4:
    show vesna shy at right
    n "Vesna est assise à l'ombre, livre à la main, visiblement peu habituée à être sur la plage."
    vesna "Oh ! Elio. Tu... tu veux la chaise ?"
    elio "Non, je voulais juste te proposer de la crème. T'as l'air de l'avoir oubliée."
    vesna "Je... merci. C'est gentil."
    n "Elle me tend son épaule avec une timidité absolue."
    n "Ma main tremble un peu aussi. Je ne vais pas mentir."
    $ affinity_vesna += 8
    hide vesna shy
    return

label pc_beach_waves_d1:
    n "Je rentre dans l'eau jusqu'aux genoux. La mer est à température parfaite."
    n "Il n'y a rien d'autre à faire que d'apprécier ça en silence."
    n "Moment d'une qualité rare."
    return

label pc_beach_waves_d4:
    show ines swimsuit at right
    n "Ines entre dans l'eau à côté de moi. Elle n'a pas mis son paréo."
    n "Maillot une pièce bordeaux. Elle est magnifique et elle le sait sûrement, mais se comporte comme si ça n'avait aucune importance."
    ines "L'eau est bonne aujourd'hui."
    elio "Très."
    ines "Tu nages ?"
    elio "Je peux essayer."
    ines "Essaie pas. Nage."
    n "On nage jusqu'au petit ponton et on revient en silence."
    n "Un silence éloquent."
    $ affinity_ines += 8
    hide ines swimsuit
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

label pc_beach_lou_spy_d4:
    show lou blush at right
    n "Un bruit derrière le grand parasol rayé. Je m'approche discrètement."
    n "Lou est là, téléphone à la main — mais l'objectif était clairement vers moi il y a deux secondes."
    elio "...Tu prenais une photo ?"
    lou "NON."
    elio "De quoi ?"
    lou "DE RIEN. De la mer."
    elio "La mer est derrière moi ?"
    lou "..."
    lou "Il y avait un oiseau."
    elio "Bien sûr."
    n "Elle est cramoisie. Je ne dis plus rien."
    n "Mais je souris."
    $ affinity_lou += 12
    hide lou blush
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
            text "❤ Zara  [affinity_zara]"  color "#FF9966" size 22
            text "❤ Vesna  [affinity_vesna]"  color "#FF99CC" size 22
            text "❤ Ines [affinity_ines]" color "#CC99FF" size 22

    text "🏊 PISCINE" xalign 0.5 ypos 30 size 36 color "#fff" outlines [(2,"#0005",0,0)]

    vbox:
        xpos 80 ypos 200
        spacing 16

        if "zara_pool" not in visited:
            textbutton "🧹 Aider Zara à nettoyer la piscine":
                style "hotspot_button"
                action Return("zara_pool")
        if "ines_pool" not in visited:
            textbutton "🪷 Ines qui lit en bord de piscine":
                style "hotspot_button"
                action Return("ines_pool")
        if "vesna_pool" not in visited:
            textbutton "🍹 Vesna apporte des boissons":
                style "hotspot_button"
                action Return("vesna_pool")
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

label pc_pool_zara_pool_d2:
    show zara laugh at right
    zara "Elio ! T'arrives juste à temps."
    elio "Pour quoi ?"
    zara "J'ai besoin que quelqu'un tienne ça pendant que je—"
    n "Elle me tend un filet à long manche et commence à s'avancer dangereusement vers le bord."
    n "Prévisiblement, elle glisse."
    n "Imprévisiblement, elle m'attrape au vol et on tombe tous les deux."
    zara "{i}[[sous l'eau]{/i} PARDON !"
    n "L'eau est froide. On ressort en toussant."
    zara "...Je crois que la piscine est propre maintenant. L'eau a bougé."
    $ affinity_zara += 10
    hide zara laugh
    return

label pc_pool_zara_pool_d6:
    show zara swimsuit at right
    zara "On refait le coup de tomber dans la piscine ?"
    elio "C'est une invitation ?"
    zara "C'est statistiquement probable."
    n "On nage une heure. Zara perd trois paris. Elle rit à chaque fois."
    $ affinity_zara += 8
    hide zara swimsuit
    return

label pc_pool_ines_pool_d2:
    show ines confident at right
    n "Ines est allongée sur un transat, livre ouvert sur la poitrine, lunettes de soleil."
    n "Elle entend mes pas sur le carrelage."
    ines "Tu nages ?"
    elio "Je pensais, oui."
    ines "Alors nage. Arrête de te justifier."
    n "Je plonge. Quand je refais surface, elle a posé son livre et me regarde."
    ines "Pas mal."
    $ affinity_ines += 8
    hide ines confident
    return

label pc_pool_ines_pool_d6:
    show ines swimsuit at right
    n "Ines est au bord, les pieds dans l'eau."
    n "Je m'assis à côté d'elle."
    ines "Il ne reste qu'un jour."
    elio "Je sais."
    ines "Est-ce que tu... reviendras ?"
    elio "Si tu me le demandes."
    ines "Je te le demande."
    $ affinity_ines += 10
    hide ines swimsuit
    return

label pc_pool_vesna_pool_d2:
    show vesna happy at right
    n "Vesna arrive avec un plateau de limonades maison et des petits gâteaux."
    vesna "Je... je pensais que vous auriez soif avec la chaleur..."
    elio "Tu penses à tout."
    vesna "Ou à peu, selon comment on voit les choses."
    n "On s'assoit au bord de la piscine et on boit les limonades ensemble."
    n "C'est parfait. Absolument parfait."
    $ affinity_vesna += 8
    hide vesna happy
    return

label pc_pool_vesna_pool_d6:
    show vesna blush at right
    n "Vesna dépose le plateau et reste."
    n "Je lui propose de s'asseoir."
    vesna "Je suis pas très piscine, d'habitude..."
    elio "Tu veux essayer ?"
    vesna "...Peut-être juste les pieds."
    n "On reste assis, pieds dans l'eau, à ne rien dire de particulier."
    n "C'est exactement ce qu'il fallait."
    $ affinity_vesna += 10
    hide vesna blush
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
            text "❤ Zara  [affinity_zara]"  color "#FF9966" size 22
            text "❤ Vesna  [affinity_vesna]"  color "#FF99CC" size 22
            text "❤ Ines [affinity_ines]" color "#CC99FF" size 22

    text "🍳 CUISINE" xalign 0.5 ypos 30 size 36 color "#fff" outlines [(2,"#0005",0,0)]

    vbox:
        xpos 80 ypos 200
        spacing 16

        if "vesna_cook" not in visited:
            textbutton "🍫 Aider Vesna avec sa recette":
                style "hotspot_button"
                action Return("vesna_cook")
        if "zara_snack" not in visited:
            textbutton "🥐 Zara qui grignote en cachette":
                style "hotspot_button"
                action Return("zara_snack")
        if "ines_taste" not in visited:
            textbutton "🍷 Ines qui goûte les vins":
                style "hotspot_button"
                action Return("ines_taste")
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

label pc_kitchen_vesna_cook_d3:
    show vesna happy at right
    vesna "Oh ! Tu tombes bien."
    vesna "J'ai besoin d'un avis honnête sur ce glaçage au chocolat."
    n "Elle trempe une cuillère dans le bol et me la tend."
    n "Le glaçage est riche, légèrement amer, absolument parfait."
    elio "C'est incroyable. Vraiment."
    vesna "C'est trop sucré ?"
    elio "C'est parfait. Exactement comme il faut."
    n "Elle rougit. Son bonheur est sincère et touchant."
    vesna "Si tu... si tu veux, tu peux rester goûter le résultat final ce soir ?"
    elio "Avec plaisir."
    $ affinity_vesna += 10
    hide vesna happy
    return

label pc_kitchen_zara_snack_d3:
    show zara laugh at right
    n "Zara est planquée derrière le réfrigérateur ouvert, en train de grignoter un croissant."
    n "Elle sursaute en m'entendant."
    zara "Je... je vérifiais les stocks !"
    elio "En mangeant le stock ?"
    zara "C'est une méthode de vérification empirique."
    elio "Je comprends pas."
    zara "Parfait. Viens, j'en ai un autre."
    n "On mange des croissants debout devant le frigo. C'est la meilleure chose de la journée."
    $ affinity_zara += 6
    hide zara laugh
    return

label pc_kitchen_ines_taste_d3:
    show ines smirk at right
    n "Ines est penchée sur un présentoir de vins, verre à la main."
    ines "Tu t'y connais en vin ?"
    elio "Pas vraiment."
    ines "Goûte."
    n "Elle me tend son verre. C'est un rouge légèrement boisé."
    elio "C'est bon."
    ines "C'est tout ce que tu as ?"
    elio "C'est bon... et ça me rappelle quelque chose que je saurai pas nommer."
    ines "..."
    ines "C'est la meilleure réponse que j'aie entendue."
    $ affinity_ines += 8
    hide ines smirk
    return

label pc_kitchen_herbs_d3:
    n "Un pot de basilic frais sur le rebord de la fenêtre."
    n "Je le sens. C'est l'été résumé en une odeur."
    n "Je le replace délicatement."
    return

label pc_kitchen_chocolate_d3:
    show vesna blush at right
    n "Une tablette de chocolat noir 70% avec une étiquette manuscrite : {i}« Recette spéciale – NE PAS TOUCHER »{/i}."
    n "Je m'apprête à reposer."
    vesna "Tu peux la prendre. C'est pour toi."
    elio "Hein ?"
    vesna "Je... j'en avais commandé exprès pour une recette que je voulais tester avec toi."
    vesna "Ce soir, si tu veux."
    n "Le ton de sa voix a changé. Plus doux. Presque un murmure."
    $ affinity_vesna += 10
    hide vesna blush
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
            text "❤ Zara  [affinity_zara]"  color "#FF9966" size 22
            text "❤ Vesna  [affinity_vesna]"  color "#FF99CC" size 22
            text "❤ Ines [affinity_ines]" color "#CC99FF" size 22
            if lou_available:
                text "❤ Lou [affinity_lou]" color "#99CCFF" size 22

    text "🌿 TERRASSE" xalign 0.5 ypos 30 size 36 color "#fff" outlines [(2,"#0005",0,0)]

    vbox:
        xpos 80 ypos 200
        spacing 16

        if "ines_massage" not in visited:
            textbutton "💆 Ines propose un massage 'pro'":
                style "hotspot_button"
                action Return("ines_massage")
        if "zara_hammock" not in visited:
            textbutton "🌴 Zara dans le hamac":
                style "hotspot_button"
                action Return("zara_hammock")
        if "spring" not in visited:
            textbutton "♨ Source chaude au fond du jardin":
                style "hotspot_button"
                action Return("spring")
        if "lou_roof" not in visited and lou_available:
            textbutton "🔭 Quelqu'un sur le toit ?":
                style "hotspot_button"
                action Return("lou_roof")
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

label pc_terrace_ines_massage_d5:
    show ines soft at right
    ines "Elio. Tu as l'air tendu."
    elio "C'est l'avant-dernier jour. Je suis nostalgique."
    ines "Assieds-toi."
    n "Elle me désigne une chaise longue. Je m'exécute sans trop savoir ce qui se passe."
    ines "Je suis formée en massage sportif. C'est professionnel."
    ines "Ne lis rien là-dedans."
    elio "Bien sûr."
    n "Ses mains sont fermes et précises. Absolument professionnelles."
    n "Jusqu'au moment où elles s'attardent un peu plus longtemps que nécessaire sur mes épaules."
    n "Aucun des deux n'en fait mention."
    ines "Mieux ?"
    elio "Beaucoup."
    $ affinity_ines += 12
    hide ines soft
    return

label pc_terrace_zara_hammock_d5:
    show zara laugh at right
    n "Zara se balance dans le hamac, les bras derrière la tête."
    zara "Elio ! Viens, y'a de la place."
    elio "Le hamac va pas craquer ?"
    zara "J'en sais rien. On peut tester."
    n "On teste. Le hamac tient. Mais c'est serré."
    n "On reste là vingt minutes à fixer le ciel et ne rien dire."
    n "C'est une des meilleures activités de la semaine."
    zara "...T'as mis de la crème aujourd'hui ?"
    elio "Oui."
    zara "Bien."
    $ affinity_zara += 8
    hide zara laugh
    return

label pc_terrace_spring_d5:
    show vesna shy at right
    n "La source chaude est cachée derrière les bougainvilliers, au fond du jardin."
    n "Je m'approche. Vesna est là — les pieds dans l'eau, yeux fermés."
    n "Elle ouvre les yeux en entendant mes pas."
    vesna "Oh ! Je pensais que personne connaissait cet endroit."
    elio "Je l'ai trouvé par hasard. Je peux rester ?"
    vesna "...Oui."
    n "On reste là en silence, les pieds dans l'eau chaude, le ciel qui vire à l'orange."
    n "Vesna a l'air plus détendue que je l'ai jamais vue."
    vesna "C'est mon endroit préféré ici."
    elio "Je comprends pourquoi."
    $ affinity_vesna += 12
    hide vesna shy
    return

label pc_terrace_lou_roof_d5:
    show lou tsundere at right
    n "Je lève les yeux. Lou est sur le toit, appuyée contre la cheminée."
    elio "Encore sur le toit ?"
    lou "Le toit, c'est calme."
    elio "Tu veux de la compagnie ?"
    lou "Non."
    n "Un silence."
    lou "...Tu peux monter si tu veux. L'échelle est derrière la remise."
    n "Je monte. On reste assis sur les tuiles chaudes à regarder la mer."
    lou "C'est mon endroit secret."
    elio "Je dirai rien."
    lou "Je sais."
    $ affinity_lou += 10
    hide lou tsundere
    return

label pc_terrace_sunset_d5:
    n "Le soleil touche l'horizon. Des oranges, des roses, des violets."
    n "Je m'assis sur les marches de la terrasse et je regarde."
    n "Il y a des moments dans la vie où on sait qu'on est exactement où il faut être."
    n "C'en est un."
    return
