# ════════════════════════════════════════════════════════
# SUMMER SHIFT – day2.rpy
# Jours 2 et 3
# ════════════════════════════════════════════════════════

# ════════════════════════════════════════════════════════
# JOUR 2
# ════════════════════════════════════════════════════════
label day2_morning:
    scene bg resort
    with dissolve

    n "{size=+6}{b}☀ Jour 2 – Matin{/b}{/size}"
    n "Le soleil tape déjà fort quand je descends. Mon short colle un peu à la peau après une nuit agitée – rêves trop vifs sur les trois femmes d'ici."
    n "Petit-déjeuner sur la terrasse. Sofia, en bikini triangle noir sous un kimono entrouvert, distribue les tâches d'une voix calme mais autoritaire."

    show sofia confident at right

    sofia "Alex. Aujourd'hui, on accélère. Réparations, réassort, et un œil sur les clients qui pourraient arriver."
    sofia "On est peu, mais on reste professionnels… même si la chaleur rend tout un peu plus… distrayant."
    alex "Je gère. Promis."
    sofia "J'espère. Ton corps semble déjà s'adapter au climat."

    n "Son regard glisse sur mon torse nu un instant. Je sens la chair de poule malgré les 30°C."

    hide sofia confident

    n "Qui accompagner ce matin ? La chaleur monte déjà."

    menu:
        "Rejoindre Lina qui range les chaises longues sur la plage.":
            $ affinity_lina += 10
            jump day2_morning_lina
        "Aider Mina à préparer le buffet du déjeuner.":
            $ affinity_mina += 10
            jump day2_morning_mina
        "Suivre Sofia pour l'inventaire des chambres.":
            $ affinity_sofia += 10
            jump day2_morning_sofia

label day2_morning_lina:
    scene bg beach
    with dissolve
    show lina happy at right

    n "Lina est déjà en sueur : bikini string jaune fluo, top de sport coupé court qui remonte à chaque mouvement. Ses seins rebondissent librement quand elle soulève une chaise."

    lina "Alex ! Sauve-moi, je crève de chaud !"
    alex "Ton système : je porte, tu supervises en mode bikini ?"
    lina "Exactement. T'as capté vite. Et t'as l'air de pas détester la vue."

    n "Elle se penche pour ramasser une serviette tombée. Son string disparaît presque entre ses fesses rondes. Je détourne les yeux… trop tard."

    n "On bosse une heure. Elle glisse deux fois, finit par terre, riant, corps luisant de sueur et de sable collé à sa peau."

    lina "Cet aprèm, nettoyage piscine. Si je tombe dedans… tu me repêches ? Ou tu me laisses flotter topless pour le fun ?"
    alex "Je… verrai sur le moment."
    lina "C'est une promesse ?"

    hide lina happy
    jump day2_afternoon_intro

label day2_morning_mina:
    scene bg kitchen
    with dissolve
    show mina happy at right

    n "Mina porte un tablier par-dessus un maillot une pièce rouge cerise. La sueur perle sur sa clavicule, descend dans son décolleté quand elle se penche pour trancher le melon."

    mina "Alex… tu arrives pile pour goûter."
    alex "Toujours prêt à tester tes… créations."
    mina "C'est une sauce épicée. Attention, ça peut brûler."

    n "Elle porte la cuillère à mes lèvres. Nos regards se croisent. Sa langue humidifie nerveusement sa lèvre inférieure."

    alex "C'est… intense. Chaud. Parfait."
    mina "Vraiment ? Je… j'aime quand c'est un peu trop."
    alex "Moi aussi."

    n "Elle rougit jusqu'à la poitrine. Le tablier frotte contre ses tétons qui pointent légèrement sous le tissu fin."

    mina "Ce soir… dessert chocolat. Tu seras là pour… goûter encore ?"
    alex "Je raterais ça pour rien au monde."

    hide mina happy
    jump day2_afternoon_intro

label day2_morning_sofia:
    scene bg room
    with dissolve
    show sofia confident at right

    n "Chambre 7. Sofia en paréo semi-transparent, rien dessous visiblement. Elle se penche pour vérifier le matelas – courbe parfaite de ses fesses, tissu qui colle à la peau moite."

    sofia "La clim fuit ici aussi. Tu peux regarder ?"
    alex "Bien sûr."
    sofia "À genoux, alors. C'est plus bas."

    n "Je m'exécute. Elle reste debout juste au-dessus, jambes légèrement écartées. Son parfum – vanille et sel – m'envahit."

    sofia "Tu as des mains habiles, Alex."
    alex "Faut bien réparer ce qui chauffe."
    sofia "Et ça chauffe beaucoup ici… ces derniers jours."

    n "Elle pose une main sur mon épaule pour 'm'aider' à me relever. Contact électrique. Ses doigts s'attardent."

    sofia "Bon boulot. Tu mérites une pause… rafraîchissante cet après-midi."

    hide sofia confident
    jump day2_afternoon_intro

# ── Après-midi Jour 2 – Piscine ─────────────────────────
label day2_afternoon_intro:
    scene bg pool
    with dissolve

    n "{size=+6}{b}🏊 Jour 2 – Après-midi{/b}{/size}"
    n "La piscine est déserte. Eau turquoise, soleil qui tape. Chaleur écrasante. On nettoie… mais l'ambiance est lourde, électrique."

    # Petite scène teasing nu / semi-nu ici, indépendante du choix du matin (pour build-up global)
    n "Lina arrive la première, topless déjà – 'pour bronzer uniformément', dit-elle en riant. Ses seins fermes, bronzés, pointent vers le ciel. Elle plonge sans hésiter, ressort en secouant ses cheveux, gouttes qui perlent sur sa peau nue."

    n "Mina rougit mais enlève son short – reste en maillot une pièce qui moule tout. Sofia observe depuis un transat, paréo ouvert, cuisses écartées juste assez pour laisser deviner."

    n "Je nettoie le bord, torse nu, short trempé qui colle. Les regards se croisent. Personne ne dit rien… mais l'air crépité de tension."

    call afternoon_pool(2)

    jump day2_evening

# ── Soir Jour 2 ──────────────────────────────────────────
label day2_evening:
    scene bg terrace
    with dissolve

    n "{size=+6}{b}🌅 Jour 2 – Soir{/b}{/size}"

    $ _girl, _score = top_girl()

    if _score < 20:
        n "Je dîne seul, la peau encore chaude de soleil et de regards. La nuit promet d'être longue."
        $ current_day += 1
        jump day_router
    elif _girl == "lina":
        jump ev_lina_d2
    elif _girl == "mina":
        jump ev_mina_d2
    else:
        jump ev_sofia_d2

# → Jour 3 dans day3.rpy