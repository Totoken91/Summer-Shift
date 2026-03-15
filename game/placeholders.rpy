# ════════════════════════════════════════════════════════
# SUMMER SHIFT – placeholders.rpy
# ════════════════════════════════════════════════════════
#
# CE FICHIER définit l'écran "art_placeholder" :
# un fond blanc plein écran avec la description de l'illustration
# à venir, pour servir de repère pendant le développement.
#
# ──────────────────────────────────────────────────────
# COMMENT L'UTILISER dans n'importe quel .rpy du jeu :
#
#   call screen art_placeholder("Ta description ici\n• détail 1\n• détail 2")
#
# → L'écran s'affiche en plein écran blanc.
# → Le joueur clique (ou espace / entrée) pour passer.
# → Ensuite le script reprend normalement.
#
# ──────────────────────────────────────────────────────
# COMMENT AJOUTER DES DIALOGUES pendant la scène :
#
# Les dialogues se mettent APRÈS le call screen, pas dedans.
# Exemple :
#
#   call screen art_placeholder("Zara sur la plage\n• Bikini rouge\n• Coucher de soleil")
#   # ↑ L'image placeholder s'affiche. Le joueur clique pour passer.
#
#   show zara happy at right          # ← le sprite apparaît sur le BG du jeu
#   zara "Tu es enfin là !"           # ← dialogue normal après le placeholder
#   elio "Je t'ai cherchée partout."
#   hide zara happy
#   jump next_label
#
# ──────────────────────────────────────────────────────
# COMMENT REMPLACER PAR LE VRAI ART quand il arrive :
#
# Supprimer la ligne `call screen art_placeholder("...")`
# et la remplacer par l'affichage du vrai CG :
#
#   show cg_zara_beach with dissolve   # ← vrai CG plein écran
#   pause                              # ← le joueur clique pour passer
#   hide cg_zara_beach
#
# ──────────────────────────────────────────────────────
# IMPORTANT – règle des crochets dans les strings Ren'Py :
#
# Ren'Py interprète [variable] comme une substitution Python.
# Pour afficher un [ littéral dans n'importe quelle string,
# il faut l'écrire [[ (deux crochets ouvrants).
#
# Exemples :
#   n "[[FULL ART ICI]"    → affiche : [FULL ART ICI]
#   n "[zara_name]"        → affiche la valeur de la variable zara_name
# ════════════════════════════════════════════════════════

screen art_placeholder(description=""):

    # modal True : bloque les clics sur tout ce qui est derrière l'écran
    # (empêche d'avancer le dialogue principal par accident)
    modal True

    # Fond blanc plein écran (1920×1080)
    # Solid("#FFFFFF") = rectangle de couleur unie, pas de fichier image nécessaire
    add Solid("#FFFFFF")

    # frame : conteneur invisible qui occupe tout l'écran
    # xfill/yfill True = s'étire pour remplir tout l'espace disponible
    frame:
        background None  # pas de fond sur le frame lui-même
        xfill True
        yfill True

        # vbox : empile les éléments verticalement
        vbox:
            xalign 0.5   # centré horizontalement
            yalign 0.45  # légèrement au-dessus du centre vertical
            xsize 960    # largeur max du bloc texte (sur 1920px total)
            spacing 40   # espace entre le titre et la description

            # Titre gris clair en haut
            text "✏  ILLUSTRATION À VENIR":
                size 40
                bold True
                color "#CCCCCC"
                xalign 0.5

            # La description passée en paramètre s'affiche ici.
            # Les \n dans la string deviennent des sauts de ligne.
            text description:
                size 26
                color "#333333"
                xalign 0.0
                line_spacing 10  # espace supplémentaire entre chaque ligne

    # Texte d'invite en bas de l'écran
    # [[ = un seul [ affiché (règle d'échappement Ren'Py, voir note ci-dessus)
    text "[[ cliquer pour continuer ]":
        xalign 0.5
        yalign 0.94
        size 22
        color "#BBBBBB"
        italic True

    # Les trois façons de passer l'écran :
    # mouseup_1 = relâchement du clic gauche (plus fluide que mousedown)
    # K_SPACE et K_RETURN = clavier
    # Return() = ferme le screen et reprend le script là où il en était
    key "mouseup_1" action Return()
    key "K_SPACE"   action Return()
    key "K_RETURN"  action Return()
