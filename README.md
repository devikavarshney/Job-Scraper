# 🔎 Naukri Job Scraper  

A Python-based **job scraper** that automatically extracts the latest job postings from [Naukri.com](https://www.naukri.com) based on user input (e.g., "Python Developer", "Data Scientist").  
The script uses **Selenium** and **BeautifulSoup** to fetch job details and saves them into text files for easy reference.  

---

## ✨ Features
- 🔹 Takes **user input** for job title (e.g., `python`, `java`, `data-scientist`)  
- 🔹 Scrapes only the **latest jobs** (within 1 day / today / few hours ago)  
- 🔹 Extracts the following details:
  - 🏷️ Job Title  
  - 🏢 Company Name  
  - 📍 Location  
  - ⏰ Posted Date  
  - 🛠️ Required Skills  
  - 🔗 Direct Application Link  
- 🔹 Saves results as **individual text files** in the `jobs/` folder  
- 🔹 Runs continuously to **check for new jobs every 10 minutes**  

---

## 🛠️ Tech Stack
- 🐍 Python 3.x  
- 🌐 Selenium – for loading job portal dynamically  
- 🍜 BeautifulSoup (bs4) – for parsing HTML content  
- 🖥️ Chrome WebDriver – for browser automation  

---

## 📂 Project Structure
📦 naukri-job-scraper
┣ 📂 jobs/ # All scraped job details saved here as job0.txt, job1.txt, etc.
┣ 📜 job_scraper.py # Main scraper script
┣ 📜 requirements.txt # Python dependencies
┗ 📜 README.md # Documentation

---

## ⚙️ Installation & Setup

### 1. Clone this repository
git clone https://github.com/your-username/naukri-job-scraper.git
cd naukri-job-scraper
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

---

## ⚙️ Install dependencies
pip install -r requirements.txt

---

## ⚙️ Set up ChromeDriver
Ensure you have Google Chrome installed.
Download the matching ChromeDriver version from ChromeDriver Downloads.
Place the chromedriver file in your project folder or add it to your PATH.

---

## ▶️ Usage
Run the script:
python job_scraper.py
When prompted, enter the job title you want to search:

Enter the job title you want to search: python
The script will:
🔍 Open Naukri.com
📄 Fetch recent job postings
💾 Save job details in the jobs/ folder
⏳ Wait 10 minutes and repeat automatically

---

## 📄 Example Job File (jobs/job0.txt)
Job Title     : Python Developer
Date Posted   : Today
Company       : ABC Technologies
Location      : Bengaluru
Skills        : Django, Flask, REST API
Link to apply : https://www.naukri.com/job-listings-python-developer-abc-tech

---

## 📦 Requirements File (requirements.txt)
selenium
beautifulsoup4
lxml

---

## 🚀 Future Improvements
- Save jobs in CSV/Excel format
- Add filters (experience, salary, remote jobs, etc.)
- Push job alerts via Telegram/WhatsApp
- Deploy as a web app

---

## ⚠️ Disclaimer
This project is for educational purposes only.
Scraping job portals may violate their Terms of Service. Please use responsibly.

---

## 🤝 Contributing
Pull requests are welcome!
If you have ideas to improve this scraper, feel free to open an issue or contribute.
