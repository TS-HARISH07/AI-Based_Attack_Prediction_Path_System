class AttackPathFeatureEngine:
    def __init__(self, graph):
        self.graph = graph

    def extract_features(self, path):
        return {
            "path_length": len(path),
            "start_node": path[0],
            "end_node": path[-1]
        }
