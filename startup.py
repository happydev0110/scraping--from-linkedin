import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/search/results/people/?keywords=%22fixed%20income%22%20and%20(%22head%20of%22%20or%20%22technology%22)&origin=CLUSTER_EXPANSION&sid=kot'

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.content,'html.parser')
# jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')

print(soup)