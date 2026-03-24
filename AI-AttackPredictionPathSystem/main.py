from pathlib import Path

from Graph_Engine.Graph_Builder import AttackGraphBuilder
from Prediction_Engine.Models.Attack_Path_Generator import AttackPathGenerator
from Prediction_Engine.Models.Attack_Path_Scorer import AttackPathScorer
from Prediction_Engine.Models.Next_Step_Predictor import NextStepPredictor
from Prediction_Engine.Output_Engine.Prediction_Result import PredictionResult
from Prediction_Engine.Output_Engine.Output_Manager import OutputManager
from RealTime_Engine.Data_Watcher import DataWatcher
from Visualization_Engine.Attack_Graph_Visualizer import AttackGraphVisualizer


DATA_PATH = Path("data/raw")


def run_engine(output_manager):
    # Build attack graph
    builder = AttackGraphBuilder(DATA_PATH)
    graph = builder.build()

    # Generate attack paths
    generator = AttackPathGenerator(graph)
    paths = generator.generate_attack_paths()

    # Score paths
    scorer = AttackPathScorer(graph)
    scored_paths = scorer.score_all_paths(paths)

    # Predict next attacker move
    predictor = NextStepPredictor(graph)

    # Clear previous results
    output_manager.clear()

    for item in scored_paths:
        path = item["path"]
        score = item["score"]

        if len(path) < 2:
            continue

        current_node = path[-2]
        predicted_next = predictor.predict_next_step(current_node)

        result = PredictionResult(
            attack_path=path,
            risk_score=score,
            current_node=current_node,
            predicted_next_node=predicted_next
        )

        output_manager.add_result(result)

    # Display structured console output
    output_manager.display_console()

    # Visualization (show only highest-risk path)
    if output_manager.results:
        top_result = output_manager.results[0]
        visualizer = AttackGraphVisualizer(graph)
        visualizer.draw(
            highlight_path=top_result.attack_path,
            predicted_next=top_result.predicted_next_node
        )


def main():
    print("Real-Time Attack Prediction Engine Started")
    print("Monitoring data changes...\n")

    output_manager = OutputManager()
    watcher = DataWatcher(DATA_PATH)

    # Initial run
    run_engine(output_manager)

    # Real-time monitoring loop
    try:
        for _ in watcher.watch():
            run_engine(output_manager)
    except KeyboardInterrupt:
        print("\nEngine stopped safely by user.")


if __name__ == "__main__":
    main()
