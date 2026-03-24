class HostNode:
    def __init__(self, host_id, hostname, ip, os, role, privilege, criticality):
        self.host_id = host_id
        self.hostname = hostname
        self.ip = ip
        self.os = os
        self.role = role
        self.privilege = privilege
        self.criticality = criticality

    def to_graph_attrs(self):
        return {
            "node_type": "host",
            "hostname": self.hostname,
            "ip": self.ip,
            "os": self.os,
            "role": self.role,
            "privilege": self.privilege,
            "criticality": self.criticality
        }

    
# Host node here means the network assets are modeled
