# ════════════════════════════════════════════════════════
# SUMMER SHIFT – characters.rpy
# Personnages, variables globales, images placeholders
# ════════════════════════════════════════════════════════

init python:
    def top_girl():
        """Retourne (nom, affinité) de la fille avec l'affinité la plus haute."""
        scores = {
            "zara":  store.affinity_zara,
            "vesna":  store.affinity_vesna,
            "ines": store.affinity_ines,
        }
        if store.lou_available:
            scores["lou"] = store.affinity_lou
        name = max(scores, key=scores.get)
        return name, scores[name]

# ── Personnages ──────────────────────────────────────────
define elio  = Character("Elio",  color="#f0f0f0")
define zara  = Character("Zara",  color="#ff9966")
define vesna  = Character("Vesna",  color="#ff99cc")
define ines = Character("Ines", color="#cc99ff")
define lou = Character("Lou", color="#99ccff")
define n     = Character(None)       # narration (sans nom)

# ── Variables d'affinité (0–100) ─────────────────────────
default affinity_zara  = 0
default affinity_vesna  = 0
default affinity_ines = 0
default affinity_lou = 0

# ── Progression ──────────────────────────────────────────
default current_day     = 1
default lou_available = False    # True à partir du jour 4

# Inventaire d'objets trouvés en point & click
default inventory = set()

# Scènes H déjà débloquées
default seen_zara_h1  = False
default seen_vesna_h1  = False
default seen_ines_h1 = False
default seen_lou_h1 = False

# ── Backgrounds ──────────────────────────────────────────────
# Images 960×640 agrandies à 1920×1080 (zoom=2.0, centrées)
image bg beach      = Transform("images/bg/plagejour.png",     zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)
image bg beach_soir = Transform("images/bg/plage soir.png",    zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)
image bg bar        = Transform("images/bg/bar cool.png",      zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)
image bg kitchen    = Transform("images/bg/salle a manger.png",zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)
image bg terrace    = Transform("images/bg/patio.png",         zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)
image bg pool       = Transform("images/bg/patio.png",         zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)
image bg room       = Transform("images/bg/chambre 1.png",     zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)
image bg resort     = Transform("images/bg/parc.png",          zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)
image bg spring     = Transform("images/bg/parc.png",          zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)
image bg ocean      = Transform("images/bg/plagejour.png",     zoom=2.0, xanchor=0.5, xpos=0.5, yanchor=0.5, ypos=0.5)

# ── Sprites (Composite coloré – remplacer par de vrais PNG) ──
# Zara  (orange chaleureux)
image zara happy     = Composite((300, 580), (0, 0), Solid("#FF9966"))
image zara blush     = Composite((300, 580), (0, 0), Solid("#FF7043"))
image zara laugh     = Composite((300, 580), (0, 0), Solid("#FFB74D"))
image zara surprised = Composite((300, 580), (0, 0), Solid("#FF5722"))
image zara swimsuit  = Composite((300, 580), (0, 0), Solid("#FF8A65"))

# Vesna  (rose poudré)
image vesna happy     = Composite((300, 580), (0, 0), Solid("#F06292"))
image vesna blush     = Composite((300, 580), (0, 0), Solid("#E91E63"))
image vesna shy       = Composite((300, 580), (0, 0), Solid("#F48FB1"))
image vesna surprised = Composite((300, 580), (0, 0), Solid("#EC407A"))
image vesna apron     = Composite((300, 580), (0, 0), Solid("#AD1457"))

# Ines  (violet élégant)
image ines confident = Composite((300, 580), (0, 0), Solid("#9C27B0"))
image ines soft      = Composite((300, 580), (0, 0), Solid("#7B1FA2"))
image ines smirk     = Composite((300, 580), (0, 0), Solid("#AB47BC"))
image ines surprised = Composite((300, 580), (0, 0), Solid("#CE93D8"))
image ines swimsuit  = Composite((300, 580), (0, 0), Solid("#8E24AA"))

# Lou  (bleu ciel)
image lou tsundere = Composite((300, 580), (0, 0), Solid("#42A5F5"))
image lou blush    = Composite((300, 580), (0, 0), Solid("#1976D2"))
image lou shy      = Composite((300, 580), (0, 0), Solid("#90CAF9"))
image lou angry    = Composite((300, 580), (0, 0), Solid("#0D47A1"))
