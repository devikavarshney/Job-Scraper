from selenium import webdriver
from bs4 import BeautifulSoup
import time
import time


def find_job():
    driver = webdriver.Chrome()
    job_input = input("Enter the job title you want to search: ")
    driver.get(f"https://www.naukri.com/{job_input}-jobs?k={job_input}")
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    job_cards = soup.find_all("div", class_="srp-jobtuple-wrapper")

    for index, jobs in enumerate(job_cards):
        post_date_tag = jobs.find('span', class_="job-post-day")
        post_date = post_date_tag.get_text(
            strip=True) if post_date_tag else "Not Available"

        if post_date.lower() in ["1 day ago", "today", "few hours ago"]:
            job_title_tag = jobs.find("a", class_="title")
            comp_name_tag = jobs.find("a", class_="comp-name mw-25")
            location_tag = jobs.find("span", class_="locWdth")

            job_title = job_title_tag.get_text(
                strip=True) if job_title_tag else "Not Available"
            comp_name = comp_name_tag.get_text(
                strip=True) if comp_name_tag else "Not Available"
            location = location_tag.get_text(
                strip=True) if location_tag else "Not Available"
            link = job_title_tag["href"] if job_title_tag else "No Link"

            skills = [skill.get_text(strip=True) for skill in jobs.find_all(
                "li", class_="dot-gt tag-li")]
            with open(f'jobs/job{index}.txt', 'w') as f:
                f.write(f'''
    Job Title : {job_title}
    Date Posted : {post_date}
    Company : {comp_name}
    Location : {location}
    Skills : {', '.join(skills) if skills else "Not Available"}
    Link to apply : {link}
    ''')
    driver.quit()


if __name__ == "__main__":
    while True:
        find_job()
        time_wait = 10
        print(f'Waiting {time_wait} minutes..')
        time.sleep(time_wait*60)
