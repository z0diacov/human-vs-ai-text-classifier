from dataclasses import dataclass
from config import config


@dataclass
class AllTextMetrics:
    word_count: int
    text_length: int
    sentence_count: int



class TextMetricCalculator:
    
    def __init__(self, text: str):
        self.text = text.strip()
        self.sentences = self._text_to_sentences()

    @property
    def word_count(self) -> int:
        """Calculate the number of words in the text."""
        return len(self.text.split())

    @property
    def text_length(self) -> int:
        """Calculate the length of the text in characters."""
        return len(self.text)
    
    @property
    def sentence_count(self) -> int:
        return max(len(self.sentences), 1)
    
    @property
    def avg_sentence_length(self) -> float:
        return self.text_length / self.sentence_count

    @property
    def all_metrics(self) -> dict:
        """Return all calculated text metrics as a dictionary."""
        return AllTextMetrics(
            word_count=self.word_count,
            text_length=self.text_length
        )


