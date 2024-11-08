<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corporate Tax Registration Deadline Calculator</title>
    <style>
        body {
            background-color: #121212;
            color: #fff;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            width: 500px;
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .form-group {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .form-group label {
            font-weight: bold;
            flex: 1;
            margin-right: 10px;
            text-align: left;
        }
        .form-group input {
            flex: 2;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: #333;
            color: #fff;
        }
        .form-group.full-width {
            flex-direction: column;
            align-items: flex-start;
        }
        .form-group.full-width label {
            margin-bottom: 5px;
            text-align: left;
        }
        button {
            padding: 10px 20px;
            background-color: #1a73e8;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover {
            background-color: #155ab3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Corporate Tax Registration Deadline Calculator</h1>
        
        <!-- Establishment Date and Company Name in the same row -->
        <div class="form-group">
            <label for="establishmentDate">Establishment Date</label>
            <input type="text" id="establishmentDate" placeholder="Enter the Establishment Date (DD-MM-YYYY or DD/MM/YYYY)">
            <label for="companyName">Company Name</label>
            <input type="text" id="companyName" placeholder="Enter the Company Name">
        </div>
        
        <!-- Deadline field, positioned below -->
        <div class="form-group full-width">
            <label for="deadline">Deadline For Corporate Tax Registration</label>
            <input type="text" id="deadline" placeholder="Calculated Deadline" readonly>
        </div>

        <!-- Button to calculate or submit -->
        <button onclick="calculateDeadline()">Calculate Deadline</button>
    </div>

    <script>
        function calculateDeadline() {
            const establishmentDateInput = document.getElementById("establishmentDate").value;
            const deadlineInput = document.getElementById("deadline");

            // Assuming a fixed deadline calculation here, adjust as per your business logic
            const dateParts = establishmentDateInput.split(/[-/]/);
            const dateObj = new Date(`${dateParts[2]}-${dateParts[1]}-${dateParts[0]}`);
            dateObj.setMonth(dateObj.getMonth() + 6); // Adds 6 months as an example

            const dd = String(dateObj.getDate()).padStart(2, '0');
            const mm = String(dateObj.getMonth() + 1).padStart(2, '0');
            const yyyy = dateObj.getFullYear();

            deadlineInput.value = `${dd}-${mm}-${yyyy}`;
        }
    </script>
</body>
</html>
