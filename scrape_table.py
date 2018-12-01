# -*- coding: utf-8 -*-
"""
Title: Table Scraper
Description: Simple script to scrape a table by id attribute.
Requirements: Selenium, Firefox webdriver 'geckodriver'
Author: Mauro Ferro
Github: https://github.com/ferromauro/tablescraper 
"""

from selenium import webdriver
import csv

def main():    
    url='' #PUT HERE THE URL TO SCRAPE
    target='target_table' # PUT HERE THE ID OF THE TABLE TO SCRAPE
    array_table=[]
    i=1
    driver = webdriver.Firefox()
    driver.get(url)
    table = driver.find_elements_by_xpath(f'//table[@id="{target}"]/tbody/tr')
    for row in table:
        array_row=[]
        if table.index(row)== 0:
            th = row.find_elements_by_tag_name('th')   
            for x in th:
                array_row.append(x.text)
        else:         
            td = row.find_elements_by_tag_name('td')
            for x in td:
                array_row.append(x.text)        
        array_table.append(array_row)
        print(f'Scrivo riga {i}')
        i=i+1
        with open('output.csv', 'w') as f:
            wtr = csv.writer(f)
            for r in array_table:wtr.writerow (r)
    print('TARGET TABLE:')
    print(array_table)  
    print('Table Scraped!!!')    
    driver.close()


if __name__ == '__main__':
    main()
