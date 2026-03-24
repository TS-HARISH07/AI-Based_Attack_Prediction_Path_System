import networkx as nx
import matplotlib.pyplot as plt


class AttackGraphVisualizer:
    def __init__(self, graph):
        self.graph = graph

    def draw(self, highlight_path=None, predicted_next=None):
        plt.figure(figsize=(12, 8))

        # Stable layout for consistent visuals
        pos = nx.spring_layout(self.graph, seed=42)

        # Node styling
        host_nodes = []
        vuln_nodes = []

        for node, attrs in self.graph.nodes(data=True):
            if attrs.get("node_type") == "host":
                host_nodes.append(node)
            else:
                vuln_nodes.append(node)

        # Draw base graph
        nx.draw_networkx_edges(
            self.graph,
            pos,
            alpha=0.4,
            width=1
        )

        nx.draw_networkx_nodes(
            self.graph,
            pos,
            nodelist=host_nodes,
            node_color="#87CEEB",   
            node_size=1000,
            label="Hosts"
        )

        nx.draw_networkx_nodes(
            self.graph,
            pos,
            nodelist=vuln_nodes,
            node_color="#FFA500", 
            node_size=1000,
            label="Vulnerabilities"
        )

        nx.draw_networkx_labels(
            self.graph,
            pos,
            font_size=9,
            font_weight="bold"
        )

        # Highlight attack path
        if highlight_path and len(highlight_path) > 1:
            path_edges = list(zip(highlight_path, highlight_path[1:]))

            nx.draw_networkx_edges(
                self.graph,
                pos,
                edgelist=path_edges,
                edge_color="red",
                width=3,
                label="Attack Path"
            )

        # Highlight predicted next move
        if predicted_next:
            nx.draw_networkx_nodes(
                self.graph,
                pos,
                nodelist=[predicted_next],
                node_color="red",
                node_size=1000,
                label="Predicted Next Move"
            )

        plt.title("Real-Time Attack Graph with Predicted Attacker Movement")
        plt.legend(scatterpoints=1)
        plt.axis("off")
        plt.tight_layout()
        plt.show()
