from http.server import BaseHTTPRequestHandler,HTTPServer
content ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lamp Filament Power Calculator</title>

  <style>
    body {
      font-family: "Poppins", sans-serif;
      background: linear-gradient(135deg, #a8edea, #fed6e3);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .container {
      background: white;
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 8px 16px rgba(0,0,0,0.2);
      width: 340px;
      text-align: center;
    }

    h1 {
      color: #ff6b81;
      font-size: 22px;
    }

    p {
      font-weight: bold;
      color: #333;
    }

    label {
      display: block;
      text-align: left;
      margin: 10px 0 5px 10%;
      font-weight: 500;
    }

    input {
      width: 80%;
      padding: 8px;
      border: 2px solid #ddd;
      border-radius: 8px;
      font-size: 16px;
      outline: none;
      transition: border 0.3s;
    }

    input:focus {
      border-color: #ff6b81;
    }

    button {
      margin-top: 20px;
      background-color: #ff6b81;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      cursor: pointer;
      transition: background 0.3s;
    }

    button:hover {
      background-color: #ff4757;
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
    <p>Formula: P = I² × R</p>

    <label for="intensity">Enter Intensity (I in Amperes):</label>
    <input type="number" id="intensity" step="any" placeholder="e.g., 0.5">

    <label for="resistance">Enter Resistance (R in Ohms):</label>
    <input type="number" id="resistance" step="any" placeholder="e.g., 10">

    <button onclick="calculatePower()">Calculate Power</button>

    <div class="result" id="result"></div>
  </div>

  <script>
    function calculatePower() {
      const I = parseFloat(document.getElementById("intensity").value);
      const R = parseFloat(document.getElementById("resistance").value);
      const resultDiv = document.getElementById("result");

      if (isNaN(I) || isNaN(R)) {
        resultDiv.style.color = "red";
        resultDiv.textContent = "⚠️ Please enter both Intensity and Resistance!";
        return;
      }

      const P = (I * I * R).toFixed(2);
      resultDiv.style.color = "#2f3542";
      resultDiv.textContent = `Power (P) = ${P} W`;
    }
  </script>

</body>
</html>
'''
from django.shortcuts import render

def lamp_power(request):
    power = None  # Default value if no calculation yet
    if request.method == 'POST':
        try:
            current = float(request.POST.get('current', 0))
            resistance = float(request.POST.get('resistance', 0))
            # Calculate power
            power = current ** 2 * resistance
        except ValueError:
            power = "Invalid input! Please enter numeric values."
    
    return render(request, 'lamp_power.html', {'power': power})
