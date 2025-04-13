document.getElementById('predict-form').addEventListener('submit', async function (e) {
    e.preventDefault(); // Stop form from submitting normally

    const form = e.target;
    const size = form.size.value;
    const year = form.year.value;
    const view = form.view.value;

    const response = await fetch('/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ size, year, view })
    });

    const data = await response.json();
    const resultDiv = document.getElementById('result');

    if (response.ok) {
      resultDiv.innerHTML = `<div class="alert alert-success">Predicted Price: <strong>${data.prediction}</strong></div>`;
    } else {
      resultDiv.innerHTML = `<div class="alert alert-danger">Error: ${data.error}</div>`;
    }
  });