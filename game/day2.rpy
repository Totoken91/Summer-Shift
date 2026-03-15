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
    n "Petit-déjeuner sur la terrasse. Ines, en bikini triangle noir sous un kimono entrouvert, distribue les tâches d'une voix calme mais autoritaire."

    show ines confident at right

    ines "Elio. Aujourd'hui, on accélère. Réparations, réassort, et un œil sur les clients qui pourraient arriver."
    ines "On est peu, mais on reste professionnels… même si la chaleur rend tout un peu plus… distrayant."
    elio "Je gère. Promis."
    ines "J'espère. Ton corps semble déjà s'adapter au climat."

    n "Son regard glisse sur mon torse nu un instant. Je sens la chair de poule malgré les 30°C."

    hide ines confident

    n "Qui accompagner ce matin ? La chaleur monte déjà."

    menu:
        "Rejoindre Zara qui range les chaises longues sur la plage.":
            $ affinity_zara += 10
            jump day2_morning_zara
        "Aider Vesna à préparer le buffet du déjeuner.":
            $ affinity_vesna += 10
            jump day2_morning_vesna
        "Suivre Ines pour l'inventaire des chambres.":
            $ affinity_ines += 10
            jump day2_morning_ines

label day2_morning_zara:
    scene bg beach
    with dissolve
    show zara happy at right

    n "Zara est déjà en sueur : bikini string jaune fluo, top de sport coupé court qui remonte à chaque mouvement. Ses seins rebondissent librement quand elle soulève une chaise."

    zara "Elio ! Sauve-moi, je crève de chaud !"
    elio "Ton système : je porte, tu supervises en mode bikini ?"
    zara "Exactement. T'as capté vite. Et t'as l'air de pas détester la vue."

    n "Elle se penche pour ramasser une serviette tombée. Son string disparaît presque entre ses fesses rondes. Je détourne les yeux… trop tard."

    n "On bosse une heure. Elle glisse deux fois, finit par terre, riant, corps luisant de sueur et de sable collé à sa peau."

    zara "Cet aprèm, nettoyage piscine. Si je tombe dedans… tu me repêches ? Ou tu me laisses flotter topless pour le fun ?"
    elio "Je… verrai sur le moment."
    zara "C'est une promesse ?"

    hide zara happy
    jump day2_afternoon_intro

label day2_morning_vesna:
    scene bg kitchen
    with dissolve
    show vesna happy at right

    n "Vesna porte un tablier par-dessus un maillot une pièce rouge cerise. La sueur perle sur sa clavicule, descend dans son décolleté quand elle se penche pour trancher le melon."

    vesna "Elio… tu arrives pile pour goûter."
    elio "Toujours prêt à tester tes… créations."
    vesna "C'est une sauce épicée. Attention, ça peut brûler."

    n "Elle porte la cuillère à mes lèvres. Nos regards se croisent. Sa langue humidifie nerveusement sa lèvre inférieure."

    elio "C'est… intense. Chaud. Parfait."
    vesna "Vraiment ? Je… j'aime quand c'est un peu trop."
    elio "Moi aussi."

    n "Elle rougit jusqu'à la poitrine. Le tablier frotte contre ses tétons qui pointent légèrement sous le tissu fin."

    vesna "Ce soir… dessert chocolat. Tu seras là pour… goûter encore ?"
    elio "Je raterais ça pour rien au monde."

    hide vesna happy
    jump day2_afternoon_intro

label day2_morning_ines:
    scene bg room
    with dissolve
    show ines confident at right

    n "Chambre 7. Ines en paréo semi-transparent, rien dessous visiblement. Elle se penche pour vérifier le matelas – courbe parfaite de ses fesses, tissu qui colle à la peau moite."

    ines "La clim fuit ici aussi. Tu peux regarder ?"
    elio "Bien sûr."
    ines "À genoux, alors. C'est plus bas."

    n "Je m'exécute. Elle reste debout juste au-dessus, jambes légèrement écartées. Son parfum – vanille et sel – m'envahit."

    ines "Tu as des mains habiles, Elio."
    elio "Faut bien réparer ce qui chauffe."
    ines "Et ça chauffe beaucoup ici… ces derniers jours."

    n "Elle pose une main sur mon épaule pour 'm'aider' à me relever. Contact électrique. Ses doigts s'attardent."

    ines "Bon boulot. Tu mérites une pause… rafraîchissante cet après-midi."

    hide ines confident
    jump day2_afternoon_intro

# ── Après-midi Jour 2 – Piscine ─────────────────────────
label day2_afternoon_intro:
    scene bg pool
    with dissolve

    n "{size=+6}{b}🏊 Jour 2 – Après-midi{/b}{/size}"
    n "La piscine est déserte. Eau turquoise, soleil qui tape. Chaleur écrasante. On nettoie… mais l'ambiance est lourde, électrique."

    # Petite scène teasing nu / semi-nu ici, indépendante du choix du matin (pour build-up global)
    n "Zara arrive la première, topless déjà – 'pour bronzer uniformément', dit-elle en riant. Ses seins fermes, bronzés, pointent vers le ciel. Elle plonge sans hésiter, ressort en secouant ses cheveux, gouttes qui perlent sur sa peau nue."

    n "Vesna rougit mais enlève son short – reste en maillot une pièce qui moule tout. Ines observe depuis un transat, paréo ouvert, cuisses écartées juste assez pour laisser deviner."

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
    elif _girl == "zara":
        jump ev_zara_d2
    elif _girl == "vesna":
        jump ev_vesna_d2
    else:
        jump ev_ines_d2

# → Jour 3 dans day3.rpy