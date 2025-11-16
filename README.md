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
```
├── wuzzuf.py
├── wuzzuf.csv        # Generated after running
└── README.md
└── License
```

---
# 📦 Output Example

| Job Title               | Company      | Post Date    | Location   | Skills                       | Time Status | Location Status | Salary        | Requirements                                |
| ----------------------- | ------------ | ------------ | ---------- | ---------------------------- | ----------- | --------------- | ------------- | ------------------------------------------- |
| Python Developer        | Digizilla    | 20 hours ago | Cairo      | Python, Django, APIs         | Full-Time   | On-site         | Not specified | Bachelor’s degree; 1–3 years experience…    |
| Senior Backend Engineer | Confidential | 2 days ago   | Cairo      | Python, Node.js, AWS         | Full-Time   | On-site         | Not specified | Strong backend experience; cloud knowledge… |
| Python Instructor       | CodeTreps    | 2 days ago   | Alexandria | Python basics, teaching kids | Part-Time   | On-site         | Not specified | Teaching experience; strong communication…  |

---
  ## ✔ Example Use Cases
  
  You can use the exported data for:
  
  Job market trend analysis
  
  Skill frequency analytics
  
  Salary research
  
  Filtering roles by skill or seniority
  
  Building dashboards
  
  Automating job tracking

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

The script may take a bit long to finish when scraping many pages, because it collects data from both the search results and each individual job page (for salary and requirements).

During execution, the program prints:
Scraped page number: 1
This message indicates that the scraper is actively processing that page and helps the user track loading progress.

---
## 🛡️ License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.

---
## 🌟 About Me

Hi, I’m Sherif, a Data Engineer with a strong foundation in Industrial Engineering and specialized in Data Engineering.
I hold a Bachelor of Engineering (BEng) in Industrial Engineering from Canadian International College (CIC) and a Microsoft Data Engineering degree from Digital Egypt Pioneers Initiative (DEPI).
I am fascinated by how systems work, how processes can be optimized, and how the right information at the right time can change everything. That curiosity led me to Industrial Engineering, and later, to Data Engineering.

Let's stay in touch! Feel free to connect with me on the following platforms:

[LinkedIn](www.linkedin.com/in/sherif-gamal-61a304336)
[Upwork](https://www.upwork.com/freelancers/~01b7b6e3cdf572d79e)
[Freelancer](https://www.freelancer.com/u/SherifGamal5)
[Portfolio](https://sherif-gamal-data-engine-ns2r13f.gamma.site/)
