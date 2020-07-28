from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def scraper():
    list0 = []
    list1 = []
    list2 = []
    driver = webdriver.Chrome()
    driver.get('https://www.ip-finder.me/ip-full-list/')
    content = driver.page_source
    soup = BeautifulSoup(content)
    #for a in soup.findAll('a', href=True, attrs={'class': 'topIpsDiv'}):
    for a in soup.findAll('div', attrs={'class': 'topIP'}):
        address = a.find('div', attrs={'class': 'ip'})
        block_count = a.find('div', attrs={'class': 'count text-blue'})
        link = a.find('a', href=True, attrs={'class': 'ip'})
        list0.append(address.text)
        list1.append(block_count.text)
        list2.append(link)
        #TODO: Scrape links
    df = pd.DataFrame({'in_address': list0, 'block_count': list1, 'link_to_reason': list2})
    df.to_csv('critical_ip_addresses.csv', index=False, encoding='utf-8')


if __name__ == '__main__':
    scraper()