document.getElementById('bmiForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;

    const response = await fetch(`http://127.0.0.1:8000/calculate_bmi?weight=${weight}&height=${height}`);
    const data = await response.json();

    document.getElementById('result').innerHTML = `
        <h3>Your BMI: ${data.bmi.toFixed(2)}</h3>
        <p>${data.message}</p>
    `;
});
