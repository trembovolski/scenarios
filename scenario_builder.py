__author__ = 'Kiryl Trembovolski'

from selenium import webdriver
import selenium
import time

def xpath_finder_wrapper(link):
    while True:
        try:
            output = driver.find_element_by_xpath(link)
        except selenium.common.exceptions.NoSuchElementException:
            continue
        break
    return output

def login(username, password):

    username_button = driver.find_element_by_id("login-username")
    password_button = driver.find_element_by_id("login-password")
    login_button = driver.find_element_by_id("login-button")

    username_button.send_keys(username)
    password_button.send_keys(password)

    time.sleep(1)

    login_button.click()

    time.sleep(4)

    scenarios_button = xpath_finder_wrapper("//div[text()='Scenarios']")

    scenarios_button.click()

    time.sleep(2)

def add_scenario_code(word, scenario_script):

    scenario_code = xpath_finder_wrapper("//textarea[@class='v-textarea v-widget v-textarea-error v-form-field v-textarea-v-form-field v-textarea-required v-required v-has-width']")
    scenario_code.send_keys(scenario_script % word.lower())

    time.sleep(2)

def add_scenario_name(word, count):

    scenario_name = xpath_finder_wrapper("//input[@class='v-textfield v-widget v-textfield-error v-form-field v-textfield-v-form-field v-textfield-required v-required v-has-width']")
    scenario_name.send_keys(word + str(count))

    time.sleep(2)

def choose_me_group(me_group):

    me_group_button = xpath_finder_wrapper("//select[@class='v-select-twincol-options']/option[text()='%s']" % me_group)
    me_group_button.click()

    time.sleep(2)

    choose_me_group_button = xpath_finder_wrapper("//div[@class='v-select-twincol-buttons']/div[1]")
    choose_me_group_button.click()

    time.sleep(2)

    save_changes_button = xpath_finder_wrapper("//span[text()='save changes']")
    save_changes_button.click()

    time.sleep(2)

def add_scenario(word, scenario_script, count):

    add_button = xpath_finder_wrapper("//section[@class='v-actionbar v-widget open v-actionbar-open v-has-height']/div[2]/ul/li[1]/span[2]")
    add_button.click()

    time.sleep(4)

    add_scenario_code(word,scenario_script)

    add_scenario_name(word, count)

    me_groups_button = xpath_finder_wrapper("//div[@class='dialog-root v-widget dialog-panel dialog-root-dialog-panel v-has-width v-has-height']/div/div[2]/div/div[2]/div/ul/li[2]/div[1]")
    me_groups_button.click()

    time.sleep(2)

    choose_me_group(me_group)

if __name__ == '__main__':

    list_of_words = ["Push",
"Drive",
"Carry",
"Fiddle",
"Pull",
"Nudge",
"Control",
"Bump",
"Abuse",
"Lure",
"Move",
"Urge",
"Confidential",
"Manoeuvre",
"Entice",
"Assist",
"Hammer",
"Outside",
"Decoy",
"Spoof",
"Pump",
"Bait",
"Deploy",
"Terminate",
"Help",
"Dump",
"Junk",
"Influence",
"Damage",
"Wash",
"Force",
"Load",
"Sway",
"Ruin",
"High",
"Coerce",
"Bulk",
"Command",
"Crush",
"Low",
"Circular",
"Generate",
"Bend",
"Squeeze",
"Ping",
"Take",
"Initiate",
"Trust",
"Rip",
"Stuff",
"Lead",
"Boost",
"Private",
"Humiliate",
"Inside",
"Steer",
"Aggregate",
"Restrict",
"Idiot",
"Front run",
"Deception",
"Mass",
"Hush",
"Embarrass",
"Park",
"Deceive",
"Fix",
"Tight lipped",
"Spike",
"Ramp",
"Bluff",
"Corner",
"Conceal",
"Attack",
"Trigger",
"Layer",
"Trick",
"Mask",
"Fool",
"Limit",
"Erode",
"Hustle",
"Obscure",
"Alter",
"Enhance",
"Rinse",
"Restore",
"Bury",
"Flash",
"Interpret",
"Launder",
"Settle",
"Disguise",
"Hide",
"Large",
"Sweep",
"Manipulate",
"Torment",
"Rape",
"Piss",
"Compliance",
"Breach",
"Mug",
"Steal"]

    scenario_script = "Text (value = \"%s\") /+5 EntityList(type = text, name = \"financial_entities\") AND Relationship(type = closeness, value = 1 .. 100) AND ((Content-Info(field = participant_count, value < 9) AND Content-Info(field = type, value = email)) OR NOT Content-Info(field = type, value = email))"
    me_group = "All"

    driver = webdriver.Chrome("/Users/Talinor/Downloads/chromedriver")
    driver.get("http://10.239.2.131:8081/admin/.magnolia/admincentral#app:beh-security:behScenarios;/:listview:")

    login("user", "rulethemall")

    #cycle starts here
    start_time = time.time()
    for word in list_of_words:
        add_scenario(word, scenario_script, 6)

    finish_time = time.time()-start_time

    print "Execution time: ", finish_time/float(60)

    driver.quit()