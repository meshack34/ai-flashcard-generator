from transformers import pipeline

# Load once at module level
qa_pipeline = pipeline("question-generation")

def generate_flashcards(text):
    result = qa_pipeline(text)
    flashcards = [{"question": qa["question"], "answer": qa["answer"]} for qa in result]
    return flashcards
