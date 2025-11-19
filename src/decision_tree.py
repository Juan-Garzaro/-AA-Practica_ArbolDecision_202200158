"""
decision_tree.py
Árbol de decisión minimalista (1 nodo umbral, 2 hojas).
"""


class DecisionTreeThreshold:
    """
    Árbol de decisión con un único nodo basado en un umbral.
    """

    def __init__(self, threshold=50):
        """Inicializa el árbol con el umbral dado."""
        self.threshold = threshold

    def classify(self, value):
        """
        Clasifica el valor según el umbral.
        Retorna "Alto" o "Bajo".
        """
        return "Alto" if value >= self.threshold else "Bajo"
