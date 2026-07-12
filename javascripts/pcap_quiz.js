document.addEventListener("DOMContentLoaded", () => {
  const normalize = (values) => values.slice().sort().join(",");

  document.querySelectorAll(".pcap-options").forEach((options) => {
    const button = options.querySelector(".pcap-check");
    const feedback = options.querySelector(".pcap-feedback");
    const solution = options.nextElementSibling;

    if (!button || !feedback || !solution) {
      return;
    }

    button.addEventListener("click", () => {
      const checked = Array.from(options.querySelectorAll("input:checked")).map(
        (input) => input.value
      );
      const expected = options.dataset.answer
        .split(",")
        .map((value) => value.trim())
        .filter(Boolean);

      if (checked.length === 0) {
        feedback.textContent = "Bitte mindestens eine Antwort auswählen.";
        feedback.className = "pcap-feedback";
        return;
      }

      const isCorrect = normalize(checked) === normalize(expected);
      feedback.textContent = isCorrect
        ? "Richtig. Die Lösung ist jetzt geöffnet."
        : `Nicht ganz. Richtige Antwort: ${expected.join(", ")}.`;
      feedback.className = `pcap-feedback ${isCorrect ? "is-correct" : "is-wrong"}`;

      solution.hidden = false;
      solution.open = true;
    });
  });

  document.querySelectorAll(".pcap-reveal").forEach((button) => {
    const solution = button.nextElementSibling;
    if (!solution) {
      return;
    }

    button.addEventListener("click", () => {
      solution.hidden = false;
      solution.open = true;
      button.hidden = true;
    });
  });
});
