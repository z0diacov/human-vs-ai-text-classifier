from pathlib import Path

from src.experiments.combined_model import CombinedModel


model = CombinedModel()
model.init_model()
performance = model.train(
    dataset=Path(__file__).parent / "data" / "processed" / "balanced_length_filtered_dataset.csv",
)
print(performance)
model.save(Path(__file__).parent / "src" / "models" / "combined_model.pkl")