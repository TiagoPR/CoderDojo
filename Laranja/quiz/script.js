const quizForm = document.getElementById("quiz-form");
const resultsDiv = document.getElementById("results");

quizForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const q1Answer = quizForm.q1.value;
  const q2Answer = quizForm.q2.value;
  let score = 0;
  if (q1Answer === "a") {
    score++;
  }
  if (q2Answer === "b") {
    score++;
  }
  resultsDiv.innerHTML = `Acertaste ${score} de 2.`;
});
