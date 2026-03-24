import json
from datetime import datetime


class OutputManager:
    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def clear(self):
        self.results = []

    def display_console(self):
        print("\n--- REAL-TIME ATTACK INTELLIGENCE ---")
        for r in self.results:
            print(
                "Path:", " -> ".join(r.attack_path),
                "| Risk:", r.risk_score,
                "| Current:", r.current_node,
                "| Predicted Next:", r.predicted_next_node
            )

    def export_json(self, filepath):
        data = {
            "timestamp": datetime.utcnow().isoformat(),
            "results": [r.to_dict() for r in self.results]
        }
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
