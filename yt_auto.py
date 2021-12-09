#using selenium web driver to automate our tasks 
from selenium import webdriver

class video():
    def __init__(self):
        self.driver =webdriver.Edge(executable_path="E:\edgedriver_win64\msedgedriver.exe")

    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        searchVideo = self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        searchVideo.click()
        

# assist=video()
# assist.play('believer by imagine dragons')
