document.getElementById("generatePlan").addEventListener("click", async () => {
  const projectName = prompt("Enter project name:");
  const duration = prompt("How many days will it take?");
  const budget = prompt("Enter project budget:");
  const workers = prompt("Enter the number of workers:");
  const city = prompt("Enter the project location city:");

  if (!projectName || !duration || !budget || !workers || !city) {
    alert("All fields are required!");
    return;
  }

  try {
    const response = await fetch("/generate_plan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        project_name: projectName,
        duration,
        budget,
        workers,
        city,
      }),
    });

    const data = await response.json();
    document.getElementById("output").innerHTML = `
      <h3>AI-Generated Plan:</h3>
      <pre>${JSON.stringify(data, null, 2)}</pre>
    `;
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("output").innerHTML =
      "<p style='color: red;'>Failed to generate plan</p>";
  }
});
