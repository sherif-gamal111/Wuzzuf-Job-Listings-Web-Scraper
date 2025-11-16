# 📄 Wuzzuf Job Listings Web Scraper

A Python web scraping tool that collects job postings from Wuzzuf.net based on a user-provided job title and number of pages to scrape. The script extracts detailed information from each listing—including job titles, companies, skills, posting dates, status, salary, and full requirements—and exports the results into a structured CSV file for analysis.

---
# ✨ Features

## 🔍 Search by Job Title
Enter any job keyword (e.g., Data Analyst, Python Developer) and scrape multiple result pages.

## 📄 Extracts Detailed Job Information
For every job posting, the scraper collects:

Job Title

Company Name

Job Location

Job Skills

Posting Date

Job Time Status (Full-time, Part-time, etc.)

Job Location Status

Job Link

Salary (scraped from the detailed job page)

Full Requirements (scraped from inside each job post)

## 🌐 Automatic Pagination
Scrapes multiple pages until reaching Wuzzuf’s maximum page limit.

## 💾 CSV Export (UTF-8)
All scraped results are stored in wuzzuf.csv using UTF-8 encoding.

## 🛡 Error Handling
Catches unexpected changes or network issues without breaking the script.

---
# 🛠 Technologies Used

Python 3

Requests — fetches HTML pages

BeautifulSoup4 — HTML parsing

lxml — fast parser

CSV — exporting job data

zip_longest — aligning columns for export

---
# 🚀 How It Works

The user enters:

Please, enter the job you are looking for: Data Engineer
Please, enter the number of page you are looking for (note: write the page - 1): 0


The script sends requests to:

https://wuzzuf.net/search/jobs/?a=hpb&q=<job>&start=<page_number>


From each job card, it extracts:

Title

Company

Skills

Location

Post Date

Status

Link

For each job link, the script opens the job page again and extracts:

Salary

Full list of requirements

All extracted data is exported to:

wuzzuf.csv

---
# 📁 Directory Structure
├── scraper.py
├── wuzzuf.csv        # Generated after running
└── README.md

---
# 📦 Output Example
Job Title	Company	Location	Skills	Post Date	Salary	Requirements
Data Engineer	XYZ	Cairo	Python, SQL	1 day ago	Not specified	Experience with ETL; SQL; APIs…

---
# ▶️ Usage

Install dependencies:

pip install requests
pip install beautifulsoup4
pip install lxml


Run the script:

python scraper.py


The final CSV will be saved to:

D:\Important\Programming\Data\Data_Engineering\Web Scraping\second_project\wuzzuf.csv

---
# ⚠️ Notes

Some fields (e.g., salary) may be missing on certain job postings. These are labeled as "Not specified".

If Wuzzuf changes its HTML structure, selectors may need adjustments.

Pagination is determined by Wuzzuf’s internal layout (15 jobs per page).

---
# 📄 License

This project is open-source under the MIT License.
