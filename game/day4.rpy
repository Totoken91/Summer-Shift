# ════════════════════════════════════════════════════════
# SUMMER SHIFT – day4.rpy
# Jours 4 et 5 — Lou arrive le Jour 4
# ════════════════════════════════════════════════════════

# ════════════════════════════════════════════════════════
# JOUR 4
# ════════════════════════════════════════════════════════
label day4_morning:
    scene bg resort
    with dissolve

    $ lou_available = True    # Lou est arrivée

    n "{size=+6}{b}☀ Jour 4 – Matin{/b}{/size}"
    n "Je descends pour le petit-déjeuner et je trouve une inconnue assise à la table du personnel."
    n "Dix-huit ans, cheveux courts, t-shirt à rayures. Elle regarde son téléphone en ignorant tout le monde."

    show ines confident at right
    show lou tsundere at left

    ines "Elio. Je te présente Lou, ma nièce."
    ines "Elle passe quelques jours pour donner un coup de main."
    ines "Lou, dis bonjour."

    lou "..."
    lou "Bonjour."

    n "Elle lève les yeux de son téléphone le temps de me jeter un regard, puis le rebaisse."
    n "Super accueil."

    elio "Bonjour ! Je suis Elio."
    lou "Je sais. Tata m'a dit."

    hide ines confident
    hide lou tsundere

    n "Et voilà. Fin de la conversation."
    n "Bon. Le Jour 4 commence. Le soleil brille, il reste trois jours."
    n "Je sens que la semaine accélère."

    menu:
        "Essayer d'engager la conversation avec Lou.":
            $ affinity_lou += 10
            jump day4_morning_lou
        "Retrouver Zara pour la session de plage prévue.":
            $ affinity_zara += 10
            jump day4_morning_zara
        "Aller voir si Vesna a besoin d'aide en cuisine.":
            $ affinity_vesna += 10
            jump day4_morning_vesna

label day4_morning_lou:
    scene bg terrace
    with dissolve
    show lou tsundere at right

    n "Je sors sur la terrasse avec mon café. Lou est là, appuyée contre la rambarde."

    elio "Belle vue, hein ?"
    lou "C'est une mer. Comme partout sur la côte."
    elio "...C'est vrai."
    lou "T'avais quoi en tête comme entrée en matière ?"
    elio "Honnêtement ? Je savais pas."

    n "Un silence. Puis elle rit. Juste un peu. Très vite réprimé."

    lou "Au moins t'es honnête."
    elio "Je fais de mon mieux."
    lou "Ines dit que t'es utile."
    elio "C'est son plus grand compliment."
    lou "Je sais. C'est pour ça que je te le dis."

    n "Elle retourne à son téléphone. Mais cette fois elle ne s'éloigne pas."

    hide lou tsundere
    jump day4_afternoon_intro

label day4_morning_zara:
    scene bg beach
    with dissolve
    show zara swimsuit at right

    n "Zara m'attendait à la plage avec deux raquettes et un sourire dangereux."

    zara "BEACH VOLLEY !"
    elio "C'est une invitation ou une déloution de guerre ?"
    zara "Les deux. On joue ?"

    n "On joue. Zara est étonnamment bonne — pour quelqu'un qui renverse des verres en permanence."
    n "On transpire, on rit, on rate des smashes ridicules."

    zara "T'es nul !"
    elio "Je suis débutant."
    zara "C'est pareil !"

    n "À un moment, elle plonge pour attraper la balle, glisse, et m'entraîne dans sa chute."
    n "On finit tous les deux sur le sable, à bout de souffle."

    zara "...Ça compte comme un point pour moi ?"
    elio "Absolument pas."
    zara "Boo."

    hide zara swimsuit
    jump day4_afternoon_intro

label day4_morning_vesna:
    scene bg kitchen
    with dissolve
    show vesna happy at right

    vesna "Elio ! Parfait timing."
    vesna "J'essaie une recette de fondant au chocolat et j'ai besoin d'un avis sur la texture."
    elio "Je suis disponible pour souffrir de cette façon."
    vesna "Ha... tu souffres pas, là."

    n "Elle rit — un petit rire discret qu'elle cache derrière sa main."
    n "Je goûte le fondant. Il est parfait."

    elio "Vesna... tu es sérieusement trop douée."
    vesna "C'est trop sucré ?"
    elio "C'est parfait. Vraiment."

    n "Elle regarde son fondant, puis moi, puis son fondant."

    vesna "J'ai aussi une ganache au chocolat blanc. C'est... elle est un peu expérimentale."
    elio "Je prends le risque."

    hide vesna happy
    jump day4_afternoon_intro

# ── Après-midi Jour 4 – Plage (Lou déambule) ──────────
label day4_afternoon_intro:
    scene bg beach
    with dissolve

    n "{size=+6}{b}🏖 Jour 4 – Après-midi{/b}{/size}"
    n "L'après-midi retour à la plage. Le soleil est à son pic."
    n "Lou rôde dans le coin — à distance, mais elle est là."

    call afternoon_beach(4)

    jump day4_evening

# ── Soir Jour 4 ──────────────────────────────────────────
label day4_evening:
    scene bg terrace
    with dissolve

    n "{size=+6}{b}🌅 Jour 4 – Soir{/b}{/size}"

    $ _girl, _score = top_girl()

    if _score < 30:
        n "Soirée calme. On dîne tous ensemble pour une fois, et c'est agréable."
        $ current_day += 1
        jump day_router
    elif _girl == "zara":
        jump ev_zara_d4
    elif _girl == "vesna":
        jump ev_vesna_d4
    elif _girl == "ines":
        jump ev_ines_d4
    else:
        jump ev_lou_d4

# ════════════════════════════════════════════════════════
# JOUR 5
# ════════════════════════════════════════════════════════
label day5_morning:
    scene bg resort
    with dissolve

    n "{size=+6}{b}☀ Jour 5 – Matin{/b}{/size}"
    n "Avant-dernier jour complet. L'air est lourd, le soleil impitoyable."
    n "Je sens que chaque conversation compte un peu plus aujourd'hui."

    menu:
        "Rejoindre Zara pour l'inventaire du bar (et ses blagues).":
            $ affinity_zara += 10
            jump day5_morning_zara
        "Aider Vesna à préparer le dîner spécial du soir.":
            $ affinity_vesna += 10
            jump day5_morning_vesna
        "Accompagner Ines pour sa promenade matinale.":
            $ affinity_ines += 10
            jump day5_morning_ines
        "Chercher Lou, qui a mystérieusement disparu.":
            $ affinity_lou += 10
            jump day5_morning_lou

label day5_morning_zara:
    scene bg bar
    with dissolve
    show zara happy at right

    n "Le bar du matin est calme. Zara compte des bouteilles en marmonnant des chiffres aléatoires."

    zara "Sept... huit... attends non— Elio ! Recommence depuis le début avec moi."
    elio "Tu veux que je compte tes bouteilles ?"
    zara "Je veux quelqu'un qui compte pendant que moi j'essaie de pas me perdre."
    elio "C'est une stratégie intéressante."

    n "On compte. Ça prend trois fois plus longtemps que nécessaire mais c'est bien plus drôle."

    zara "Elio ?"
    elio "Hm ?"
    zara "Quand tu repars, là... l'été finit et tout..."
    zara "C'est dommage."
    elio "Ouais."
    zara "Enfin bref ! Vingt-deux, vingt-trois..."

    hide zara happy
    jump day5_afternoon_intro

label day5_morning_vesna:
    scene bg kitchen
    with dissolve
    show vesna happy at right

    n "Vesna prépare une sauce lentement, en ajoutant des épices avec soin."

    elio "Je peux aider ?"
    vesna "Tu peux... goûter et me dire si c'est assez relevé ?"
    elio "Toujours."

    n "La sauce est incroyable."

    elio "T'as envisagé d'ouvrir ton propre restaurant ?"
    vesna "Parfois. Mais c'est... intimidant."
    elio "Tu cuisines mieux que la moitié des chefs que j'ai vus à la télé."
    vesna "Tu regardes des émissions de cuisine ?"
    elio "Maintenant oui."

    n "Elle rit — vraiment cette fois — et ne cache pas son sourire."

    hide vesna happy
    jump day5_afternoon_intro

label day5_morning_ines:
    scene bg beach
    with dissolve
    show ines soft at right

    n "Ines marche pieds nus dans le sable, paréo flottant dans le vent."
    n "Je l'ai rejointe sans vraiment réfléchir."

    ines "Tu te lèves tôt."
    elio "Toi aussi."
    ines "J'ai pas trop le choix. Le resort se réveille avec moi."
    elio "Ça t'arrive de prendre du temps pour toi ?"
    ines "..."
    ines "Tu poses des questions directes pour quelqu'un qui travaille pour moi."
    elio "Désolé, je—"
    ines "Non. C'est... bien."

    n "On marche en silence un moment. Un silence confortable."

    ines "Parfois j'oublie que j'ai le droit de ne pas gérer, juste un instant."
    ines "Merci de me le rappeler."

    hide ines soft
    jump day5_afternoon_intro

label day5_morning_lou:
    scene bg room
    with dissolve
    show lou blush at right

    n "Je cherche Lou et la trouve sur le toit-terrasse au-dessus des chambres."
    n "Elle regarde quelque chose avec son téléphone. Ou plutôt... elle regardait quelque chose. Elle a sursauté."

    lou "Quoi ?! T'es là depuis quand ?"
    elio "Je viens d'arriver."
    lou "Bien. Parce que sinon... bref."
    elio "Tu regardais quoi ?"
    lou "La mer. C'est autorisé ?"
    elio "Évidemment."

    n "Un silence."

    lou "...T'as pas un truc à faire ?"
    elio "J'avais quelqu'un à trouver."
    lou "Et tu m'as trouvée. Bingo. Tu peux repartir."
    elio "Je suis bien ici."
    lou "..."
    lou "Très bien."

    n "On reste là cinq minutes. Elle fait semblant d'ignorer que je suis là. Moi aussi."
    n "C'est étrangement agréable."

    hide lou blush
    jump day5_afternoon_intro

# ── Après-midi Jour 5 – Terrasse ────────────────────────
label day5_afternoon_intro:
    scene bg terrace
    with dissolve

    n "{size=+6}{b}🌿 Jour 5 – Après-midi{/b}{/size}"
    n "L'après-midi se passe sur la terrasse et autour de la source chaude au fond du jardin."

    call afternoon_terrace(5)

    jump day5_evening

# ── Soir Jour 5 ──────────────────────────────────────────
label day5_evening:
    scene bg terrace
    with dissolve

    n "{size=+6}{b}🌅 Jour 5 – Soir{/b}{/size}"

    $ _girl, _score = top_girl()

    if _score < 40:
        n "La soirée passe doucement. Tout le monde est un peu fatigué, un peu mélancolique."
        n "Il ne reste plus qu'un jour et demi."
        $ current_day += 1
        jump day_router
    elif _girl == "zara":
        jump ev_zara_d5
    elif _girl == "vesna":
        jump ev_vesna_d5
    elif _girl == "ines":
        jump ev_ines_d5
    else:
        jump ev_lou_d5
