class NextStepPredictor:
    def __init__(self, graph):
        self.graph = graph

    def predict_next_step(self, current_node):
        """
        Predict the next attacker move based on reachable nodes
        and risk-related attributes.
        """

        candidates = []

        for neighbor in self.graph.successors(current_node):
            attrs = self.graph.nodes[neighbor]
            score = 0

            if attrs.get("node_type") == "host":
                score += attrs.get("criticality", 1) * 10

            if attrs.get("node_type") == "vulnerability":
                score += attrs.get("cvss", 0) * 5

            candidates.append((neighbor, score))

        if not candidates:
            return None

        candidates.sort(key=lambda x: x[1], reverse=True)
        return candidates[0][0]
