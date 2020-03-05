from selenium import webdriver
from collections import defaultdict
import time
import CreateCSV

def main(url):
    driver = webdriver.Chrome(executable_path=r"C:\Users\Saad\Documents\chromedriver.exe")
    driver.get(url)
    review_chunks = driver.find_elements_by_class_name("ember-view")
    time.sleep(1)
    review_chunks = driver.find_elements_by_css_selector("div[role = 'article']")
    list_reviews =[]
    for review_chunk in review_chunks:
        review = defaultdict(list)
        print(review_chunk.text)
        reviews = review_chunk.find_elements_by_class_name("we-customer-review__body")
        user_review_str = get_p_tags(reviews[0])
        if len(reviews) >1:
            review["relevant"] = 1
            developer_review = get_p_tags(reviews[1])
            review["developer"] = developer_review
        else:
            review["relevant"] = 0
            review["developer"] = ""
        review["user"] = user_review_str
        list_reviews.append(review)
    CreateCSV.create(list_reviews)

def get_p_tags(elem):
    p_tag_str =''
    p_tags = elem.find_elements_by_tag_name("p")
    for i in p_tags:
        text= i.text.strip()
        if text:
            p_tag_str += text
    return p_tag_str

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

