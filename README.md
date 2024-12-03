# K-Line Chart Application

This project demonstrates a web application that displays K-Line data using Flask, SQLite, and Chart.js.

## Project Structure

- `createDB.py`: Script to create the SQLite database and insert sample data.
- `app.py`: Flask application to serve the API endpoint for K-Line data.
- `index.html`: HTML file to display the K-Line chart.
- `script.js`: JavaScript file to fetch data from the API and render the chart using Chart.js.

## Setup Instructions

1. **Create the Database**:
   Run the `createDB.py` script to create the `data.db` database and insert sample data.
	- If you want to update the database, delete the data.db file and run the createDB.py script and inside the script you will be able to add desired parameters.

   ```bash
   python createDB.py

2. Run the Flask Application: Start the Flask application by running app.py.
python app.py -- write this command in git bash or windows powershell but path need to be on this actual folder.

3.Open the HTML File: Open index.html in a web browser to view the K-Line chart.


Dependencies
Flask - pip install Flask             ->  -
Flask-CORS - pip install  Cors        ->   |    need to have python installed on your PC
SQLite3 - pip install sqlite-utils    ->   |
jsonify - pip install jsonify	          -		
Chart.js - npm install chart.js	      ->   |    need to have Node.js installed on your PC

I configurated .bat file for installing this library :installLibrary.bat

