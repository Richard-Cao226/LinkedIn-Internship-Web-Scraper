from bs4 import BeautifulSoup
import requests
import sys

with open(f'internships.txt', 'w') as f:
	link = input("Enter link: ")
	html_text = requests.get(link)
	while html_text == None:
		print("Invalid link. Please try again.")
		link = input("Enter link: ")
		html_text = requests.get(link)
	html_text = html_text.text
	soup = BeautifulSoup(html_text, 'lxml')
	try:
		jobs = soup.find('ul', class_ = 'jobs-search__results-list').find_all('li')
	except Exception as e:
		print("Website not recognized as LinkedIn job posting page.")
		sys.exit()
	for job in jobs:
		company_name = job.find('a', class_ = 'hidden-nested-link')
		if company_name == None:
			continue
		else:
			company_name = company_name.text.strip()
		location = job.find('span', class_ = 'job-search-card__location')
		if location == None:
			continue
		else:
			location = location.text.strip()
		status = job.find('span', class_ = 'result-benefits__text')
		if status == None:
			continue
		else:
			status = status.text.strip()
		more_info = job.div.a['href']
		
		f.write(f'''
Company: {company_name}
Location: {location}
Status: {status}
More Info: {more_info}
''')
	print("Job postings saved to internships.txt")