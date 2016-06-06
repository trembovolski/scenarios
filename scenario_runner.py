__author__ = 'Kiryl Trembovolski'

from selenium import webdriver
import selenium
import time
import csv

def xpath_finder_wrapper(link):
    while True:
        try:
            output = driver.find_element_by_xpath(link)
        except selenium.common.exceptions.NoSuchElementException:
            continue
        break
    return output

def login(username, password):

    login_button = driver.find_element_by_id("username")
    password_button = driver.find_element_by_id("password")
    submit_login_button = driver.find_element_by_id("submit")

    login_button.send_keys(username)
    password_button.send_keys(password)

    time.sleep(1)

    submit_login_button.click()

    time.sleep(4)

def search(word, num, search_field, counts):

    search_field.send_keys("scenario:%s" % word + str(num))

    time.sleep(2)

    search_field_submit = xpath_finder_wrapper("//div[@class='v-button v-widget search-button v-button-search-button']")
    search_field_submit.click()

    time.sleep(8)

    total_count = xpath_finder_wrapper("//div[@class='v-label v-widget stats-label v-label-stats-label v-has-width']")
    counts[word] = total_count.text.split(' ', 3)[3]

    time.sleep(2)

    search_field.clear()

    time.sleep(2)

if __name__ == '__main__':

    counts = {}
    number = 5
    list_of_words = ["Abuse",
"Aggregate",
"Alter",
"Assist",
"Attack",
"Bait",
"Bend",
"Bluff",
"Boost",
"Breach",
"Bulk",
"Bump",
"Bury",
"Carry",
"Circular",
"Coerce",
"Command",
"Compliance",
"Conceal",
"Confidential",
"Control",
"Corner",
"Crush",
"Damage",
"Deceive",
"Deception",
"Decoy",
"Deploy",
"Disguise",
"Drive",
"Dump",
"Embarrass",
"Enhance",
"Entice",
"Erode",
"Fiddle",
"Fix",
"Flash",
"Fool",
"Force",
"Front run",
"Generate",
"Hammer",
"Help",
"Hide",
"High",
"Humiliate",
"Hush",
"Hustle",
"Idiot",
"Influence",
"Initiate",
"Inside",
"Interpret",
"Junk",
"Large",
"Launder",
"Layer",
"Lead",
"Limit",
"Load",
"Low",
"Lure",
"Manipulate",
"Manoeuvre",
"Mask",
"Mass",
"Move",
"Mug",
"Nudge",
"Obscure",
"Outside",
"Park",
"Ping",
"Piss",
"Private",
"Pull",
"Pump",
"Push",
"Ramp",
"Rape",
"Restore",
"Restrict",
"Rinse",
"Rip",
"Ruin",
"Settle",
"Spike",
"Spoof",
"Squeeze",
"Steal",
"Steer",
"Stuff",
"Sway",
"Sweep",
"Take",
"Terminate",
"Tight lipped",
"Torment",
"Trick",
"Trigger",
"Trust",
"Urge",
"Wash"]

    driver = webdriver.Chrome("/Users/Talinor/Downloads/chromedriver")
    driver.get("http://10.239.2.131:8080/dashboard/secure/dashboard#!search")

    time.sleep(1)

    login("user", "rulethemall")

    search_field = xpath_finder_wrapper("//input[@class='v-textfield v-widget filter-panel-keywords-field v-textfield-filter-panel-keywords-field']")

    start_time = time.time()
    for word in list_of_words:

        search(word, number, search_field, counts)

    finish_time = time.time()-start_time

    print "Execution time: ", finish_time/float(60)
    print counts

    writer = csv.writer(open("/Users/Talinor/counts%s.csv" % str(number), "wb"))
    for key, value in counts.items():
        writer.writerow([key, value])

    time.sleep(3)

    driver.quit()

