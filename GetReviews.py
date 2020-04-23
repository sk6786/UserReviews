from selenium import webdriver
from collections import defaultdict
import time
import CreateCSV
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re


def main(url, filename, ratings = [1,2,3,4,5]):
    irrelevant_count = 0
    relevant_count = 0
    RELEVANT = 500
    IRRELEVANT = 500
    count = 0
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, executable_path=r"C:\Users\Saad\Documents\chromedriver.exe")
    driver.get(url)
    time.sleep(3)
    for i in range(0,400):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    review_chunks = driver.find_elements_by_class_name("ember-view")
    time.sleep(1)
    review_chunks = driver.find_elements_by_css_selector("div[role = 'article']")
    list_reviews =[]
    for review_chunk in review_chunks:
        if count == 1000:
            break
        review = defaultdict(list)
        print(review_chunk.text)
        rating = get_rating(review_chunk)
        if rating in ratings:
            count += 1
            reviews = review_chunk.find_elements_by_class_name("we-clamp")
            user_review_str = get_p_tags(reviews[0])
            if len(reviews) > 1:
                # if relevant_count <= RELEVANT:
                review["relevant"] = 1
                developer_review = get_p_tags(reviews[1])
                review["developer"] = developer_review
                review['rating'] = rating
                relevant_count += 1
                review["user"] = user_review_str
                list_reviews.append(review)
            else:
                # if irrelevant_count <= IRRELEVANT:
                review["relevant"] = 0
                review['rating'] = rating
                review["developer"] = "n/a"
                irrelevant_count += 1
                review["user"] = user_review_str
                list_reviews.append(review)
    CreateCSV.create(list_reviews, filename)



def get_rating(review_chunk):
    dic= {'1 out of 5': 1,'2 out of 5': 2,'3 out of 5': 3,'4 out of 5': 4,'5 out of 5': 5}
    attr = review_chunk.find_element_by_class_name("we-star-rating").get_attribute("aria-label")
    return dic[attr]


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

#
# main("https://apps.apple.com/us/app/slack/id618783545#see-all/reviews", "slackLow.csv", [1,2])
# main("https://apps.apple.com/us/app/slack/id618783545#see-all/reviews", 'slackHigh.csv', [4,5])
# main("https://apps.apple.com/us/app/uber/id368677368#see-all/reviews", 'uberLow.csv', [1,2])
# main("https://apps.apple.com/us/app/uber/id368677368#see-all/reviews", 'uberHigh.csv', [4,5])
# main("https://apps.apple.com/us/app/venmo/id351727428#see-all/reviews",'venmolow.csv', [1,2])
# main("https://apps.apple.com/us/app/venmo/id351727428#see-all/reviews",'venmoHigh.csv', [4,5])
main("https://apps.apple.com/us/app/bitmoji/id868077558#see-all/reviews", "bitmojiLow.csv",[1,2])
main("https://apps.apple.com/us/app/bitmoji/id868077558#see-all/reviews", "bitmojiHigh.csv",[4,5])
