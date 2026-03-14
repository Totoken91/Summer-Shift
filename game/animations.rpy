# ════════════════════════════════════════════════════════
# SUMMER SHIFT – animations.rpy
# Transforms UI (adapté depuis modern_fantasy)
# ════════════════════════════════════════════════════════

## Slide léger vers la droite au hover (boutons de menu + choix)
transform choice_select():
    on idle:
        easein 0.3 xoffset 0
    on hover:
        easein 0.3 xoffset 10
    on selected_hover:
        xoffset 10

## Version miroir (slide gauche)
transform choice_select_mirror():
    on idle:
        easein 0.3 xoffset 0
    on hover:
        easein 0.3 xoffset -10
    on selected_hover:
        xoffset -10

## Apparition progressive du badge de sélection au hover
transform selector_appear():
    alpha 0.0
    on idle:
        linear 0.2 alpha 0.0
    on hover:
        pause 0.15
        linear 0.3 alpha 1.0

## Transition rapide entre écrans
define quick_dissolve = Dissolve(0.3)
