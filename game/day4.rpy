# ════════════════════════════════════════════════════════
# SUMMER SHIFT – day4.rpy
# Jours 4 et 5 — Clara arrive le Jour 4
# ════════════════════════════════════════════════════════

# ════════════════════════════════════════════════════════
# JOUR 4
# ════════════════════════════════════════════════════════
label day4_morning:
    scene bg resort
    with dissolve

    $ clara_available = True    # Clara est arrivée

    n "{size=+6}{b}☀ Jour 4 – Matin{/b}{/size}"
    n "Je descends pour le petit-déjeuner et je trouve une inconnue assise à la table du personnel."
    n "Dix-huit ans, cheveux courts, t-shirt à rayures. Elle regarde son téléphone en ignorant tout le monde."

    show sofia confident at right
    show clara tsundere at left

    sofia "Alex. Je te présente Clara, ma nièce."
    sofia "Elle passe quelques jours pour donner un coup de main."
    sofia "Clara, dis bonjour."

    clara "..."
    clara "Bonjour."

    n "Elle lève les yeux de son téléphone le temps de me jeter un regard, puis le rebaisse."
    n "Super accueil."

    alex "Bonjour ! Je suis Alex."
    clara "Je sais. Tata m'a dit."

    hide sofia confident
    hide clara tsundere

    n "Et voilà. Fin de la conversation."
    n "Bon. Le Jour 4 commence. Le soleil brille, il reste trois jours."
    n "Je sens que la semaine accélère."

    menu:
        "Essayer d'engager la conversation avec Clara.":
            $ affinity_clara += 10
            jump day4_morning_clara
        "Retrouver Lina pour la session de plage prévue.":
            $ affinity_lina += 10
            jump day4_morning_lina
        "Aller voir si Mina a besoin d'aide en cuisine.":
            $ affinity_mina += 10
            jump day4_morning_mina

label day4_morning_clara:
    scene bg terrace
    with dissolve
    show clara tsundere at right

    n "Je sors sur la terrasse avec mon café. Clara est là, appuyée contre la rambarde."

    alex "Belle vue, hein ?"
    clara "C'est une mer. Comme partout sur la côte."
    alex "...C'est vrai."
    clara "T'avais quoi en tête comme entrée en matière ?"
    alex "Honnêtement ? Je savais pas."

    n "Un silence. Puis elle rit. Juste un peu. Très vite réprimé."

    clara "Au moins t'es honnête."
    alex "Je fais de mon mieux."
    clara "Sofia dit que t'es utile."
    alex "C'est son plus grand compliment."
    clara "Je sais. C'est pour ça que je te le dis."

    n "Elle retourne à son téléphone. Mais cette fois elle ne s'éloigne pas."

    hide clara tsundere
    jump day4_afternoon_intro

label day4_morning_lina:
    scene bg beach
    with dissolve
    show lina swimsuit at right

    n "Lina m'attendait à la plage avec deux raquettes et un sourire dangereux."

    lina "BEACH VOLLEY !"
    alex "C'est une invitation ou une déclaration de guerre ?"
    lina "Les deux. On joue ?"

    n "On joue. Lina est étonnamment bonne — pour quelqu'un qui renverse des verres en permanence."
    n "On transpire, on rit, on rate des smashes ridicules."

    lina "T'es nul !"
    alex "Je suis débutant."
    lina "C'est pareil !"

    n "À un moment, elle plonge pour attraper la balle, glisse, et m'entraîne dans sa chute."
    n "On finit tous les deux sur le sable, à bout de souffle."

    lina "...Ça compte comme un point pour moi ?"
    alex "Absolument pas."
    lina "Boo."

    hide lina swimsuit
    jump day4_afternoon_intro

label day4_morning_mina:
    scene bg kitchen
    with dissolve
    show mina happy at right

    mina "Alex ! Parfait timing."
    mina "J'essaie une recette de fondant au chocolat et j'ai besoin d'un avis sur la texture."
    alex "Je suis disponible pour souffrir de cette façon."
    mina "Ha... tu souffres pas, là."

    n "Elle rit — un petit rire discret qu'elle cache derrière sa main."
    n "Je goûte le fondant. Il est parfait."

    alex "Mina... tu es sérieusement trop douée."
    mina "C'est trop sucré ?"
    alex "C'est parfait. Vraiment."

    n "Elle regarde son fondant, puis moi, puis son fondant."

    mina "J'ai aussi une ganache au chocolat blanc. C'est... elle est un peu expérimentale."
    alex "Je prends le risque."

    hide mina happy
    jump day4_afternoon_intro

# ── Après-midi Jour 4 – Plage (Clara déambule) ──────────
label day4_afternoon_intro:
    scene bg beach
    with dissolve

    n "{size=+6}{b}🏖 Jour 4 – Après-midi{/b}{/size}"
    n "L'après-midi retour à la plage. Le soleil est à son pic."
    n "Clara rôde dans le coin — à distance, mais elle est là."

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
    elif _girl == "lina":
        jump ev_lina_d4
    elif _girl == "mina":
        jump ev_mina_d4
    elif _girl == "sofia":
        jump ev_sofia_d4
    else:
        jump ev_clara_d4

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
        "Rejoindre Lina pour l'inventaire du bar (et ses blagues).":
            $ affinity_lina += 10
            jump day5_morning_lina
        "Aider Mina à préparer le dîner spécial du soir.":
            $ affinity_mina += 10
            jump day5_morning_mina
        "Accompagner Sofia pour sa promenade matinale.":
            $ affinity_sofia += 10
            jump day5_morning_sofia
        "Chercher Clara, qui a mystérieusement disparu.":
            $ affinity_clara += 10
            jump day5_morning_clara

label day5_morning_lina:
    scene bg bar
    with dissolve
    show lina happy at right

    n "Le bar du matin est calme. Lina compte des bouteilles en marmonnant des chiffres aléatoires."

    lina "Sept... huit... attends non— Alex ! Recommence depuis le début avec moi."
    alex "Tu veux que je compte tes bouteilles ?"
    lina "Je veux quelqu'un qui compte pendant que moi j'essaie de pas me perdre."
    alex "C'est une stratégie intéressante."

    n "On compte. Ça prend trois fois plus longtemps que nécessaire mais c'est bien plus drôle."

    lina "Alex ?"
    alex "Hm ?"
    lina "Quand tu repars, là... l'été finit et tout..."
    lina "C'est dommage."
    alex "Ouais."
    lina "Enfin bref ! Vingt-deux, vingt-trois..."

    hide lina happy
    jump day5_afternoon_intro

label day5_morning_mina:
    scene bg kitchen
    with dissolve
    show mina happy at right

    n "Mina prépare une sauce lentement, en ajoutant des épices avec soin."

    alex "Je peux aider ?"
    mina "Tu peux... goûter et me dire si c'est assez relevé ?"
    alex "Toujours."

    n "La sauce est incroyable."

    alex "T'as envisagé d'ouvrir ton propre restaurant ?"
    mina "Parfois. Mais c'est... intimidant."
    alex "Tu cuisines mieux que la moitié des chefs que j'ai vus à la télé."
    mina "Tu regardes des émissions de cuisine ?"
    alex "Maintenant oui."

    n "Elle rit — vraiment cette fois — et ne cache pas son sourire."

    hide mina happy
    jump day5_afternoon_intro

label day5_morning_sofia:
    scene bg beach
    with dissolve
    show sofia soft at right

    n "Sofia marche pieds nus dans le sable, paréo flottant dans le vent."
    n "Je l'ai rejointe sans vraiment réfléchir."

    sofia "Tu te lèves tôt."
    alex "Toi aussi."
    sofia "J'ai pas trop le choix. Le resort se réveille avec moi."
    alex "Ça t'arrive de prendre du temps pour toi ?"
    sofia "..."
    sofia "Tu poses des questions directes pour quelqu'un qui travaille pour moi."
    alex "Désolé, je—"
    sofia "Non. C'est... bien."

    n "On marche en silence un moment. Un silence confortable."

    sofia "Parfois j'oublie que j'ai le droit de ne pas gérer, juste un instant."
    sofia "Merci de me le rappeler."

    hide sofia soft
    jump day5_afternoon_intro

label day5_morning_clara:
    scene bg room
    with dissolve
    show clara blush at right

    n "Je cherche Clara et la trouve sur le toit-terrasse au-dessus des chambres."
    n "Elle regarde quelque chose avec son téléphone. Ou plutôt... elle regardait quelque chose. Elle a sursauté."

    clara "Quoi ?! T'es là depuis quand ?"
    alex "Je viens d'arriver."
    clara "Bien. Parce que sinon... bref."
    alex "Tu regardais quoi ?"
    clara "La mer. C'est autorisé ?"
    alex "Évidemment."

    n "Un silence."

    clara "...T'as pas un truc à faire ?"
    alex "J'avais quelqu'un à trouver."
    clara "Et tu m'as trouvée. Bingo. Tu peux repartir."
    alex "Je suis bien ici."
    clara "..."
    clara "Très bien."

    n "On reste là cinq minutes. Elle fait semblant d'ignorer que je suis là. Moi aussi."
    n "C'est étrangement agréable."

    hide clara blush
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
    elif _girl == "lina":
        jump ev_lina_d5
    elif _girl == "mina":
        jump ev_mina_d5
    elif _girl == "sofia":
        jump ev_sofia_d5
    else:
        jump ev_clara_d5
