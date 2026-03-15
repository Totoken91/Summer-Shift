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
    n "Moi, Elio, 19 ans, fauché mais pas idiot, j'ai signé pour un été à {b}La Vague Dorée{/b}, un resort côtier oublié des touristes depuis la tempête."
    n "La patronne, Ines Marchetti, dirige l'endroit d'une main de fer dans un gant de soie depuis dix ans."
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

    show ines confident at right
    with dissolve

    ines "Elio, c’est ça ? Ines Marchetti. Bienvenue."
    ines "Pose ton sac. Je te présente l’équipe."

    n "La trentaine élégante. Paréo crème noué bas sur les hanches, maillot bordeaux qui épouse des courbes généreuses sans rien cacher. Son regard me détaille de haut en bas, lentement. Je sens mes épaules se redresser instinctivement."

    elio "Bonjour, madame Marchetti. Enchanté de—"

    show zara happy at left
    with easeinleft

    zara "NOUVEAU !!!"

    n "Un plateau jaillit du couloir et s’écrase contre mon épaule – vide, Dieu merci. La coupable plaque une main sur sa bouche, yeux écarquillés."

    zara "Merde ! Pardon ! T’es entier ? J’ai pas vu que t’étais là, il a glissé, je—"
    ines "Zara."
    zara "Oui madame !"
    ines "Inspire."
    zara "… Oui madame."

    n "Elle expire bruyamment, puis me tend une main avec un sourire éclatant qui fait danser une fossette."

    zara "Zara ! Barmaid, serveuse, et championne toutes catégories de petites catastrophes."
    zara "Tkt, je progresse. L’an dernier j’aurais aussi renversé le mojito dessus."

    elio "C’est… rassurant."
    zara "Hein ? Grave !"

    hide zara happy
    with easeoutleft

    show vesna shy at left
    with easeinleft

    ines "Et voici Vesna, notre cuisinière."

    n "Une silhouette menue se glisse dans l’embrasure de la porte de service. Cheveux bruns attachés à la va-vite, tablier qui souligne une taille fine."

    vesna "B… bonjour… Vesna. Je suis la chef."
    vesna "J’ai… fait des croissants. Si tu veux goûter…"

    n "Ses joues rosissent jusqu’aux oreilles. On dirait qu’elle vient de proposer un strip-tease plutôt qu’un petit-déj."

    elio "Avec plaisir, merci. Ça sent divinement bon."
    vesna "Oh… c’est rien… vraiment…"

    hide vesna shy
    with easeoutleft

    ines "Voilà l’équipe. Toi, tu seras l’homme à tout faire : ménage, courses, renfort en salle ou en cuisine quand ça chauffe."
    ines "Et essaie de limiter les dégâts. Zara a déjà le monopole."

    n "Un sourire très bref passe sur ses lèvres – carnassier, presque. Je déglutis."

    n "On me montre ma chambre – lit double, vue sur le jardin, ventilateur qui ronronne doucement – puis je donne un coup de main aux tâches matinales."
    n "Vers 11 h, j’ai enfin un moment de répit avant le service déjeuner."

    menu:
        "Aller traîner avec Zara au bar.":
            $ affinity_zara += 10
            jump day1_help_zara
        "Proposer un coup de main à Vesna en cuisine.":
            $ affinity_vesna += 10
            jump day1_help_vesna
        "Demander à Ines s’il y a quelque chose d’utile à faire.":
            $ affinity_ines += 10
            jump day1_help_ines

# ── Fin de matinée Jour 1 ───────────────────────────────
label day1_help_zara:
    scene bg bar
    with dissolve
    show zara happy at right

    n "Zara est derrière le comptoir, short en jean coupé très haut, débardeur moulant taché de citron. Elle range des verres en se dandinant sur une musique imaginaire."

    zara "Oh putain, Elio ! T’es venu m’aider ? T’es un ange."
    elio "Je connais rien au bar, mais je peux essayer…"
    zara "Parfait ! Les mecs qui savent pas ont moins peur de renverser. C’est statistique."
    elio "T’as des stats là-dessus ?"
    zara "Pas encore. Mais je vais en tenir à partir d’aujourd’hui."

    n "On passe une heure à ranger, à rigoler, à éviter les désastres. Elle se penche souvent – très souvent – pour ramasser des trucs. Je fais semblant de ne pas remarquer la courbe de ses reins quand elle se cambre."

    n "Bilan : deux verres explosés. Les deux par Zara, évidemment."

    zara "Pas mon record du mois."
    elio "C’est positif ou négatif ?"
    zara "Positif. D’habitude j’en explose trois… et parfois sur un client."

    hide zara happy
    jump day1_afternoon_intro

label day1_help_vesna:
    scene bg kitchen
    with dissolve
    show vesna apron at right

    n "La cuisine est d’une propreté irréelle. Vesna trie des herbes, tablier noué serré, une mèche qui colle à sa nuque moite de chaleur."

    vesna "Oh… tu… tu veux aider ?"
    elio "Si je dérange pas."
    vesna "Non ! Pas du tout ! Enfin… je veux dire… merci."

    n "Elle me tend un tablier. Nos doigts se frôlent une seconde de trop. Elle rougit encore plus fort."

    vesna "Tu sais éplucher ?"
    elio "À peu près."
    vesna "Je vais t’apprendre. Le geste compte. Faut… caresser la peau du légume, pas l’arracher."

    n "Elle se place derrière moi pour guider ma main. Son souffle chaud dans mon cou. Je rate exprès le deuxième légume juste pour la sentir se coller un peu plus."

    n "Une heure passe. Sa voix douce, ses corrections patientes, la façon dont elle mordille sa lèvre quand je réussis… J’oublie presque qu’on cuisine."

    hide vesna apron
    jump day1_afternoon_intro

label day1_help_ines:
    scene bg terrace
    with dissolve
    show ines confident at right

    n "Ines est installée sur la terrasse, jambes croisées, carnet sur les genoux. Son paréo s’est entrouvert juste assez pour laisser deviner la naissance de sa poitrine."

    elio "Madame Marchetti ? Besoin d’un coup de main ?"
    ines "Tutoie-moi, Elio. ‘Madame’ me donne l’impression d’être ta prof de maths."
    ines "Oui. Ce parasol est mort. Boîte à outils dans le local, deuxième porte."

    n "Je m’active sous ses yeux. Elle ne parle presque pas, mais son regard suit chacun de mes gestes comme si elle évaluait… autre chose que mes talents de bricoleur."

    ines "Pas mal. Tu te débrouilles."
    elio "C’était un compliment ?"
    ines "Dans ma bouche, oui. Profites-en, ça n’arrive pas tous les jours."

    n "Elle se lève lentement, le tissu glisse sur sa cuisse. Je détourne les yeux une seconde trop tard."

    hide ines confident
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
    elif _girl == "zara":
        jump ev_zara_d1
    elif _girl == "vesna":
        jump ev_vesna_d1
    else:
        jump ev_ines_d1

label ev_solo_d1:
    scene bg terrace
    n "Je m’affale sur un transat avec une limonade glacée. La mer est violette maintenant."
    n "Première journée. Chaude. Très chaude."
    n "Et ce n’est que le début."
    $ current_day += 1
    jump day_router