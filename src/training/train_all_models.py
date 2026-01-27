import sys

from pathlib import Path
from joblib import Parallel, delayed

from src.training.model_configs import MODEL_CONFIGS
from src.training.train_one import train_single_model

# PROJECT_ROOT = Path(__file__).parent.parent.parent

def main():

    dataset_path = Path("data") / "processed" / "balanced_length_filtered_dataset.csv"

    output_dir = Path("src") / "models"

    results = Parallel(
        n_jobs=3,
        backend="loky",
        verbose=10
    )(
        delayed(train_single_model)(
            config,
            dataset_path,
            output_dir
        )
        for config in MODEL_CONFIGS
    )

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
