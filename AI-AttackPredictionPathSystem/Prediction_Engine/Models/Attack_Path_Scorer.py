class AttackPathScorer:
    def __init__(self, graph):
        self.graph = graph

    def score_path(self, path):
        """
        Simple but realistic scoring logic:
        - Higher criticality target → higher score
        - Longer path → higher exposure
        """

        score = 0

        # Score based on target criticality
        target_node = path[-1]
        target_attrs = self.graph.nodes[target_node]
        score += target_attrs.get("criticality", 1) * 10

        # Score based on path length
        score += len(path) * 5

        return score

    def score_all_paths(self, paths):
        """
        Returns paths sorted by highest risk
        """
        scored_paths = []

        for path in paths:
            scored_paths.append({
                "path": path,
                "score": self.score_path(path)
            })

        scored_paths.sort(key=lambda x: x["score"], reverse=True)
        return scored_paths
