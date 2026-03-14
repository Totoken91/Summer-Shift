# ════════════════════════════════════════════════════════
# SUMMER SHIFT – characters.rpy
# Personnages, variables globales, images placeholders
# ════════════════════════════════════════════════════════

init python:
    def top_girl():
        """Retourne (nom, affinité) de la fille avec l'affinité la plus haute."""
        scores = {
            "lina":  store.affinity_lina,
            "mina":  store.affinity_mina,
            "sofia": store.affinity_sofia,
        }
        if store.clara_available:
            scores["clara"] = store.affinity_clara
        name = max(scores, key=scores.get)
        return name, scores[name]

# ── Personnages ──────────────────────────────────────────
define alex  = Character("Alex",  color="#f0f0f0")
define lina  = Character("Lina",  color="#ff9966")
define mina  = Character("Mina",  color="#ff99cc")
define sofia = Character("Sofia", color="#cc99ff")
define clara = Character("Clara", color="#99ccff")
define n     = Character(None)       # narration (sans nom)

# ── Variables d'affinité (0–100) ─────────────────────────
default affinity_lina  = 0
default affinity_mina  = 0
default affinity_sofia = 0
default affinity_clara = 0

# ── Progression ──────────────────────────────────────────
default current_day     = 1
default clara_available = False    # True à partir du jour 4

# Inventaire d'objets trouvés en point & click
default inventory = set()

# Scènes H déjà débloquées
default seen_lina_h1  = False
default seen_mina_h1  = False
default seen_sofia_h1 = False
default seen_clara_h1 = False

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
# Lina  (orange chaleureux)
image lina happy     = Composite((300, 580), (0, 0), Solid("#FF9966"))
image lina blush     = Composite((300, 580), (0, 0), Solid("#FF7043"))
image lina laugh     = Composite((300, 580), (0, 0), Solid("#FFB74D"))
image lina surprised = Composite((300, 580), (0, 0), Solid("#FF5722"))
image lina swimsuit  = Composite((300, 580), (0, 0), Solid("#FF8A65"))

# Mina  (rose poudré)
image mina happy     = Composite((300, 580), (0, 0), Solid("#F06292"))
image mina blush     = Composite((300, 580), (0, 0), Solid("#E91E63"))
image mina shy       = Composite((300, 580), (0, 0), Solid("#F48FB1"))
image mina surprised = Composite((300, 580), (0, 0), Solid("#EC407A"))
image mina apron     = Composite((300, 580), (0, 0), Solid("#AD1457"))

# Sofia  (violet élégant)
image sofia confident = Composite((300, 580), (0, 0), Solid("#9C27B0"))
image sofia soft      = Composite((300, 580), (0, 0), Solid("#7B1FA2"))
image sofia smirk     = Composite((300, 580), (0, 0), Solid("#AB47BC"))
image sofia surprised = Composite((300, 580), (0, 0), Solid("#CE93D8"))
image sofia swimsuit  = Composite((300, 580), (0, 0), Solid("#8E24AA"))

# Clara  (bleu ciel)
image clara tsundere = Composite((300, 580), (0, 0), Solid("#42A5F5"))
image clara blush    = Composite((300, 580), (0, 0), Solid("#1976D2"))
image clara shy      = Composite((300, 580), (0, 0), Solid("#90CAF9"))
image clara angry    = Composite((300, 580), (0, 0), Solid("#0D47A1"))
