from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverPath = '/Users/sayak/Desktop/projects/cnnAutomation/chromedriver' # variable holds the file path of the webdriver
driver = webdriver.Chrome(driverPath) # instance of chrome webdriver is created
driver.get("https://www.cnn.com/")

def search(userInput,userNumber):
	"""
		Searches user input on CNN
	"""
	searchButton = driver.find_element_by_class_name('search-icon') # finds the search button and clicks it
	searchButton.send_keys(Keys.RETURN) # presses the enter button
	search = driver.find_element_by_id("header-search-bar")
	search.clear()
	search.send_keys(userInput)# will search user input
	search.send_keys(Keys.RETURN)
	
def getArticles(userNumber):
	"""
		Gets the amount of articles the user wants to read. Includes headline, publish date, and article itself
	"""
	headlineList = []
	publishDateList = []
	articleList = []
	for i in range(1,userNumber+1):
		headline = driver.find_elements_by_xpath("//div[@class='cnn-search__results-list']/div[{}]/div[2]/h3[1]".format(i))
		publishDate = driver.find_elements_by_xpath("//div[@class='cnn-search__results-list']/div[{}]/div[2]/div[1]".format(i))
		article = driver.find_elements_by_xpath("//div[@class='cnn-search__results-list']/div[{}]/div[2]/div[2]".format(i))
		print(headline[0].text)
		headlineList.append(headline[0].text)
		publishDateList.append(publishDate[0].text)
		articleList.append(article[0].text)
	writeToFile(headlineList,publishDateList,articleList,userNumber)

def writeToFile(headlineList,publishDateList,articleList,userNumber):
	with open('output.txt','w') as f:
		for i in range(userNumber):
			f.write(headlineList[i])
			f.write("\n")
			f.write(publishDateList[i])
			f.write("\n")
			f.write(articleList[i])
			f.write("\n")
			f.write("\n")

def main():
	print("Welcome to myNews!")
	userInput = input("Enter what you want to hear about today: ")
	userNumber = int(input("Enter how many articles you want to read: "))
	search(userInput,userNumber)
	getArticles(userNumber)
	time.sleep(3)
	driver.close()


main()