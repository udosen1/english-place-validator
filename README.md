🏙 English Place Name Validator
A Python-based CLI (command-line interface) project that checks if user-entered locations are real places in England, using live data from OpenStreetMap’s Nominatim API.

This tool helps simulate real-world data validation in analytics pipelines, ETL workflows, or user input cleaning, especially for location-based data.

📌 Features
✅ Takes a place name as user input

🌐 Connects to OpenStreetMap Nominatim API

🧠 Filters results to accept only:

Recognised locations in England

Types like city, town, village, hamlet, borough, or administrative

🔁 Loops until a valid English location is entered

📊 Provides clean output for downstream data analysis or dashboards

🧪 Example Usage
bash
Copy
Edit
Which major urban area in England do you live in? abuja
❌ That doesn't appear to be a real place in England. Please try again.

Which major urban area in England do you live in? Manchester
✅ Thank you! Manchester is a valid place in England.
🛠 Technologies Used

Python 3.11+

OpenStreetMap Nominatim API

requests library

Spyder IDE (optional)

📂 Files Included

File Name	Description
place_validator_api.py	Main program that handles API validation
requirements.txt	Contains dependencies to install
README.md	Project overview and documentation
09_06_2025_project.py	(Optional) earlier version using local list

🧰 Setup Instructions

Clone the repository

git clone https://github.com/udosen1/english-place-validator.git
cd english-place-validator
Install dependencies


pip install -r requirements.txt
Run the validator

python place_validator_api.py
🚀 Use Case

This project simulates how real-world data systems validate and clean user-entered location data before it enters a database, dashboard, or model, a core part of:

🧹 ETL pipelines

📊 BI dashboards

🤖 Machine learning preprocessing

🧪 QA & testing environments

👤 Author

Udosen Itoro
📍 Open to roles in data analytics, backend, and data engineering
🔗 GitHub Profile

🏁 Final Notes

✅ This project is fully functional, documented, and API-driven
📬 Contributions and feedback are welcome!