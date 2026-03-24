class NetworkEdge:
    def __init__(self, protocol, trust_level):
        self.protocol = protocol
        self.trust_level = trust_level

    def to_graph_attrs(self):
        return {
            "edge_type": "network",
            "protocol": self.protocol,
            "trust": self.trust_level
        }


# Network edge here means connections are being calculated 