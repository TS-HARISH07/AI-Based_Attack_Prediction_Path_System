import networkx as nx


class AttackPathGenerator:
    def __init__(self, graph: nx.DiGraph):
        self.graph = graph

    def get_entry_points(self):
        entry_points = []
        for node, attrs in self.graph.nodes(data=True):
            if attrs.get("node_type") == "host" and attrs.get("privilege") == "low":
                entry_points.append(node)
        return entry_points

    def get_targets(self, min_criticality=8):
        targets = []
        for node, attrs in self.graph.nodes(data=True):
            if (
                attrs.get("node_type") == "host"
                and attrs.get("criticality", 0) >= min_criticality
            ):
                targets.append(node)
        return targets

    def generate_attack_paths(self, max_depth=4):
        attack_paths = []

        entry_points = self.get_entry_points()
        targets = self.get_targets()

        for entry in entry_points:
            for target in targets:
                if entry == target:
                    continue

                try:
                    for path in nx.all_simple_paths(
                        self.graph,
                        source=entry,
                        target=target,
                        cutoff=max_depth
                    ):
                        attack_paths.append(path)
                except nx.NetworkXNoPath:
                    pass

        return attack_paths
