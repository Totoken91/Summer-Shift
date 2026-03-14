# ════════════════════════════════════════════════════════
# SUMMER SHIFT – script.rpy
# Point d'entrée + Jour 1 complet + routeur de jours
# ════════════════════════════════════════════════════════

# ── Routeur principal ────────────────────────────────────
label day_router:
    if current_day == 1:
        jump day1_morning
    elif current_day == 2:
        jump day2_morning
    elif current_day == 3:
        jump day3_morning
    elif current_day == 4:
        jump day4_morning
    elif current_day == 5:
        jump day5_morning
    elif current_day == 6:
        jump day6_morning
    elif current_day == 7:
        jump day7_morning
    else:
        jump ending_router

# ════════════════════════════════════════════════════════
# INTRODUCTION
# ════════════════════════════════════════════════════════
label start:
    scene bg resort
    with fade

    n "Juillet. Trente-sept degrés à l'ombre, et l'air sent le sel et la crème solaire."
    n "Moi, Alex, 19 ans, fauché mais pas idiot, j'ai signé pour un été à {b}La Vague Dorée{/b}, un resort côtier oublié des touristes depuis la tempête."
    n "La patronne, Sofia Marchetti, dirige l'endroit d'une main de fer dans un gant de soie depuis dix ans."
    n "Presque personne cet été. Juste trois femmes… et moi."
    n "Un job tranquille, qu’ils disaient."
    n "J’ai déjà des doutes."

    jump day1_morning

# ════════════════════════════════════════════════════════
# JOUR 1
# ════════════════════════════════════════════════════════
label day1_morning:
    scene bg resort
    with dissolve

    n "{size=+6}{b}☀ Jour 1 – Matin{/b}{/size}"

    n "Le taxi me lâche devant la façade blanche aux volets bleus délavés. La mer miroite comme un miroir brûlant."
    n "Avant que je toque, la porte s’ouvre. Une silhouette apparaît."

    show sofia confident at right
    with dissolve

    sofia "Alex, c’est ça ? Sofia Marchetti. Bienvenue."
    sofia "Pose ton sac. Je te présente l’équipe."

    n "La trentaine élégante. Paréo crème noué bas sur les hanches, maillot bordeaux qui épouse des courbes généreuses sans rien cacher. Son regard me détaille de haut en bas, lentement. Je sens mes épaules se redresser instinctivement."

    alex "Bonjour, madame Marchetti. Enchanté de—"

    show lina happy at left
    with easeinleft

    lina "NOUVEAU !!!"

    n "Un plateau jaillit du couloir et s’écrase contre mon épaule – vide, Dieu merci. La coupable plaque une main sur sa bouche, yeux écarquillés."

    lina "Merde ! Pardon ! T’es entier ? J’ai pas vu que t’étais là, il a glissé, je—"
    sofia "Lina."
    lina "Oui madame !"
    sofia "Inspire."
    lina "… Oui madame."

    n "Elle expire bruyamment, puis me tend une main avec un sourire éclatant qui fait danser une fossette."

    lina "Lina ! Barmaid, serveuse, et championne toutes catégories de petites catastrophes."
    lina "Tkt, je progresse. L’an dernier j’aurais aussi renversé le mojito dessus."

    alex "C’est… rassurant."
    lina "Hein ? Grave !"

    hide lina happy
    with easeoutleft

    show mina shy at left
    with easeinleft

    sofia "Et voici Mina, notre cuisinière."

    n "Une silhouette menue se glisse dans l’embrasure de la porte de service. Cheveux bruns attachés à la va-vite, tablier qui souligne une taille fine."

    mina "B… bonjour… Mina. Je suis la chef."
    mina "J’ai… fait des croissants. Si tu veux goûter…"

    n "Ses joues rosissent jusqu’aux oreilles. On dirait qu’elle vient de proposer un strip-tease plutôt qu’un petit-déj."

    alex "Avec plaisir, merci. Ça sent divinement bon."
    mina "Oh… c’est rien… vraiment…"

    hide mina shy
    with easeoutleft

    sofia "Voilà l’équipe. Toi, tu seras l’homme à tout faire : ménage, courses, renfort en salle ou en cuisine quand ça chauffe."
    sofia "Et essaie de limiter les dégâts. Lina a déjà le monopole."

    n "Un sourire très bref passe sur ses lèvres – carnassier, presque. Je déglutis."

    n "On me montre ma chambre – lit double, vue sur le jardin, ventilateur qui ronronne doucement – puis je donne un coup de main aux tâches matinales."
    n "Vers 11 h, j’ai enfin un moment de répit avant le service déjeuner."

    menu:
        "Aller traîner avec Lina au bar.":
            $ affinity_lina += 10
            jump day1_help_lina
        "Proposer un coup de main à Mina en cuisine.":
            $ affinity_mina += 10
            jump day1_help_mina
        "Demander à Sofia s’il y a quelque chose d’utile à faire.":
            $ affinity_sofia += 10
            jump day1_help_sofia

# ── Fin de matinée Jour 1 ───────────────────────────────
label day1_help_lina:
    scene bg bar
    with dissolve
    show lina happy at right

    n "Lina est derrière le comptoir, short en jean coupé très haut, débardeur moulant taché de citron. Elle range des verres en se dandinant sur une musique imaginaire."

    lina "Oh putain, Alex ! T’es venu m’aider ? T’es un ange."
    alex "Je connais rien au bar, mais je peux essayer…"
    lina "Parfait ! Les mecs qui savent pas ont moins peur de renverser. C’est statistique."
    alex "T’as des stats là-dessus ?"
    lina "Pas encore. Mais je vais en tenir à partir d’aujourd’hui."

    n "On passe une heure à ranger, à rigoler, à éviter les désastres. Elle se penche souvent – très souvent – pour ramasser des trucs. Je fais semblant de ne pas remarquer la courbe de ses reins quand elle se cambre."

    n "Bilan : deux verres explosés. Les deux par Lina, évidemment."

    lina "Pas mon record du mois."
    alex "C’est positif ou négatif ?"
    lina "Positif. D’habitude j’en explose trois… et parfois sur un client."

    hide lina happy
    jump day1_afternoon_intro

label day1_help_mina:
    scene bg kitchen
    with dissolve
    show mina apron at right

    n "La cuisine est d’une propreté irréelle. Mina trie des herbes, tablier noué serré, une mèche qui colle à sa nuque moite de chaleur."

    mina "Oh… tu… tu veux aider ?"
    alex "Si je dérange pas."
    mina "Non ! Pas du tout ! Enfin… je veux dire… merci."

    n "Elle me tend un tablier. Nos doigts se frôlent une seconde de trop. Elle rougit encore plus fort."

    mina "Tu sais éplucher ?"
    alex "À peu près."
    mina "Je vais t’apprendre. Le geste compte. Faut… caresser la peau du légume, pas l’arracher."

    n "Elle se place derrière moi pour guider ma main. Son souffle chaud dans mon cou. Je rate exprès le deuxième légume juste pour la sentir se coller un peu plus."

    n "Une heure passe. Sa voix douce, ses corrections patientes, la façon dont elle mordille sa lèvre quand je réussis… J’oublie presque qu’on cuisine."

    hide mina apron
    jump day1_afternoon_intro

label day1_help_sofia:
    scene bg terrace
    with dissolve
    show sofia confident at right

    n "Sofia est installée sur la terrasse, jambes croisées, carnet sur les genoux. Son paréo s’est entrouvert juste assez pour laisser deviner la naissance de sa poitrine."

    alex "Madame Marchetti ? Besoin d’un coup de main ?"
    sofia "Tutoie-moi, Alex. ‘Madame’ me donne l’impression d’être ta prof de maths."
    sofia "Oui. Ce parasol est mort. Boîte à outils dans le local, deuxième porte."

    n "Je m’active sous ses yeux. Elle ne parle presque pas, mais son regard suit chacun de mes gestes comme si elle évaluait… autre chose que mes talents de bricoleur."

    sofia "Pas mal. Tu te débrouilles."
    alex "C’était un compliment ?"
    sofia "Dans ma bouche, oui. Profites-en, ça n’arrive pas tous les jours."

    n "Elle se lève lentement, le tissu glisse sur sa cuisse. Je détourne les yeux une seconde trop tard."

    hide sofia confident
    jump day1_afternoon_intro

# ════════════════════════════════════════════════════════
# APRÈS-MIDI JOUR 1 – Plage
# ════════════════════════════════════════════════════════
label day1_afternoon_intro:
    scene bg beach
    with dissolve

    n "{size=+6}{b}🏖 Jour 1 – Après-midi{/b}{/size}"
    n "Déjeuner fini. La plage privée est déserte. Le soleil cogne. Ma peau brûle déjà."
    n "Je pars marcher, torse nu, short mouillé par l’écume."

    call afternoon_beach(1)

    jump day1_evening

# ════════════════════════════════════════════════════════
# SOIR JOUR 1
# ════════════════════════════════════════════════════════
label day1_evening:
    scene bg terrace
    with dissolve

    n "{size=+6}{b}🌅 Jour 1 – Soir{/b}{/size}"

    $ _girl, _score = top_girl()

    if _score < 20:
        jump ev_solo_d1
    elif _girl == "lina":
        jump ev_lina_d1
    elif _girl == "mina":
        jump ev_mina_d1
    else:
        jump ev_sofia_d1

label ev_solo_d1:
    scene bg terrace
    n "Je m’affale sur un transat avec une limonade glacée. La mer est violette maintenant."
    n "Première journée. Chaude. Très chaude."
    n "Et ce n’est que le début."
    $ current_day += 1
    jump day_router