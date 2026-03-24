class PredictionResult:
    def __init__(
        self,
        attack_path,
        risk_score,
        current_node,
        predicted_next_node
    ):
        self.attack_path = attack_path
        self.risk_score = risk_score
        self.current_node = current_node
        self.predicted_next_node = predicted_next_node

    def to_dict(self):
        return {
            "attack_path": self.attack_path,
            "risk_score": self.risk_score,
            "current_node": self.current_node,
            "predicted_next_node": self.predicted_next_node
        }
