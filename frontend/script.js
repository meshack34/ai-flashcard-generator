async function generateFlashcards() {
  const text = document.getElementById("inputText").value;

  const response = await fetch("http://127.0.0.1:5000/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });

  const data = await response.json();
  const flashcards = data.flashcards || [];

  const container = document.getElementById("flashcards");
  container.innerHTML = "";

  flashcards.forEach(card => {
    const div = document.createElement("div");
    div.className = "flashcard";
    div.innerHTML = `<strong>Q:</strong> ${card.question}<br><strong>A:</strong> ${card.answer}`;
    container.appendChild(div);
  });
}
