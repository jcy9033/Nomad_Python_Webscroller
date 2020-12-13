import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://jp.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        # link.string 으로 가져온 문자열을 array에 넣을 때 숫자로 변경하기 위한 코드
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    # 여기 왜 print 가 들어가는가
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
        # title 과 anchor 를 한번에 찾도록 코드 합치기
        title = result.find("h2", {"class": "title"}).find("a")["title"]
        # inspect 에서 url 이 들어간 회사와 그렇지 않은 회사가 나눠져 있어서 if 사용
        # a(anchor) 는 url 이 걸쳐진 것
        company = result.find("span", {"class": "company"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        # 여백(빈 공간) 지우기 위한 코드
        company = company.strip()
        print(title, company)
    return jobs
