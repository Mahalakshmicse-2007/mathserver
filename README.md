# Ex.05 Design a Website for Server Side Processing
# Date:20/10/2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lamp Filament Power Calculator</title>
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #a8edea, #fed6e3);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .container {
      background: white;
      padding: 30px;
      border-radius: 20px;
      box-shadow: 0 10px 20px rgba(0,0,0,0.1);
      width: 350px;
      text-align: center;
    }
    h1 {
      color: #ff6b81;
      font-size: 22px;
    }
    label {
      display: block;
      margin-top: 15px;
      font-weight: 600;
      color: #333;
    }
    input {
      width: 80%;
      padding: 8px;
      margin-top: 5px;
      border: 2px solid #ddd;
      border-radius: 8px;
      font-size: 16px;
    }
    button {
      margin-top: 20px;
      background: #ff6b81;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 10px;
      cursor: pointer;
      font-size: 16px;
      transition: 0.3s;
    }
    button:hover {
      background: #ff4757;
    }
    .result {
      margin-top: 20px;
      font-size: 18px;
      font-weight: bold;
      color: #2f3542;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>💡 Lamp Filament Power Calculator</h1>
    <p>Formula: <strong>P = I² × R</strong></p>

    <label for="intensity">Enter Intensity (I in Amperes):</label>
    <input type="number" id="intensity" step="any" placeholder="e.g., 0.5">

    <label for="resistance">Enter Resistance (R in Ohms):</label>
    <input type="number" id="resistance" step="any" placeholder="e.g., 10">

    <button onclick="calculatePower()">Calculate Power</button>

    <div class="result" id="result"></div>
  </div>

  <script>
    function calculatePower() {
      const I = parseFloat(document.getElementById('intensity').value);
      const R = parseFloat(document.getElementById('resistance').value);
      const resultDiv = document.getElementById('result');

      if (isNaN(I) || isNaN(R)) {
        resultDiv.textContent = "⚠️ Please enter both Intensity and Resistance.";
        resultDiv.style.color = "red";
        return;
      }

      const P = (I * I * R).toFixed(2);
      resultDiv.style.color = "#2f3542";
      resultDiv.textContent = `Power (P) = ${P} W`;
    }
  </script>

</body>
</html>
```
# SERVER SIDE PROCESSING:

# HOMEPAGE:
![alt text](<Screenshot 2025-10-01 202047.png>)
# RESULT:
The program for performing server side processing is completed successfully.
