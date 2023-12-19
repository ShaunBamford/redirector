import webbrowser as wb
import asyncio
import keyboard
import random
import ctypes
# Change console title
ctypes.windll.kernel32.SetConsoleTitleW("Redirector")

## A simple script that directs you to a boring website when key pressed (F2) 
# Title
print("██████╗ ███████╗██████╗ ██╗██████╗ ███████╗ ██████╗████████╗ ██████╗ ██████╗")
print("██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗")
print("██████╔╝█████╗  ██║  ██║██║██████╔╝█████╗  ██║        ██║   ██║   ██║██████╔╝")
print("██╔══██╗██╔══╝  ██║  ██║██║█ ╔══██╗██╔══╝  ██║        ██║   ██║   ██║██╔══██╗")
print("██║  ██║███████╗██████╔╝██║██║  ██║███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║")
print("╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")

# Instructions for user
print("PRESS F2  TO REDIRECT TO A WEBSITE")
print("this doesn't need to be visible on screen, just minimize me! :)")

# Array of websites
websites = [
        "https://en.wikipedia.org/wiki/Doi",'http://www.google.com', 'http://www.bing.com', 'http://www.yahoo.com', 'http://www.duckduckgo.com', 'http://www.amazon.com', 'http://www.ebay.com', 'http://www.wikipedia.org', 'http://stackoverflow.com', 'http://github.com', 'http://www.python.org', 'http://www.microsoft.com', 'http://www.apple.com', 'http://www.adobe.com', 'http://www.oracle.com', 'http://www.ibm.com', 'http://www.netflix.com', 'http://www.hulu.com', 'http://www.disneyplus.com', 'http://www.bbc.com', 'http://www.cnn.com', 'http://www.nytimes.com', 'http://www.theguardian.com', 'http://www.reuters.com', 'http://www.bloomberg.com', 'http://www.forbes.com', 'http://www.businessinsider.com', 'http://techcrunch.com', 'http://www.cnet.com', 'http://www.engadget.com', 'http://www.wired.com', 'http://www.theverge.com', 'http://mashable.com', 'http://www.buzzfeed.com', 'http://www.vice.com', 'http://www.quora.com', 'http://medium.com', 'http://www.ted.com', 'http://www.coursera.org', 'http://www.edx.org', 'http://www.khanacademy.org', 'http://www.udemy.com', 'http://www.codecademy.com', 'http://www.freecodecamp.org', 'http://leetcode.com', 'http://www.hackerrank.com', 'http://www.geeksforgeeks.org', 'http://stackexchange.com', 'http://www.imdb.com', 'http://www.rottentomatoes.com', 'http://www.metacritic.com', 'http://www.goodreads.com', 'http://www.yelp.com', 'http://www.tripadvisor.com', 'http://www.booking.com', 'http://www.airbnb.com', 'http://www.expedia.com', 'http://www.trivago.com', 'http://www.zillow.com', 'http://www.realtor.com', 'http://www.redfin.com', 'http://www.webmd.com', 'http://www.mayoclinic.org', 'http://www.healthline.com', 'http://www.medicalnewstoday.com', 'http://www.nhs.uk', 'http://www.indeed.com', 'http://www.linkedin.com', 'http://www.glassdoor.com', 'http://www.monster.com', 'http://www.simplyhired.com', 'http://www.ziprecruiter.com', 'http://www.themuse.com', 'http://www.angel.co', 'http://www.crunchbase.com', 'http://www.pitchbook.com', 'http://seekingalpha.com', 'http://www.fool.com', 'http://www.investopedia.com', 'http://www.barrons.com', 'http://www.kiplinger.com', 'http://money.usnews.com', 'http://www.nerdwallet.com', 'http://www.bankrate.com', 'http://www.creditkarma.com', 'http://www.mint.com', 'http://www.personalcapital.com', 'http://www.zoho.com', 'http://www.trello.com', 'http://www.asana.com', 'http://www.atlassian.com/software/jira', 'http://www.slack.com', 'http://www.zoom.us', 'http://www.skype.com', 'http://www.webex.com', 'http://www.microsoft.com/en-us/microsoft-teams/group-chat-software', 'http://meet.google.com', 'http://www.dropbox.com', 'http://www.google.com/drive', 'http://www.onedrive.live.com', 'http://www.box.com'
]

# Loop to check if F2 has been pressed
while True:
        if keyboard.is_pressed('F2'):
            # Opens up a random website from websites array
            wb.open(random.choice(websites))