# 🏙️ English Place Name Validator

This Python script prompts the user to enter a place name and validates it.

---

## 📌 Why This Project Matters

In data analytics, bad input leads to bad insights. Ensuring valid location data helps maintain accuracy.

---

## 🚀 Features

- 🚫 Rejects empty, numeric-only, or clearly invalid input  
- ✅ Accepts only alphabetic names of actual places  
- 🌍 Optional: Uses OpenStreetMap (Nominatim) for verification  
- 🔁 Loops until valid location is given  

---

## 💡 Skills Demonstrated

- Input validation and sanitisation  
- Use of external APIs (`requests`)  
- Loop logic and user interaction design  
- Geolocation awareness  
- Clean data practices  

---

## 🛠️ Tech Stack

- Python 3  
- Optional: `requests` library (for API)  
- OpenStreetMap Nominatim API  

---

## ▶️ How to Run

**Basic version (offline):**
```bash
python 09_06_2025_project.py


**With API validation (online):**
```bash
pip install requests
python 09_06_2025_project_api.py