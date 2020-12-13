from indeed import extract_indeed_pages, extract_indeed_jobs

# 0, 1, 2, 3 ... 19 페이지 수를 구하는 함수
last_indeed_page = extract_indeed_pages()

# 구한 페이지수를 url 부분에 넣어서 값을 구하는 함수 
indeed_jobs = extract_indeed_jobs(last_indeed_page)


