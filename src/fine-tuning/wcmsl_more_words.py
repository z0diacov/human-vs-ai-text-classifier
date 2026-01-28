import sys

from pathlib import Path

from src.model_impl import WCMSLModel

def main():
    model = WCMSLModel()
    model_path = Path("src") / "models" / "wcmsl_more_words.pkl"
    model.load(model_path)

    fine_tune_dataset = Path("data") / "raw" / "Test_AI_Human.csv"

    performance = model.finetune(fine_tune_dataset)

    print("Fine-tuning completed. New performance:")
    print(performance)

    fine_tuned_model_path = Path("src") / "models" / "wcmsl_more_words_finetuned.pkl"
    model.save(fine_tuned_model_path)


if __name__ == "__main__":
    main()