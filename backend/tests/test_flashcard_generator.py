import pytest
from backend.flashcard_generator import generate_flashcards

def test_generate_flashcards():
    text = "The Earth revolves around the Sun in 365 days."
    result = generate_flashcards(text)
    assert isinstance(result, list)
    assert "question" in result[0] and "answer" in result[0]
