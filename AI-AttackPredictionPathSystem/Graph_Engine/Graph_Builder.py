import csv
import json
import networkx as nx
from pathlib import Path

from Graph_Engine.Node_Models.Host_Node import HostNode
from Graph_Engine.Node_Models.Vulnerability_Node import VulnerabilityNode
from Graph_Engine.Edge_Models.Network_Edge import NetworkEdge
from Graph_Engine.Edge_Models.Vulnerability_Edge import VulnerabilityEdge


class AttackGraphBuilder:
    def __init__(self, data_path: Path):
        self.data_path = data_path
        self.graph = nx.DiGraph()

    def _clean_row(self, row):
        cleaned = {}
        for k, v in row.items():
            if k:
                key = k.replace("\ufeff", "").strip().lower()
                value = v.strip() if isinstance(v, str) else v
                cleaned[key] = value
        return cleaned

    def load_hosts(self):
        with open(self.data_path / "network_assets.csv",
                  newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for raw in reader:
                row = self._clean_row(raw)

                host_id = row.get("host_id")
                if not host_id:
                    continue

                try:
                    criticality = int(row.get("criticality", 1))
                except ValueError:
                    criticality = 1

                host = HostNode(
                    host_id,
                    row.get("hostname", "unknown"),
                    row.get("ip_address", "0.0.0.0"),
                    row.get("os", "unknown"),
                    row.get("role", "unknown"),
                    row.get("privilege_level", "low"),
                    criticality
                )

                self.graph.add_node(host.host_id, **host.to_graph_attrs())

    def load_topology(self):
        with open(self.data_path / "topology.json") as f:
            connections = json.load(f)

        for conn in connections:
            edge = NetworkEdge(
                conn.get("protocol", "unknown"),
                conn.get("trust_level", "low")
            )
            self.graph.add_edge(
                conn["source"],
                conn["destination"],
                **edge.to_graph_attrs()
            )

    def load_vulnerabilities(self):
        with open(self.data_path / "vulnerabilities.csv",
                  newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for raw in reader:
                row = self._clean_row(raw)

                vuln_id = row.get("vuln_id")
                host_id = row.get("host_id")
                if not vuln_id or not host_id:
                    continue

                try:
                    cvss = float(row.get("cvss_score", 0))
                except ValueError:
                    cvss = 0.0

                vuln_node_id = f"VULN_{vuln_id}"

                vuln = VulnerabilityNode(
                    vuln_node_id,
                    cvss,
                    row.get("exploitability", "low"),
                    row.get("requires_auth", "no")
                )

                self.graph.add_node(vuln_node_id, **vuln.to_graph_attrs())
                self.graph.add_edge(
                    host_id,
                    vuln_node_id,
                    **VulnerabilityEdge().to_graph_attrs()
                )

    def build(self):
        self.load_hosts()
        self.load_topology()
        self.load_vulnerabilities()
        return self.graph
