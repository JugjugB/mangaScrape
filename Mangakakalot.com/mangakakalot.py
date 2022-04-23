from urllib.request import Request, urlopen
import re
import os
import smtplib, ssl
import datetime
from email.message import EmailMessage

# load manga list from csv file
if os.path.isfile('mangalist.txt'):
    with open('mangalist.txt', 'r') as f:
        mangalist = f.read().split('\n')
        print(mangalist)

# email details
email = 'example@email.com' # replace with receiver email

port = 465
context = ssl.create_default_context()

for i in mangalist:
    # load all existing chapters from webpage to list
    page = Request(i, headers={'User-Agent': 'Mozilla/5.0'})
    html_bytes = urlopen(page).read()
    html = html_bytes.decode("utf-8")

    # find title
    title = re.search('(?<=<title>).*(?=Manga Online )', html).group(0)

    # get all chapters
    link = i + '/chapter-.*?(?=")'
    linkmatch = list(set(re.findall(link, html)))
    textfile = "chapterlist/" + title + ".txt"

    # function to sort by order of manga chapter
    def sortkey(link):
        res = re.search('chapter-', link)
        try:
            chapnum = int(link[res.end():])
        except ValueError:
            chapnum = float(link[res.end():])
        return chapnum
    
    linkmatch.sort(reverse=True, key=sortkey)

    # load all chapters in file to list
    prevlist = []
    if os.path.isfile(textfile):
        with open(textfile, 'r') as f:
            prevlist = f.readlines()

    # create a list of new chapters (not in prevlist)
    newlist = []
    for j in linkmatch:
        if j + '\n' not in prevlist:
            newlist.append(j)

    # rewrite updated list to file in numerical order
    with open(textfile, 'w') as f:
        for j in linkmatch:
            f.write(j + '\n')

    # send to email if there are new chapters
    message = """
    
    """
    for j in newlist:
        message += j + '\n'

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = title + " (New Chapters)"
    msg['From'] = 'mangabot'
    msg['To'] = email
    
    if len(newlist) > 0:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
            server.login("sender-email@email.com", 'password') # replace with sender email and password   
            server.send_message(msg)
            server.quit()

# log date and time of program execution   
now = str(datetime.datetime.now())
if os.path.isfile('checklog.txt') == False:
    with open('checklog.txt', 'w') as f:
        f.write(now + '\n')
else:
    with open('checklog.txt', 'a') as f:
        f.write(now + '\n')