🚀 Naukri Job Scraper

A Python automation tool that scrapes fresh job postings from Naukri.com
 using Selenium + BeautifulSoup.
It filters jobs posted today, yesterday, or a few hours ago and saves details (title, company, skills, location, and apply link) into text files for easy access.

✨ Features

🔎 Search jobs by any title (e.g., Data Scientist, Frontend Developer, Software Engineer).

🕒 Only fetches recent postings (Today, Few hours ago, or 1 day ago).

📂 Saves each job result as a separate text file under /jobs/.

🛠 Uses Selenium for dynamic content & BeautifulSoup for parsing.

🔁 Runs in a loop with custom time intervals (default: 10 minutes).

📌 Example Output (job text file)
Job Title : Software Engineer
Date Posted : Today
Company : Google
Location : Bangalore
Skills : Python, Django, REST API, Cloud
Link to apply : https://www.naukri.com/job-listings-software-engineer-google

🛠 Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/naukri-job-scraper.git
cd naukri-job-scraper

2. Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Requirements File (requirements.txt)
selenium
beautifulsoup4
lxml


You also need Google Chrome and the matching ChromeDriver
 installed.

▶️ Usage

Run the script and enter the job title you want:

python job_scraper.py

Example:
Enter the job title you want to search: data-scientist


It will:

Scrape fresh postings for "data scientist".

Save job details in /jobs/job0.txt, /jobs/job1.txt, etc.

Repeat scraping every 10 minutes.

📂 Project Structure
naukri-job-scraper/
│── job_scraper.py        # Main script
│── requirements.txt      # Dependencies
│── jobs/                 # Folder containing scraped job results
│── README.md             # Documentation

💡 Future Enhancements

Export jobs to CSV / JSON instead of text files.

Add WhatsApp/Telegram/email notifications for new postings.

Support multiple job titles at once.

Add Docker support for easier deployment.

⚠️ Disclaimer

This project is for educational purposes only.
Scraping websites may violate their terms of service. Please use responsibly.

⭐ Show Your Support

If you find this useful, give the repo a star ⭐ and feel free to contribute! 🚀
