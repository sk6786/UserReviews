from selenium import webdriver
from collections import defaultdict
import time
import CreateCSV
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re


def main(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, executable_path=r"C:\Users\Saad\Documents\chromedriver.exe")
    driver.get(url)
    time.sleep(3)
    for i in range(0,100):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    review_chunks = driver.find_elements_by_class_name("ember-view")
    time.sleep(1)
    review_chunks = driver.find_elements_by_css_selector("div[role = 'article']")
    list_reviews =[]
    for review_chunk in review_chunks:
        review = defaultdict(list)
        print(review_chunk.text)
        reviews = review_chunk.find_elements_by_class_name("we-clamp")
        user_review_str = get_p_tags(reviews[0])
        if len(reviews) > 1:
            review["relevant"] = 1
            developer_review = get_p_tags(reviews[1])
            review["developer"] = developer_review
        else:
            review["relevant"] = 0
            review["developer"] = "n/a"
        review["user"] = user_review_str
        list_reviews.append(review)
    CreateCSV.create(list_reviews)

def get_p_tags(elem):
    p_tag_str = ''
    p_tags = elem.find_elements_by_tag_name("p")
    for i in p_tags:
        text = i.get_attribute("innerHTML").strip()
        if text:
            p_tag_str += text + " "
    p_tag_str = p_tag_str.strip()
    return strip_non_ascii(p_tag_str)

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)
# structure = [
#
#     {
#         "user": "blah blah",
#         "relevant": 1,
#         "developer": ""
#
#     },
#
#
# ]







main("https://apps.apple.com/us/app/google-maps-transit-food/id585027354#see-all/reviews")

