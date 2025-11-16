import requests
from bs4 import BeautifulSoup
import lxml
import csv
from itertools import zip_longest

job_titles = []
company_names = []
job_skills = []
job_locations = []
job_post_dates = []
job_time_statuss = []
job_location_statuss = []
company_images = []
links = []
salaries = []
requirements = []

job = input("Please, enter the job you are looking for: ")
page_number = int(input("Please, enter the number of page you are looking for (note: write the page - 1): "))

while True:

    try:

        wuzzuf_page = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={job}&start={page_number}")

        src = wuzzuf_page.content
        # print(src)

        soup = BeautifulSoup(src, "lxml")
        # print(soup)

        page_limit = int(soup.find("strong").text)
        # print(page_limit)

        if (page_number > page_limit // 15):
            print("You have reached the maximum number of pages available for this job search.")
            break

        # first we need job title
        # the return value of the find_all is a list
        job_title = soup.find_all("h2", {"class" : "css-193uk2c"})
        # print(job_title)

        company_name = soup.find_all("a", {"class" : "css-ipsyv7"})
        # print(company_name)

        job_location = soup.find_all("span", {"class" : "css-16x61xq"})
        # print(job_location)

        job_skill = soup.find_all("div", {"class" : "css-1rhj4yg"})
        # print(job_skill)

        job_post_new_date = soup.find_all("div", {"class" : "css-eg55jf"})
        # print(job_post_new_date)
        job_post_old_date = soup.find_all("div", {"class" : "css-1jldrig"})
        # print(job_post_old_date)
        post_date = [*job_post_new_date, *job_post_old_date]

        job_time_status = soup.find_all("span", {"class" : "css-uc9rga"})
        # print(job_time_status)

        job_location_status = soup.find_all("span", {"class" : "css-uofntu"})
        # print(job_locatoin_status)

        company_image = soup.find_all("img", {"class" : "css-1in28d3"}) 
        # print(company_image)

        for i in range(len(job_title)):
            job_titles.append(job_title[i].text)
            links.append(job_title[i].find("a").attrs["href"])
            company_names.append(company_name[i].text)
            job_locations.append(job_location[i].text)
            job_skills.append(job_skill[i].text)
            job_post_dates.append(post_date[i].text)
            job_time_statuss.append(job_time_status[i].text)
            job_location_statuss.append(job_location_status[i].text)
            # company_images.append(company_image[i].text)

        page_number += 1
        print(f"Scraped page number: {page_number}")

    except:
        print("An error occurred while trying to scrape the data. Please check your internet connection or the website structure.")
        break

for link in links:
    job_link = requests.get(link)
    src = job_link.content
    soup = BeautifulSoup(src, "lxml")
    salary = soup.find_all("span", {"calss" : "css-2rozun"})
    salaries.append(salary.text.strip() if salary else "Not specified")

    requirement = soup.find("div", {"class" : "css-1lqavbg"})
    requirement_text = ""
    for li in requirement.find_all("li"):
        requirement_text += li.text.strip() + "; "
        requirement_text = requirement_text[:-2]  # to remove the last semicolon and space
    requirements.append(requirement_text)

file_list = [job_titles, company_names, job_post_dates, job_locations, job_skills, job_time_statuss, job_location_statuss, links, salaries, requirements]
exported = zip_longest(*file_list)

with open(r"D:\Important\Programming\Data\Data_Engineering\Web Scraping\second_project\wuzzuf.csv", "w", encoding='utf-8', newline='') as wuzzuf_csv:
    writer = csv.writer(wuzzuf_csv)
    writer.writerow(["Job Title", "Company Name", "Post Date", "Job Location", "Job Skills", "Job Time Status", "Job Location Status", "Links", "Salary", "Requirements"])
    writer.writerows(exported)
